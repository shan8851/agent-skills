# Routing cheatsheet

Use this source router before doing work.

## A) GitHub repo / PR / issue links

Goal: static analysis by default.

Preferred:
- `gh repo view`
- `gh api` for tree/manifests/metadata
- targeted file reads

Do not run:
- `go test`, `npm test`, `make`, setup scripts, project binaries

Only if explicitly requested:
- deeper verification / runtime checks

## B) X/Twitter links or asks

- Use `bird` first.
- If `bird` fails, use web fallback and mark lower confidence.

## C) YouTube links

- Use `summarize "<url>" --youtube auto --cli codex` first.
- Summarize claims, decisions, action items.
- If `--cli codex` is unavailable, fallback to provider/API-backed summarize.
- If `summarize` transcript coverage is weak/fails, fallback to web fetch/search and state fallback.

## D) Direct web URLs (articles/docs/posts)

- Use `summarize "<url>" --cli codex` first.
- If `--cli codex` is unavailable, fallback to provider/API-backed summarize.
- If extraction quality is poor, fallback to `web_fetch` + targeted `web_search`.

## E) General web/topic research

- Use web search + fetch.
- Include Reddit scan where community sentiment is useful:
  - e.g. add `site:reddit.com` query pass.

## F) Unknown/combined inputs

- Split into sub-questions by source type.
- Preserve one unified final output contract.
