# Agent Skills

Skills I use regularly with coding agents.

Use these as a starting point and adapt to your own workflow.

## Structure

```
skills/
├── personal-agents/             # Memory, recall and routines for your own agent
├── thinking-and-communication/  # Understand, check, rehearse, write, challenge
├── software-engineering/        # Dev process & methodology
└── cli-tools/                   # CLI tool companion skills
```

Categories are directory-based — no frontmatter needed. Add a new folder to create a category.

## Install via Skills CLI

```bash
# List skills in this repo
npx skills add shan8851/agent-skills --list

# Install all skills globally
npx skills add shan8851/agent-skills -g --all

# Install selected skills globally
npx skills add shan8851/agent-skills --skill plain-english --skill rehearse -g -y

# Install to project scope (no -g)
npx skills add shan8851/agent-skills --skill research-review
```

Useful commands:

```bash
npx skills list
npx skills remove <skill-name>
npx skills update
```

## Personal Agents

Memory, recall and routines for people running their own agent.

- `agent-self-improvement` — Weekly propose-only review of dumps, memory, context, skills, and crons to suggest workflow improvements.
- `memory-curation` — Curates and promotes memory with signal-first judgment so only durable rules/preferences are stored long-term.
- `recall` — Structured escalation for finding past context from conversations, decisions, or discussions when session memory falls short.
- `weekly-focus-brief` — Produces a user-centric weekly focus brief from dump/memory signals with concrete actions.
- `write-a-skill` — Creates/refines skills with clear triggers, lean structure, and reusable references/scripts.
- `dump` — *(legacy)* Captures raw user dumps into workspace-local markdown logs with no chat response. Kept for older setups.

## Thinking & Communication

Understand things, check you've understood them, and say them well. Useful to anyone, not just developers.

- `plain-english` — Explains confusing letters, documents, contracts and official messages in everyday language: what it says, what to do and by when, with every key point tied to the source.
- `check-my-understanding` — You explain it back in your own words; it credits what's right and fixes misunderstandings one at a time with questions, not lectures.
- `rehearse` — Prepares and role-plays important conversations (pay rises, difficult feedback, landlords, boundaries) with adjustable difficulty, "time out" coaching and a specific debrief.
- `challenge-me` — Stress-tests ideas, plans, projects, and writing concepts with rigorous iterative challenge and tradeoff analysis.
- `rate-content` — Quickly rate a single link/article/post/video/repo with a TL;DR, weighted signal score, recommended action, tags, and evidence notes.
- `research-review` — Unified review workflow for links/repos/posts/videos/topics with safe defaults and concise TL;DR output.
- `writing-voice` — Drafts and polishes posts/emails in user voice with lightweight humanizer + critic pass support.

## Software Engineering

Dev process, planning, and methodology skills.

- `deep-monorepo-code-review` — Deep-review a monorepo after a major refactor by validating branches, splitting review lanes, and synthesizing a triage list.
- `javascript-supply-chain-hardening` — Harden JavaScript/TypeScript repos against npm supply-chain risk with package-manager policy, build-script trust policy, lockfile hygiene, pinning, and CI install gates.
- `local-app-screenshots-and-gif` — Capture screenshots and generate a tour GIF from a locally running web app for README or social posts.
- `product-planning-doc-pack` — Creates focused `planning-docs/` before implementation: PRD, architecture, inferred UX/CLI/API surface spec, source map, risks, working implementation plan, and agent guidance.
- `prompt-first-ai-product` — Build AI products where the prompt IS the product — test-first prompt engineering, iterate before building UI.
- `subagent-driven-development` — Execute implementation plans by dispatching fresh subagents per task with two-stage review.
- `systematic-debugging` — 4-phase root cause investigation for any bug, test failure, or unexpected behavior.
- `writing-plans` — Writes comprehensive implementation plans with bite-sized tasks, exact file paths, and complete code examples.

## CLI Tools

Reference skills for CLI tools — install the tool, then the skill teaches your agent how to use it.

- `companies-house-cli` — UK Companies House data: search companies, directors, filings, PSC, charges, insolvency. [🦞 ClawHub](https://clawhub.ai/shan8851/companies-house-cli) · [🌐 Site](https://ch-cli.xyz)
- `fuel-cli` — UK fuel prices: nearby stations by postcode, ranked by price/distance/freshness.
- `openclaw-blackbox` — OpenClaw run debugging: inspect failed/weird agent runs from local disk evidence. [🦞 ClawHub](https://clawhub.ai/shan8851/openclaw-blackbox) · [🌐 GitHub](https://github.com/shan8851/openclaw-blackbox)
- `parliament-cli` — UK Parliament data: bills, members, divisions, votes, and written questions. [🦞 ClawHub](https://clawhub.ai/shan8851/parliament-cli) · [🌐 Site](https://www.parliment-cli.xyz)
- `rail-cli` — UK National Rail: live departures, arrivals, station search, destination filtering.
- `tfl-cli` — London transport: tube status, journey planning, live arrivals, disruptions, bike docks. [🦞 ClawHub](https://clawhub.ai/shan8851/tfl-cli) · [🌐 Site](https://tfl-cli.xyz)

## Site

Browse the skills at [shan8851.com/skills](https://www.shan8851.com/skills).
