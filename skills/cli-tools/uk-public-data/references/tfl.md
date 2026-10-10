# tfl: Transport for London

Package `@shan8851/tfl-cli`, binary `tfl`. Node.js 22+. Homepage: https://github.com/shan8851/tfl-cli

Line status, disruptions, journey planning, live arrivals, stop search and Santander Cycles docks, from the official TfL Unified API.

## Commands

| Command | What it does |
|---|---|
| `tfl status [line]` | Current status of all supported lines, or one (`northern`, `elizabeth`, `overground`). |
| `tfl disruptions [line]` | Current disruption notices. |
| `tfl route <from> <to>` | Journey planner. |
| `tfl arrivals <stop>` | Live arrivals at a stop or station. |
| `tfl search stops <query>` | Find stops and stations; returns ids you can reuse. |
| `tfl bikes <location>` | Nearby Santander Cycles docks with bikes and spaces. |

Locations can be station names, postcodes (`SE1 9SG`), coordinates (`51.50,-0.12`) or TfL stop ids (`940GZZLUWLO`, hub ids like `HUBKGX`).

## Flags

**status, disruptions**
- `--mode <modes>`: comma-separated, from `tube`, `overground`, `dlr`, `elizabeth-line`. Default is all four.
- `--detail` (status only): include TfL's free-text reason, for example the cause of "Minor Delays". Use it whenever a line isn't "Good Service".
- Bus status is out of scope. Trams and river services aren't covered by `status` either.

**route**
- `--date YYYY-MM-DD`, `--time HH:MM`; add `--arrive-by` to treat the time as an arrival time. Without them, it plans for now.
- `--via <location>`.
- `--mode <modes>`: comma-separated, for example `tube,walking`. Values include `public-bus`, `overground`, `train`, `tube`, `coach`, `dlr`, `cablecar`, `tram`, `river`, `walking`, `cycle`, `national-rail`, `elizabeth-line`.
- `--preference least-time | least-interchange | least-walking`.
- `--accessibility <values>`: comma-separated, from `no-requirements`, `no-solid-stairs`, `no-escalators`, `no-elevators`, `step-free-to-vehicle`, `step-free-to-platform`. For "step-free" requests use `step-free-to-platform`, or `step-free-to-vehicle` if the user needs level boarding.
- `--max-walk-minutes <n>`.
- `--output <path>`.

**arrivals**
- `--line <line>`, `--direction inbound | outbound | all`, `--limit <n>` (default 10), `--output <path>`.

**bikes**
- `--radius <metres>` (default 500), `--limit <n>` (default 10), `--output <path>`.

**search stops**
- `--limit <n>` (default 10).

**All commands:** `--json`, `--text`; `tfl --no-color …` or `NO_COLOR`.

## `--output` projection

Available on `route`, `arrivals` and `bikes`. Dot paths with zero-based indexes: `journeys.0.durationMinutes`, `journeys.0.legs`, `arrivals.0.timeToStationSeconds`, `bikePoints.0.bikes`. A malformed path returns `INVALID_INPUT`; a path that doesn't exist returns `NOT_FOUND`. With `--json`, the projected value is returned as `data` inside the normal envelope.

## Key: `TFL_APP_KEY`

Optional. Everything works without it; a key gives higher rate limits. Free from https://api-portal.tfl.gov.uk/ (sign up, then subscribe to a product to get a key). Set it in the environment or `.env`.

## Gotchas

- Ambiguous places return `AMBIGUOUS_LOCATION` with candidates `{ id, name, modes }`. "kings" matches King's Cross, Seven Kings, Kingsbury and more. Re-run with the candidate's `id`.
- A status `severity` of 10 is "Good Service"; lower numbers are worse. Read `description` rather than relying on the number.
- `UNSUPPORTED_MODE` (exit 2) means a mode outside the lists above.
- Journey times are TfL's estimate for the planned time, not a guarantee. Check `status` for the lines the route uses if the user is travelling now.
- Exit codes: 0 success, 2 bad input, not found, ambiguous or unsupported mode, 3 auth, rate limit, timeout or upstream failure, 4 internal error.
