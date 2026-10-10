# rail: National Rail live boards

Package `@shan8851/rail-cli`, binary `rail`. Node.js 22+. Homepage: https://rail-cli.xyz

Live departures and arrivals for every National Rail station in Great Britain, plus station-name search. Data comes from National Rail's Darwin feed (the Live Departure Boards web service, LDBWS) through a Huxley2 proxy.

## Commands

| Command | What it does |
|---|---|
| `rail departures <station>` | Live departures. `<station>` is a name (`"kings cross"`) or a 3-letter CRS code (`KGX`). |
| `rail arrivals <station>` | Live arrivals. |
| `rail search <query>` | Find stations by name. Returns `{ name, crs }` candidates. No token needed. |

## Flags

| Flag | Applies to | Notes |
|---|---|---|
| `--to <station>` | departures | Only services that call at this station. |
| `--from <station>` | arrivals | Only services that called at this station. |
| `--expand` | departures, arrivals | Adds calling points to each service. Larger output; use only when needed. |
| `--limit <n>` | departures, arrivals, search | Default 10. |
| `--select name`, `crs` or `name,crs` | search | Return only those fields. |
| `--stdin` | search | Read newline-separated queries from stdin: `printf "waterloo\nvictoria\n" \| rail search --stdin --json`. Can't be combined with a positional query. |
| `--json` / `--text` | all | Force output format. |
| `--no-color` | root (`rail --no-color departures KGX`) | Or set `NO_COLOR`. |

## Output

`departures` and `arrivals` return `data.station`, `data.filter` (when `--to`/`--from` was used) and `data.services[]`. Each service has `scheduledTime`, `expectedTime` (only when different from scheduled), `status` (`on-time`, `expected`, `delayed`, `cancelled`, `unknown`), `statusLabel`, `platform` (absent until announced), `operatorName`, `counterpartName` (destination for departures, origin for arrivals) and, with `--expand`, `callingPoints`.

The tool does not pass on delay or cancellation reasons, or station messages. Don't make them up; point the user to National Rail Enquiries if they want the reason.

Ambiguous names return `AMBIGUOUS_LOCATION` with `error.details.candidates` (`{ crs, name }`). `"london"` is ambiguous; `"kings cross"` or `KGX` is not. Re-run with the CRS code.

## Token: `DARWIN_ACCESS_TOKEN`

Required for `departures` and `arrivals`. The tool sends it to Huxley2 as an `accessToken` query parameter, and Huxley2 passes it on to National Rail's LDBWS service.

**Where to get one now.** The old registration page (`realtime.nationalrail.co.uk/OpenLDBWSRegistration/...`) no longer exists; it returns 404. National Rail's developer page (https://www.nationalrail.co.uk/developers/darwin-data-feeds/) now sends developers to the Rail Data Marketplace, https://raildata.org.uk/. Register there (free), find the Live Departure Board Web Service (LDBWS) public product in the catalogue, subscribe, and copy the **consumer key** from the subscription's API details.

**Not yet confirmed:** whether a Rail Data Marketplace consumer key works through Huxley2 in the same way as the old tokens did. Third-party guides report that the consumer key works as an LDBWS access token, but National Rail lists the Marketplace product as a JSON API, and Huxley2 talks to the older interface. If the user has a key and `rail departures` returns `AUTH_ERROR` (HTTP 401/403) or a persistent `UPSTREAM_API_ERROR`, say plainly that the key or the backend may not be compatible, rather than retrying.

Third-party guides also say tokens issued under the old scheme still work for now. That isn't confirmed by National Rail, so if an old token starts failing, a Marketplace key is the route to try.

## Backend: `RAIL_API_URL`

Optional. Defaults to `https://huxley2.azurewebsites.net`, the public Huxley2 demo server. It is run by a third party, and its own README says it has no uptime guarantee and regularly goes down. If departures fail with `UPSTREAM_API_ERROR` (exit 3) while `rail search` still works, the demo server or the token is the likely cause. Users who need reliability can run their own Huxley2 instance and set `RAIL_API_URL` to it.

Note: without a token the demo server currently answers board requests with HTTP 500, which the tool reports as a retryable `UPSTREAM_API_ERROR`, not `AUTH_ERROR`. So check `DARWIN_ACCESS_TOKEN` is set before blaming the server.

## Gotchas

- CRS codes are three letters (`KGX` King's Cross, `LDS` Leeds, `EDB` Edinburgh, `MAN` Manchester Piccadilly). Use `rail search` when unsure.
- "Is the 08:15 delayed?": run `departures` from the origin, optionally with `--to`, and find the service whose `scheduledTime` is `08:15`. Boards only cover the next couple of hours, so a train much later in the day won't be there yet; say so.
- Times are local UK time as shown on station boards, with no date.
- Exit codes: 0 success, 2 bad input, not found or ambiguous, 3 auth, rate limit, timeout or upstream failure, 4 internal error.
