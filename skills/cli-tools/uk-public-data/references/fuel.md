# fuel: UK fuel prices

Package `@shan8851/fuel-cli`, binary `fuel`. Node.js 22+. Homepage: https://github.com/shan8851/fuel-cli

Forecourt prices from the UK government's Fuel Finder scheme, ranked by price, distance and how recently each price was updated.

## Commands

| Command | What it does |
|---|---|
| `fuel near "<postcode \| lat,lon>" --fuel <type>` | Stations near a UK postcode or coordinates, for one fuel type. `--fuel` is required. |
| `fuel station "<node id \| text>"` | One station's detail: prices for every fuel, opening times, address. |

## Fuel types

| Code | Fuel |
|---|---|
| `E10` | Standard unleaded petrol |
| `E5` | Super unleaded petrol |
| `B7_STANDARD` | Standard diesel |
| `B7_PREMIUM` | Premium diesel |
| `B10` | B10 biodiesel |
| `HVO` | HVO renewable diesel |

"Petrol" means `E10` unless the user says super; "diesel" means `B7_STANDARD`. Petrol and diesel are never ranked together.

## `near` flags and defaults

- `--radius <distance>`: default 5 miles. A bare number is miles; `8mi` or `8km` also work.
- `--limit <n>`: default 10, maximum 50.
- `--sort best | price | distance | freshest`: default `best`, which balances price, distance and price freshness. For "cheapest", use `--sort price`, but mention how far away it is and how old the price is.
- `--refresh`: download fresh data before answering.
- `--output <path>`, `--json`, `--text`; `fuel --no-color …` or `NO_COLOR`.

The location must be a full UK postcode (`SW1A 1AA`) or `lat,lon` coordinates. Postcode districts (`SW1`) and place names are rejected with `INVALID_INPUT`. If the user gave only a district or a place, either ask for a full postcode or pick a well-known full postcode in that district (say which one you used, and widen `--radius` if needed).

## `station`

Matches a node id exactly, or matches text against the station's name, brand, postcode and first address line. The text match runs against the national dataset the tool keeps in its local cache, not against a live search. Stations are refreshed at most hourly and prices every 15 minutes, and if a download fails the tool quietly falls back to the older cached copy.

So:
- If a station isn't found or its prices look old, run it again with `--refresh` (`fuel station "<query>" --refresh`), or run a `fuel near … --refresh` for the area first.
- Several matches return `AMBIGUOUS_QUERY` with candidates (name, brand, address, postcode, node id). Re-run with the node id.
- Project one value with `--output station.prices.0.pencePerLitre` or a subtree with `--output station.openingTimes`.

## Data quality

Read `data.quality` before answering:
- Each price has a freshness band: `fresh` (updated in the last 30 minutes), `aging` (up to 3 hours), `stale` (older) or `unknown` (no timestamp). `data.quality.freshnessCounts` totals them.
- `data.quality.advisories` lists warnings (stale prices, missing timestamps, excluded test stations). Pass relevant ones on, for example "this price was last updated two days ago".
- Likely test or demo forecourts are hidden when real stations exist; the count is in `data.quality.excludedLikelyTestStations`.

Prices are reported by retailers under the scheme. They can lag the pump, so present them as "reported" prices.

## Credentials: `FUEL_FINDER_CLIENT_ID` and `FUEL_FINDER_CLIENT_SECRET`

Required to download data. Free: sign in with a GOV.UK One Login at the Fuel Finder developer portal, https://www.developer.fuel-finder.service.gov.uk/, and create an application to get a client id and secret. GOV.UK's guidance page is https://www.gov.uk/guidance/access-the-latest-fuel-prices-and-forecourt-data-via-api-or-email.

```sh
export FUEL_FINDER_CLIENT_ID=your_client_id
export FUEL_FINDER_CLIENT_SECRET=your_client_secret
```

Or put the same two lines (without `export`) in a git-ignored `.env`. Without credentials, the tool can still answer from any copy already in its cache (possibly out of date; check freshness). With no cache, every command returns `AUTH_ERROR` (exit 3).

Optional: `FUEL_FINDER_BASE_URL` (API base, defaults to `https://www.fuel-finder.service.gov.uk`) and `FUEL_CACHE_DIR` (cache location; defaults to the platform cache folder).

## Gotchas

- Postcode lookups go through postcodes.io; a typo returns `INVALID_INPUT` or `NOT_FOUND`.
- An empty `stations` list means nothing selling that fuel within the radius. Offer a wider `--radius` rather than saying there's none.
- Exit codes: 0 success, 2 bad input, not found or ambiguous, 3 auth, rate limit, timeout or upstream failure, 4 internal error.
