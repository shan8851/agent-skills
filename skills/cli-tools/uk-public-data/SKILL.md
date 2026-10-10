---
name: uk-public-data
description: Answer questions about UK trains, London transport, Parliament, companies and fuel prices using five free, JSON-first command-line tools built for agents (rail, tfl, parliament, ch, fuel) that read official public data. Use when the user asks things like "next train to Leeds", "is the 08:15 from King's Cross delayed", "is the Northern line running", "how do I get from Waterloo to Bank (step-free)", "how did MPs vote on…", "who is the MP for…", "status of the X Bill", "who are the directors of…", "who owns X Ltd", "is this company still active" or "cheapest diesel near SW1".
---

# UK public data

Five small command-line tools, one per data source. Each returns the same JSON envelope, so once you can read one you can read them all. They are free to install; three need a free API key.

## Which tool for which question

| Question | Tool (npm package) | Command to start with |
|---|---|---|
| National Rail departures, arrivals, delays, station codes | `rail` (`@shan8851/rail-cli`) | `rail departures <station> --to <station>` |
| Tube, Overground, DLR, Elizabeth line status; London journeys; live arrivals; Santander bikes | `tfl` (`@shan8851/tfl-cli`) | `tfl status <line>` / `tfl route <from> <to>` |
| Bills, Commons votes, MPs and peers, written questions | `parliament` (`@shan8851/parliament-cli`) | `parliament bill "<title>"` / `parliament divisions "<term>"` |
| Company profile, status, directors, owners (PSC), filings, charges, insolvency | `ch` (`@shan8851/companies-house-cli`) | `ch search "<name>"` then `ch info <number>` |
| Petrol and diesel prices near a postcode | `fuel` (`@shan8851/fuel-cli`) | `fuel near "<postcode>" --fuel B7_STANDARD` |

Mainline trains into a London terminus are `rail`; the Underground and other TfL services are `tfl`. Bus status is not covered by either.

## Before the first command

1. **Check the tool is installed:** `command -v rail` (macOS/Linux) or `where rail` (Windows). Swap in the binary you need.
2. **If it's missing, ask the user before installing anything.** Offer either a global install, `npm install -g @shan8851/<package>`, or a one-off run with `npx -y @shan8851/<package> <command>`. All five need Node.js 22 or later (`node --version`).
3. **Check for a key if the tool needs one** (table below). If the key is missing, the tool returns `AUTH_ERROR`. Tell the user exactly where to get one; don't guess or work around it.

| Tool | Environment variable | Needed? | Free sign-up |
|---|---|---|---|
| `rail` | `DARWIN_ACCESS_TOKEN` | Required for `departures` and `arrivals`; `search` works without | Rail Data Marketplace, https://raildata.org.uk/ (see `references/rail.md`: the old National Rail sign-up page is gone) |
| `tfl` | `TFL_APP_KEY` | Optional; raises TfL rate limits | https://api-portal.tfl.gov.uk/ |
| `parliament` | none | — | — |
| `ch` | `COMPANIES_HOUSE_API_KEY` | Required for every command | https://developer.company-information.service.gov.uk/ |
| `fuel` | `FUEL_FINDER_CLIENT_ID` and `FUEL_FINDER_CLIENT_SECRET` | Required to download data (a warm local cache can still be read) | https://www.developer.fuel-finder.service.gov.uk/ (needs a GOV.UK One Login) |

Keys go in the shell environment or in a `.env` file in the directory the command runs from (each tool loads `.env` automatically). Make sure that `.env` is git-ignored. Never print, echo, log or commit a key, and never paste one into a command line that ends up in shell history or chat.

## Reading the output

Always add `--json` when you are going to parse the result. Without it, output is text in a terminal and JSON when piped, which is easy to get wrong.

Every response is one envelope:

```json
{ "ok": true,  "schemaVersion": "1", "command": "departures", "requestedAt": "…", "data": { … } }
{ "ok": false, "schemaVersion": "1", "command": "departures", "requestedAt": "…",
  "error": { "code": "AMBIGUOUS_LOCATION", "message": "…", "retryable": false, "details": { … } } }
```

| Exit code | Meaning | What to do |
|---|---|---|
| 0 | Success | Answer from `data`. An empty list is a real answer ("no trains in the next window"), not an error. |
| 2 | Bad input, not found, or ambiguous | Read `error.details.candidates`, then re-run with the exact id or code from the candidate that fits. If more than one could fit, ask the user. |
| 3 | Missing or rejected key, rate limit, timeout, or upstream failure | If `error.retryable` is `true`, retry once after a short pause. If not, report the message. For `AUTH_ERROR`, tell the user how to get or fix the key. |
| 4 | Internal error in the tool | Report it; don't retry in a loop. |

Error codes you will see: `INVALID_INPUT`, `NOT_FOUND`, `AMBIGUOUS_LOCATION` (rail, tfl), `AMBIGUOUS_QUERY` (parliament, fuel), `AUTH_ERROR`, `RATE_LIMITED`, `TIMEOUT`, `UPSTREAM_API_ERROR`, `INTERNAL_ERROR`, and `UNSUPPORTED_MODE` (tfl).

`parliament` and `ch` list commands keep the query under `data.input` and paging under `data.pagination`. `tfl` (route, arrivals, bikes) and `fuel` take `--output <dot.path>` to return one value or subtree, for example `--output journeys.0.durationMinutes`; with `--json` it still comes back inside the envelope as `data`.

## Worked example

User: "When's the next train from King's Cross to Leeds? Is it on time?"

1. `command -v rail` finds the binary, and `DARWIN_ACCESS_TOKEN` is set.
2. Run `rail departures KGX --to LDS --limit 3 --json`. Station names work too (`"kings cross"`), but codes avoid ambiguity. If you only have a vague name, `rail search "kings cross" --json` returns `{ name, crs }` candidates.
3. Read the envelope. `ok` is `true`, so look at `data.services` (illustrative values):
   ```json
   { "station": { "crs": "KGX", "name": "London Kings Cross" },
     "filter": { "crs": "LDS", "name": "Leeds", "type": "to" },
     "services": [
       { "scheduledTime": "14:33", "status": "on-time", "statusLabel": "On time",
         "platform": "5", "operatorName": "London North Eastern Railway", "counterpartName": "Leeds" },
       { "scheduledTime": "15:03", "expectedTime": "15:10", "status": "expected", "statusLabel": "Exp 15:10",
         "operatorName": "London North Eastern Railway", "counterpartName": "Leeds" } ] }
   ```
   `status` is one of `on-time`, `expected` (running late, with `expectedTime`), `delayed` (late, no estimate), `cancelled` or `unknown`. A missing `platform` means it hasn't been announced. Add `--expand` only if the user asks where it calls.
4. Answer in one or two lines: "The next direct train is the 14:33 LNER to Leeds, platform 5, on time. The one after, the 15:03, is expected at 15:10." The tool doesn't return delay reasons, so don't invent one.

If step 2 had returned exit code 2 with `AMBIGUOUS_LOCATION` (for example a bare `"london"`), pick the right CRS code from `error.details.candidates` or ask the user which station they meant. If it had returned `UPSTREAM_API_ERROR` with `retryable: true`, retry once, then tell the user the live feed is unavailable rather than guessing times.

## Limits worth knowing up front

- `parliament` looks members up by name or id, not by constituency, and divisions are Commons only and give totals, not how each MP voted. See `references/parliament.md` for how to handle "who is the MP for…".
- `rail` goes through a third-party Huxley2 server by default, with no uptime guarantee.
- `fuel near` needs a full postcode or coordinates (a district like `SW1` is rejected) and `--fuel` every time. `fuel station` matches names against its local copy of the national dataset.
- Companies House data is what companies filed. "Who owns it" means persons with significant control (`ch psc`), not the full ownership chain.

## References

Read the one you need; don't load them all.

- `references/rail.md`: `rail` commands, flags, token route and the Huxley2 backend.
- `references/tfl.md`: `tfl` status, disruptions, journeys (step-free options), arrivals, bikes.
- `references/parliament.md`: bills, divisions, members, written questions, paging.
- `references/companies-house.md`: search, advanced search, officers, PSC, filings, charges, insolvency.
- `references/fuel.md`: `fuel near`, `fuel station`, fuel types, cache and freshness.
- `references/examples.md`: edge cases (missing key, ambiguous names, upstream down, empty results).
