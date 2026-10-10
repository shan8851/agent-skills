# parliament: UK Parliament

Package `@shan8851/parliament-cli`, binary `parliament`. Node.js 22+. No key needed. Homepage: https://www.parliament-cli.xyz

Bills, Commons divisions (votes), members of both Houses and written questions, from the official Parliament APIs (Bills, Commons Votes, Members, Written Questions).

## Commands

| Command | What it does |
|---|---|
| `parliament bill <id \| "title">` | One bill by id, or a title resolved to a single match. Returns `shortTitle`, `currentHouse`, `currentStage`, `isAct`, `isDefeated`, `lastUpdate`. |
| `parliament search bills "<query>"` | Search bills by title. `search` supports only `bills`. |
| `parliament divisions <id \| "term">` | One Commons division by id, or search division titles. `votes` is an alias. |
| `parliament member <id \| "name">` | One MP or peer by id, or a name resolved to a single match. Returns `nameDisplayAs`, `party`, `house`. |
| `parliament questions <id \| "term">` | One written question by id, or search question text. |

## Flags

- `--take <n>` (default 10) and `--skip <n>` (default 0) page through search results on `search bills`, `divisions` and `questions`. Paging details are in `data.pagination` (`totalResults`, `returnedCount`).
- `--json`, `--text`, `--no-color` work at root or on the subcommand. `NO_COLOR` is also respected.

## What it can and can't answer

- **"Status of the X Bill"**: `parliament bill "X"`. If it returns `AMBIGUOUS_QUERY`, pick the right `billId` from `error.details.candidates` (they include stage and whether it became an Act) and run `parliament bill <billId>`. A bill that received Royal Assent shows `isAct: true` and the Act's title.
- **"How did MPs vote on…"**: `parliament divisions "<words from the division title>"`, then `parliament divisions <divisionId>`. You get the title, date, and aye and no totals. You don't get how individual MPs voted, and there are no House of Lords divisions. Division titles use formal bill names, so search for "Terminally Ill Adults", not "assisted dying". If a topic search returns nothing, find the bill's formal title first with `parliament search bills`.
- **"Who is the MP for <constituency>?"**: not directly supported. `member` matches names, not constituencies, and the record doesn't include a constituency. Say so, and suggest https://members.parliament.uk/ for a constituency lookup. If the user gives a name, `parliament member "<name>"` confirms party and House.
- **Written questions**: search matches question text. Results include `uin` and `house`.

## Gotchas

- Short or common names ("smith") return `AMBIGUOUS_QUERY` with candidates from both Houses. Filter on `house: "Commons"` when the user asked about an MP.
- An empty `results` list with `ok: true` means nothing matched; try other words before saying it doesn't exist.
- Advanced: the API base URLs can be overridden with `PARLIAMENT_BILLS_API_BASE_URL`, `PARLIAMENT_COMMONS_VOTES_API_BASE_URL`, `PARLIAMENT_MEMBERS_API_BASE_URL` and `PARLIAMENT_QUESTIONS_API_BASE_URL`. Normally leave them alone.
- Exit codes: 0 success, 2 bad input, not found or ambiguous, 3 rate limit or upstream failure, 4 internal error.
