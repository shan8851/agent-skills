---
name: research-review
description: "Unified review/research workflow for links, repos, posts, videos, and topics. Use when the user asks to review, research, summarize, sanity-check, or 'look into' something. Enforce safe defaults: never run untrusted repo code/tests/builds, prefer static analysis, write findings to a notes repo, return a concise TL;DR, and keep the main chat responsive via quick-ack + background execution for longer tasks."
category: workflow
---

# Research Review

Single, safety-first review workflow.

## Non-negotiable defaults

- Do **not** run untrusted project code (`npm test`, `go test`, build scripts, binaries) unless user explicitly asks.
- Do **not** clone into the main workspace.
- Prefer metadata + static reads over local execution.
- Always return a short TL;DR in chat.
- **Do NOT always write to notes.** Apply the persistence decision tree below.

If deep code execution is explicitly requested later, call that out as a mode change and confirm.

## Quick execution flow

1) **Ack immediately**
- If work may exceed ~60–90s, send a quick "on it" response first.
- Use background/sub-agent execution for long jobs so the channel lane stays responsive.

2) **Route by source type**
- Use `references/routing-cheatsheet.md`.
- Route examples:
  - GitHub repo link → static repo review (no code execution).
  - X/Twitter link → social reader tool first.
  - YouTube link → `summarize` first (`--youtube auto`), then fallback.
  - Direct URL/article link → `summarize` first, then fallback to web fetch/search if needed.
  - General topic → web search + fetch (include Reddit scan when useful).

3) **URL/YouTube summarize-first lane**
- For direct article URLs: run `summarize "<url>"` first.
- For YouTube links: run `summarize "<url>" --youtube auto` first.
- If `summarize` fails or coverage is weak, fallback to web search/fetch and explicitly note fallback.
- Never run downloaded code/binaries from target content.

4) **Synthesize**
- Output sections (in this order):
  - TL;DR (2–5 bullets)
  - Why it matters (for the user/request)
  - Risks/caveats
  - Recommended next move

5) **Persistence decision (do NOT default to writing)**

Apply this decision tree:
- **ALWAYS persist** if: user explicitly asks to write it up, OR it's a project/tool we're actively adopting, OR it contains a concrete action plan we'll execute
- **ASK first** if: it's a repo/tool review that might be useful later but isn't immediately actionable — offer: "Want the full write-up in notes or is the TL;DR enough?"
- **SKIP persistence** if: it's a quick sanity check, one-off curiosity, or the TL;DR covers everything useful

When persisting:
- Use `references/note-template.md` format
- Default destination: your configured notes repo or workspace notes directory

6) **Commit + push notes changes** (only when persisting)
- In your notes repo:
  - `git pull --rebase`
  - apply changes
  - `git add -A && git commit -m "..."`
  - `git push`

## Safety mode details

For repo reviews, these are allowed by default:
- README, manifests, file tree, recent commits, CI/workflow files, dependency metadata, docs.

These are blocked by default:
- test/build/run commands
- executing checked-out scripts from target repo
- running downloaded binaries

Optional deep-static mode (still safe):
- cloning to ephemeral scratch (e.g. `/tmp/research/<id>`) for read-only file inspection, then cleanup.

## Quality bar

- Prefer practical, opinionated conclusions over generic summaries.
- Be explicit about confidence and gaps.
- Avoid over-claiming from sparse evidence.
- Keep chat response concise; keep full detail in notes.
