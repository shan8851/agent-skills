---
name: companies-house-cli
description: UK Companies House CLI — search companies, directors, filings, PSC, charges, insolvency.
category: cli-tool
clawhubUrl: https://clawhub.ai/shan8851/companies-house-cli
---

# companies-house-cli

Use `ch` for UK Companies House data: company search, profiles, officers, filings, PSC, charges, insolvency.

## Setup

- `npm install -g @shan8851/companies-house-cli`
- Get a free API key: https://developer.company-information.service.gov.uk/
- `export COMPANIES_HOUSE_API_KEY=your_key` or add to `.env` in working directory

## Search

- By name: `ch search "Revolut"`
- With restrictions: `ch search "Revolut" --restrictions active-companies`
- Fetch all pages: `ch search "Revolut" --all`

## Company Profile

- By number: `ch info 09215862`
- Short numbers auto-pad: `ch info 9215862` becomes 09215862

## Officers

- List directors/secretaries: `ch officers 09215862`
- All officers (paginated): `ch officers 09215862 --all`
- Order by: `ch officers 09215862 --order-by appointed_on`

## Filings

- Filing history: `ch filings 09215862`
- Filter by type: `ch filings 09215862 --type accounts`
- Include document download links: `ch filings 09215862 --type accounts --include-links`
- All filings: `ch filings 09215862 --all`

## PSC (Beneficial Owners)

- List PSC records: `ch psc 09215862`
- All records: `ch psc 09215862 --all`

## Search Person

- Find a person across all UK companies: `ch search-person "Nik Storonsky"`
- Limit enrichment fan-out: `ch search-person "Nik Storonsky" --match-limit 5`
- Fetch all search pages: `ch search-person "Nik Storonsky" --all`

## Charges

- List company charges: `ch charges 09215862`
- All charges: `ch charges 09215862 --all`

## Insolvency

- Check insolvency history: `ch insolvency 09215862`
- Returns empty result cleanly if no history (not an error)

## Pagination

- All list commands support: `--items-per-page <n>`, `--start-index <n>`, `--all`
- `--all` fetches every page automatically
- `--all` and `--start-index` are mutually exclusive

## Output

- Add `--json` for stable normalized JSON output
- JSON envelope: `{ command, input, pagination, data }`
- Errors go to stderr as JSON when `--json` is set
- Disable colour: `ch --no-color search "Revolut"`

## Notes

- API key required (free, instant signup at Companies House developer portal)
- Auth is HTTP Basic (key as username, blank password)
- Rate limit: 600 requests per 5 minutes
- Company numbers are automatically zero-padded to 8 digits
- `search-person` fans out appointment requests for each match — use `--match-limit` on broad names to control API usage
- `--include-links` on filings derives document content URLs for direct PDF download
