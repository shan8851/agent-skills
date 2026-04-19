# agent-skills

![Shan Skills](./assets/skills-header-only.png)

Skills I use regularly with coding agents.

Use these as a starting point and adapt to your own workflow.

## Structure

```
skills/
├── workflow/              # Agent operating patterns
├── software-engineering/  # Dev process & methodology
└── cli-tools/             # CLI tool companion skills
```

Categories are directory-based — no frontmatter needed. Add a new folder to create a category.

## Install via Skills CLI

```bash
# List skills in this repo
npx skills add shan8851/agent-skills --list

# Install all skills globally
npx skills add shan8851/agent-skills -g --all

# Install selected skills globally
npx skills add shan8851/agent-skills --skill writing-voice --skill challenge-me -g -y

# Install to project scope (no -g)
npx skills add shan8851/agent-skills --skill research-review
```

Useful commands:

```bash
npx skills list
npx skills remove <skill-name>
npx skills update
```

## Workflow

Agent operating patterns and prompt workflows — no external tooling required.

- `agent-self-improvement` — Weekly propose-only review of dumps, memory, context, skills, and crons to suggest workflow improvements.
- `challenge-me` — Stress-tests ideas, plans, projects, and writing concepts with rigorous iterative challenge and tradeoff analysis.
- `dump` — Captures raw user dumps into workspace-local markdown logs with no chat response.
- `memory-curation` — Curates and promotes memory with signal-first judgment so only durable rules/preferences are stored long-term.
- `recall` — Structured escalation for finding past context from conversations, decisions, or discussions when session memory falls short.
- `research-review` — Unified review workflow for links/repos/posts/videos/topics with safe defaults and concise TL;DR output.
- `weekly-focus-brief` — Produces a user-centric weekly focus brief from dump/memory signals with concrete actions.
- `write-a-skill` — Creates/refines skills with clear triggers, lean structure, and reusable references/scripts.
- `writing-voice` — Drafts and polishes posts/emails in user voice with lightweight humanizer + critic pass support.

## Software Engineering

Dev process, planning, and methodology skills.

- `deep-monorepo-code-review` — Deep-review a monorepo after a major refactor by validating branches, splitting review lanes, and synthesizing a triage list.
- `local-app-screenshots-and-gif` — Capture screenshots and generate a tour GIF from a locally running web app for README or social posts.
- `product-planning-doc-pack` — Creates a tight planning pack (PRD, impl plan, UI spec, source map, AGENTS.md) before implementation starts.
- `prompt-first-ai-product` — Build AI products where the prompt IS the product — test-first prompt engineering, iterate before building UI.
- `subagent-driven-development` — Execute implementation plans by dispatching fresh subagents per task with two-stage review.
- `systematic-debugging` — 4-phase root cause investigation for any bug, test failure, or unexpected behavior.
- `writing-plans` — Writes comprehensive implementation plans with bite-sized tasks, exact file paths, and complete code examples.

## CLI Tools

Reference skills for CLI tools — install the tool, then the skill teaches your agent how to use it.

- `companies-house-cli` — UK Companies House data: search companies, directors, filings, PSC, charges, insolvency. [🦞 ClawHub](https://clawhub.ai/shan8851/companies-house-cli) · [🌐 Site](https://ch-cli.xyz)
- `fuel-cli` — UK fuel prices: nearby stations by postcode, ranked by price/distance/freshness.
- `parliament-cli` — UK Parliament data: bills, members, divisions, votes, and written questions. [🦞 ClawHub](https://clawhub.ai/shan8851/parliament-cli) · [🌐 Site](https://www.parliment-cli.xyz)
- `rail-cli` — UK National Rail: live departures, arrivals, station search, destination filtering.
- `tfl-cli` — London transport: tube status, journey planning, live arrivals, disruptions, bike docks. [🦞 ClawHub](https://clawhub.ai/shan8851/tfl-cli) · [🌐 Site](https://tfl-cli.xyz)

## Site

Browse a UI version at [skills.shan8851.com](https://skills.shan8851.com)
