# Edge cases

Short worked cases for the situations that go wrong most often. The JSON is trimmed to the parts that matter.

## 1. Missing key

User: "Who are the directors of Monzo?"

`ch search "Monzo" --json` returns:

```json
{ "ok": false, "command": "search",
  "error": { "code": "AUTH_ERROR", "retryable": false,
    "message": "Missing COMPANIES_HOUSE_API_KEY. Set it in your environment or add it to a local .env file." } }
```

Exit code 3, not retryable. Don't retry, and don't fall back to guessing from memory. Tell the user:

> I need a free Companies House API key for this. Create an account at https://developer.company-information.service.gov.uk/, create an application and add a REST API key, then set it as `COMPANIES_HOUSE_API_KEY` in your shell or a git-ignored `.env` file. Don't paste the key here; I don't need to see it.

The same pattern applies to `rail` (`DARWIN_ACCESS_TOKEN`, see `rail.md` for the current sign-up route) and `fuel` (`FUEL_FINDER_CLIENT_ID` and `FUEL_FINDER_CLIENT_SECRET`). `tfl` and `parliament` don't need a key.

## 2. Ambiguous station or name

User: "Next train from London to Brighton?"

`rail departures "london" --to "brighton" --json` returns exit code 2:

```json
{ "ok": false, "error": { "code": "AMBIGUOUS_LOCATION", "retryable": false,
  "details": { "query": "london", "candidates": [
    { "crs": "BFR", "name": "London Blackfriars" }, { "crs": "LBG", "name": "London Bridge" },
    { "crs": "CST", "name": "London Cannon Street" }, { "crs": "CHX", "name": "London Charing Cross" },
    { "crs": "EUS", "name": "London Euston" } ] } } }
```

The candidate list is short (five here) and alphabetical, so the station the user wants may not be in it: Victoria is missing. Use `rail search "london" --limit 20 --json` to see more. Several London stations have direct trains to Brighton, so don't pick one silently. Either ask ("Victoria, London Bridge or Blackfriars?") or, if the user wants the next train from anywhere in London, run `departures` for each likely station (`VIC`, `LBG`, `BFR`) with `--to BTN --limit 3` and give the earliest, saying which station it leaves from.

When only one candidate fits the context (the user said "the Northern line at King's Cross", and `tfl` offered `HUBKGX` alongside Seven Kings and Kingsbury), re-run with that `id` without asking.

`parliament` and `fuel` use `AMBIGUOUS_QUERY` in the same way: re-run with the `billId`, member `id` or station node id from the candidates.

## 3. Upstream down

User: "Is my 17:42 from Leeds on time?"

`rail departures LDS --json` returns exit code 3:

```json
{ "ok": false, "error": { "code": "UPSTREAM_API_ERROR", "retryable": true, "details": { "status": 500 },
  "message": "Rail departures lookup for \"LDS\" failed with HTTP 500. Set RAIL_API_URL to a working Huxley instance if the public service is unavailable." } }
```

`retryable` is true, so retry once after a few seconds. If it fails again:

1. Check `DARWIN_ACCESS_TOKEN` is set; the public Huxley2 server also answers HTTP 500 when no token is sent.
2. If the token is set, say the live feed isn't responding and suggest checking National Rail Enquiries directly. Mention that the default backend is a third-party server with no uptime guarantee, and that `RAIL_API_URL` can point at another Huxley2 instance.

Never fill the gap with a timetable guess.

## 4. Empty result

User: "How did MPs vote on assisted dying?"

`parliament divisions "assisted dying" --json` returns `ok: true`, exit 0, with `"results": []` and `totalResults: 0`.

An empty list is a valid answer, but here it's a search-term problem: division titles use the bill's formal name. Find it with `parliament search bills "terminally ill"` (it returns the Terminally Ill Adults (End of Life) Bill), then run `parliament divisions "Terminally Ill" --json`. Report the matching divisions with dates and aye and no totals, and say that the tool gives totals, not how individual MPs voted.

Other empty results to read correctly:
- `rail departures … --to …` with no services: no direct trains in the board's window. Say that; don't claim there are no trains at all.
- `ch insolvency <number>` with an empty list: no insolvency history on the register.
- `fuel near … --fuel HVO` with no stations: none within the radius sell it. Offer a larger `--radius`.

## 5. Something the tools can't answer

User: "Who is the MP for Leeds Central and Headingley?"

`parliament member "Leeds Central and Headingley"` returns `NOT_FOUND`, because `member` matches names, not constituencies. Say so plainly, and point to https://members.parliament.uk/ for a constituency search. If the user then names the MP, `parliament member "<name>"` confirms party and House.
