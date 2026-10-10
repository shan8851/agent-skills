# Agent Skills

A small set of skills I actually use with coding agents and personal agents (Claude Code, Codex, OpenClaw and others). Each one encodes a process a plain prompt usually wouldn't follow. Use them as a starting point and adapt them to your own setup.

## Structure

```
skills/
├── personal-agents/             # Capture, recall and reflect on your notes; keep memory tidy
├── thinking-and-communication/  # Understand, check, rehearse, research, write, challenge
├── software-engineering/        # Planning, supply-chain hardening, app screenshots
└── cli-tools/                   # UK public data via JSON-first CLIs
```

Categories are directory-based, so no frontmatter is needed. Skills that depend on your setup include an "Adapting to your setup" section with Claude Code, Codex and OpenClaw examples.

## Install via Skills CLI

```bash
# List skills in this repo
npx skills add shan8851/agent-skills --list

# Install all skills globally
npx skills add shan8851/agent-skills -g --all

# Install selected skills globally
npx skills add shan8851/agent-skills --skill plain-english --skill rehearse -g -y

# Install to project scope (no -g)
npx skills add shan8851/agent-skills --skill research
```

Useful commands:

```bash
npx skills list
npx skills remove <skill-name>
npx skills update
```

## Personal Agents

A simple, portable "second brain" loop for any agent with access to a notes folder: capture → recall → reflect, plus long-term memory hygiene.

- `capture` — Cleans up dictated or quick notes in your own voice, files them in your notes folder and confirms in one line.
- `recall` — Answers "what did I decide about…" questions from your saved notes and memory, with the source, date, confidence and anything newer that changes it.
- `reflect` — Looks back over your recent notes when you ask, citing them: progress, real patterns and open follow-ups, with no forced advice.
- `memory-curation` — Keeps the agent's long-term memory small and accurate: always saves what you ask it to remember, updates rather than duplicates, refuses secrets and tells you what changed.

## Thinking & Communication

Understand things, check you've understood them, and say them well. Useful to anyone, not just developers.

- `plain-english` — Explains confusing letters, documents, contracts and official messages in everyday language: what it says, what to do and by when, with every key point tied to the source.
- `check-my-understanding` — You explain it back in your own words; it credits what's right and fixes misunderstandings one at a time with questions, not lectures.
- `rehearse` — Prepares and role-plays important conversations (pay rises, difficult feedback, landlords, boundaries) with adjustable difficulty, "time out" coaching and a specific debrief.
- `challenge-me` — Stress-tests an idea, plan, product or design with a one-question-at-a-time grilling, then gives a verdict with risks, alternatives and a strength score.
- `research` — A quick take on any link (TL;DR and read/skim/skip verdict) or sourced deep research on a topic, tool or repo, with safe read-only defaults.
- `writing-voice` — Drafts, humanises and critiques posts and emails so they sound like you, learning your voice from your own writing samples. Drafts only; never sends.

## Software Engineering

- `product-planning-doc-pack` — Turns a fuzzy product or feature idea into a lean planning pack: PRD, architecture, surface spec, data sources, a plan built from thin end-to-end slices, and risks.
- `javascript-supply-chain-hardening` — Locks down npm, pnpm, yarn or bun installs with release-age delays, install-script allowlists, frozen installs in CI and Docker, SHA-pinned actions and trusted publishing.
- `local-app-screenshots-and-gif` — Captures same-sized screenshots of a local web app, checks them for private data, and builds a small looping tour GIF for the README.

## CLI Tools

- `uk-public-data` — Answers questions about UK trains, London transport, Parliament, companies and fuel prices using five free, JSON-first CLIs built for agents: [rail](https://rail-cli.xyz), [tfl](https://github.com/shan8851/tfl-cli), [parliament](https://www.parliament-cli.xyz), [ch](https://ch-cli.xyz) (Companies House) and [fuel](https://github.com/shan8851/fuel-cli).

## Credits

- `challenge-me`'s one-question-at-a-time loop is inspired by the "grill me" pattern popularised by Matt Pocock's grill-me skill.
- `product-planning-doc-pack` borrows ideas such as tracer bullets and deep modules from Matt Pocock's skills.

## Licence

MIT. See [LICENSE](LICENSE).

## Site

Browse the skills at [shan8851.com/skills](https://www.shan8851.com/skills).
