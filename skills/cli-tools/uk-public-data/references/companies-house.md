# ch: Companies House

Package `@shan8851/companies-house-cli`, binary `ch`. Node.js 22+. Homepage: https://ch-cli.xyz

Company search and discovery, profiles, officers, filing history, persons with significant control (PSC), charges and insolvency, from the Companies House Public Data API.

## Commands

| Command | Answers |
|---|---|
| `ch search "<name>"` | Find a company and its number. `--restrictions active-companies` hides dissolved ones. |
| `ch search-advanced <filters>` | Discovery by location, SIC code, status, type and dates (filters below). |
| `ch info <number>` | "Is this company still active?" Status, type, incorporation date, registered office, SIC codes, accounts and confirmation statement dates. |
| `ch officers <number>` | "Who are the directors?" Directors and secretaries, current and resigned. |
| `ch psc <number>` | "Who owns or controls it?" Persons with significant control and their nature of control. |
| `ch filings <number>` | Filing history. |
| `ch charges <number>` | Mortgages and other secured charges. |
| `ch insolvency <number>` | Insolvency history. No history is returned as an empty result, not an error. |
| `ch search-person "<name>"` | Officers matching a name, with their appointments across companies. |

Company numbers are zero-padded automatically: `ch info 9215862` becomes `09215862`. Scottish and other prefixed numbers (`SC123456`, `NI…`, `OC…` for LLPs) are passed as given.

## Flags

**Paging** (search, search-advanced, officers, psc, filings, charges, search-person): `--items-per-page <n>` (default 10), `--start-index <n>` (zero-based), `--all` (fetch every page). `--all` can't be combined with a non-zero `--start-index`. Paging details are in `data.pagination`, the query in `data.input`.

**officers**: `--order-by <field>` (for example `appointed_on`), `--register-type <type>` and `--register-view <true|false>` (passed straight to Companies House; register type is for example `directors`, `secretaries` or `llp-members`).

**psc**: `--register-view <true|false>`.

**filings**: `--category <categories>` (comma-separated, for example `accounts`, `confirmation-statement`, `officers`, `capital`, `incorporation`); `--type` is an alias. `--include-links` adds direct document download URLs.

**search-person**: `--match-limit <n>` (default 10) caps how many matching officers are enriched with their appointments. Each one costs an extra API call, so keep it low for common names.

**search-advanced filters** (at least one is required):
`--company-name-includes <text>`, `--company-name-excludes <text>`, `--company-status <status>` (`active`, `dissolved`…), `--company-type <type>` (`ltd`, `plc`, `llp`…), `--company-subtype <subtype>`, `--location <text>` (registered office), `--sic-codes <codes>` (comma-separated), `--incorporated-from` / `--incorporated-to` and `--dissolved-from` / `--dissolved-to` (`YYYY-MM-DD`).

Examples:
- `ch search-advanced --location Bristol --company-status active --sic-codes 62012 --items-per-page 20 --json`
- `ch search-advanced --company-name-includes bakery --company-name-excludes holdings --location York --json`
- `ch search-advanced --incorporated-from 2025-01-01 --incorporated-to 2025-03-31 --company-type ltd --json`

Results land under `data.companies`. Start with `--items-per-page`; only use `--all` when the full list is really needed.

**Output**: `--json`, `--text` on the subcommand (canonical) or at root (`ch --json search …`); `--no-color` or `NO_COLOR`.

## Key: `COMPANIES_HOUSE_API_KEY`

Required for every command. Free from https://developer.company-information.service.gov.uk/: create an account, create an application, and add a REST API key for the live environment. Set it in the environment or a git-ignored `.env`. The API uses HTTP Basic auth with the key as the username and a blank password; the tool handles that.

Rate limit: 600 requests per 5 minutes per key. `--all` and `search-person` can use many requests; a `RATE_LIMITED` error is retryable after a pause.

## Reading the answers carefully

- **Active or not**: report `companyStatus` exactly as given (`active`, `dissolved`, `liquidation`, `administration`…). "Active" on the register doesn't mean trading. Mention it if `accounts.overdue` or `confirmationStatement.overdue` is true.
- **Directors**: separate current officers from resigned ones (resigned ones have a `resignedOn` date).
- **Ownership**: PSC records show people or entities with over 25% of shares or votes, or significant influence. If the PSC is another company, say so; the chain stops there unless you look that company up too. PSC data is self-reported and may be out of date.
- Companies House data is what companies filed, not verified facts. For due diligence, say what each point is based on.
- `search` matches names loosely; confirm the company number with `ch info` before answering about "X Ltd", especially when several similar names exist.

## Gotchas

- There's no ambiguity error here: `search` returns a list. Pick the best match by exact name and status, or ask the user if several fit.
- Handled errors go to stdout as JSON in `--json` mode, not stderr.
- Exit codes: 0 success, 2 bad input or not found, 3 auth, rate limit or upstream failure, 4 internal error.
