---
name: tfl-cli
description: London transport CLI — tube status, journey planning, live arrivals, disruptions, bike docks.
category: cli-tool
clawhubUrl: https://clawhub.ai/shan8851/tfl-cli
---

# tfl-cli

Use `tfl` for London transport: tube status, journey planning, disruptions, live arrivals, bike availability.

## Setup

- `npm install -g @shan8851/tfl-cli`
- Optional: set `TFL_APP_KEY` env var for higher rate limits (works without any key)

## Status

- All lines: `tfl status`
- Specific line: `tfl status northern`
- Filter by mode: `tfl status --mode tube,dlr`
- With detail: `tfl status --detail`

## Disruptions

- Current disruptions: `tfl disruptions`
- Specific line: `tfl disruptions piccadilly`

## Journey Planning

- Station to station: `tfl route "waterloo" "kings cross"`
- Postcode to postcode: `tfl route "SE1 9SG" "EC2R 8AH"`
- With preferences: `tfl route "waterloo" "paddington" --preference least-interchange`
- Arrive by time: `tfl route "waterloo" "paddington" --arrive-by --time 09:00 --date 2026-03-24`
- Via a waypoint: `tfl route "waterloo" "paddington" --via "bank"`

## Arrivals

- Next arrivals: `tfl arrivals "waterloo"`
- Specific line: `tfl arrivals "waterloo" --line northern`
- Filter direction: `tfl arrivals "waterloo" --direction inbound`
- Limit results: `tfl arrivals "waterloo" --limit 5`

## Bikes

- Near postcode: `tfl bikes "SE1 9SG"`
- Custom radius: `tfl bikes "SE1 9SG" --radius 1000`
- More results: `tfl bikes "SE1 9SG" --limit 20`

## Search

- Find stops/stations: `tfl search stops "paddington"`
- Limit results: `tfl search stops "paddington" --limit 10`

## Output

- All commands default to text in TTY, JSON when piped
- Force JSON: `tfl status --json`
- Force text: `tfl status --text`
- Disable colour: `tfl --no-color status`

## Notes

- No API key required for basic usage
- Accepts station names, postcodes (SE1 9SG), coordinates (51.50,-0.12), and TfL stop IDs
- Status and disruptions cover tube, overground, DLR, and Elizabeth line
- JSON envelope: `{ ok, schemaVersion, command, requestedAt, data }` or `{ ok, schemaVersion, command, requestedAt, error }`
- Exit codes: 0 success, 2 bad input or ambiguity, 3 upstream failure, 4 internal error
- When a station name is ambiguous, the error includes candidate suggestions
