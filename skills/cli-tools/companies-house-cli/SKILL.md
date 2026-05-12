---
name: companies-house-cli
description: UK Companies House CLI — search companies, advanced company discovery by location/SIC/status/type/dates/name filters, profiles, officers, filings, PSC, charges, insolvency, and agent-friendly JSON output aligned with rail-cli and tfl-cli. Use when looking up UK company records, directors, filing history, beneficial owners, charges, insolvency, or building due-diligence/acquisition lead lists from Companies House data.
clawhubUrl: https://clawhub.ai/shan8851/companies-house-cli
---

# companies-house-cli

Use `ch` for UK Companies House data: company search, advanced discovery filters, profiles, officers, filings, PSC, charges, and insolvency.

Setup

- `npm install -g @shan8851/companies-house-cli`
- Requires Node.js 22+.
- Get a free API key: https://developer.company-information.service.gov.uk/
- `export COMPANIES_HOUSE_API_KEY=your_key` or add it to a local `.env`

Search

- By name: `ch search "Revolut"`
- With restrictions: `ch search "Revolut" --restrictions active-companies`
- Fetch all pages: `ch search "Revolut" --all`
- JSON in canonical style: `ch search "Revolut" --json`

Advanced Search

Use `ch search-advanced` when you need discovery rather than exact/name lookup — for example building local acquisition/research lists, finding firms in a geography/SIC niche, or narrowing Companies House by lifecycle dates.

- Location + SIC + status: `ch search-advanced --location "County Durham" --company-status active --sic-codes 69201`
- Name include + location: `ch search-advanced --company-name-includes cleaning --location Sunderland --items-per-page 20`
- Date window as JSON: `ch search-advanced --incorporated-from 2024-01-01 --incorporated-to 2024-12-31 --json`
- Multiple SIC codes: `ch search-advanced --sic-codes 69201,62012 --company-status active`
- Exclude noisy name terms: `ch search-advanced --company-name-includes roofing --company-name-excludes dormant --location Leeds`

Advanced filters

- `--company-name-includes <text>` — company name text that must be included
- `--company-name-excludes <text>` — company name text that must be excluded
- `--company-status <status>` — e.g. `active`, `dissolved`
- `--company-type <type>` — e.g. `ltd`, `plc`, `llp`
- `--company-subtype <subtype>` — Companies House subtype filter
- `--location <location>` — registered office location text
- `--sic-codes <codes>` — comma-separated SIC codes, e.g. `69201,62012`
- `--incorporated-from <date>` / `--incorporated-to <date>` — incorporation date range, `YYYY-MM-DD`
- `--dissolved-from <date>` / `--dissolved-to <date>` — dissolution date range, `YYYY-MM-DD`

Advanced search rules and output

- At least one advanced filter is required; bare `ch search-advanced` is invalid.
- List pagination flags work here too: `--items-per-page <n>`, `--start-index <n>`, `--all`.
- Text output starts with the active filters and pagination summary, then normalized company cards.
- JSON uses command `search-advanced`; filters are under `data.input`, pagination under `data.pagination`, and results under `data.companies`.
- The Companies House advanced endpoint is useful for discovery, but still public registry data; treat it as a first-pass research list, then verify details with `ch info`, `ch officers`, filings, PSC, charges, and external checks.

Company Profile

- By number: `ch info 09215862`
- Force text: `ch info 09215862 --text`
- Short numbers auto-pad: `ch info 9215862` becomes `09215862`

Officers

- List directors/secretaries: `ch officers 09215862`
- All officers: `ch officers 09215862 --all`
- Order by: `ch officers 09215862 --order-by appointed_on`

Filings

- Filing history: `ch filings 09215862`
- Filter by type: `ch filings 09215862 --type accounts`
- Include document download links: `ch filings 09215862 --type accounts --include-links`
- All filings: `ch filings 09215862 --all`

PSC (Beneficial Owners)

- List PSC records: `ch psc 09215862`
- All records: `ch psc 09215862 --all`

Search Person

- Find a person across UK companies: `ch search-person "Nik Storonsky"`
- Limit enrichment fan-out: `ch search-person "Nik Storonsky" --match-limit 5`
- Fetch all search pages: `ch search-person "Nik Storonsky" --all`

Charges

- List company charges: `ch charges 09215862`
- All charges: `ch charges 09215862 --all`

Insolvency

- Check insolvency history: `ch insolvency 09215862`
- Returns empty result cleanly if no history exists (not an error)

Pagination

- List commands support: `--items-per-page <n>`, `--start-index <n>`, `--all`
- `--all` fetches every page automatically
- `--all` and non-zero `--start-index` cannot be combined

Output

- Defaults to text in a TTY and JSON when piped
- Canonical usage is subcommand-local flags: `ch search "Revolut" --json`, `ch info 09215862 --text`, `ch search-advanced --location Durham --json`
- Root compatibility aliases still work: `ch --json search "Revolut"`, `ch --text info 09215862`
- Success envelope: `{ ok, schemaVersion, command, requestedAt, data }`
- Error envelope: `{ ok, schemaVersion, command, requestedAt, error }`
- Command metadata lives under `data.input` and `data.pagination`
- Disable colour: `ch --no-color search "Revolut"` or set `NO_COLOR`

Agent Notes

- JSON mode writes handled errors to stdout, not stderr
- Error payloads include `code`, `message`, and `retryable`
- Exit codes are explicit:
  - `0` success
  - `2` bad input or not found
  - `3` auth, upstream, or rate-limit failures
  - `4` internal failures
- Update any existing parsers that expected top-level `input` or `pagination`; those now live under `data`
- For broad `search-person`, use `--match-limit` to control appointment-enrichment fan-out
- For broad `search-advanced`, prefer `--items-per-page` first; only use `--all` when you really need the full result set

Notes

- API key required (free, instant signup at Companies House developer portal)
- Auth is HTTP Basic (key as username, blank password)
- Rate limit: 600 requests per 5 minutes
- Company numbers are automatically zero-padded to 8 digits
- `search-person` fans out appointment requests for each match — use `--match-limit` on broad names to control API usage
- `--include-links` on filings derives document content URLs for direct PDF download
