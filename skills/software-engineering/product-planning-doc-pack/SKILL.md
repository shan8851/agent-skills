---
name: product-planning-doc-pack
description: Create a focused planning pack for a new software product, feature, tool, or app before implementation. Produces planning-docs with PRD, architecture, surface spec, source map, implementation plan, risks, and agent guidance. Use when product clarity is needed before code.
---

# Product Planning Doc Pack

Use this when a software product, feature, tool, or app idea is promising but not clear enough to build. The goal is **planning**, not launch/demo prep and not implementation.

The output should be a compact set of working planning documents that clarify product value, scope, architecture, user/API/CLI surface, data sources, risks, and implementation slices.

Avoid documentation theatre. If a section does not change what gets built, tighten it or delete it.

## When this skill fits

Use when:
- starting a new software product or substantial feature;
- creating a repo before scaffolding;
- turning a messy idea into a PRD plus build plan;
- planning a public OSS project, internal tool, devtool, dashboard, AI workflow, local-first app, CLI, API, or library;
- the user says “write a PRD”, “make a planning pack”, “scope this properly”, or “prepare docs before building”;
- product/UX/API/data/architecture uncertainty exists.

Do not use when:
- the change is tiny and obvious;
- a PRD already exists and the user only wants implementation tasks;
- the user only wants brainstorming or challenge;
- the user wants demo/launch material for an already-finished product — use a dedicated demo/launch skill instead;
- the user explicitly wants code now and accepts the ambiguity.

## Output location

Create planning files under `planning-docs/`.

For existing repos, add `planning-docs/` to `.gitignore` by default unless the user explicitly wants the planning pack committed. This avoids clashing with normal project docs and keeps working plans private by default.

For brand-new repos where the planning pack is the initial artifact, use `planning-docs/` and add it to `.gitignore` unless the user explicitly wants to commit or publish it.

Default structure:

```text
planning-docs/
  prd.md
  architecture.md
  surface-spec.md
  source-map.md
  implementation-plan.md
  risks.md
  agent-guidance.md
```

Optional files:
- `planning-docs/eval-plan.md` for AI/prompt/model-heavy products.
- `planning-docs/research-notes.md` when meaningful external research informed decisions.

## Workflow

### 1. Ground the context

For existing repos, inspect what is already there:
- README and package manifests;
- existing docs and design notes;
- current tests, routes, schemas, commands, modules, or UI surfaces relevant to the idea;
- repo guidance such as `AGENTS.md` or `CLAUDE.md` if present.

For new projects, inspect examples, competitors from web search, related tools, or linked docs if available.

If missing context is inspectable, inspect it. If it is not, ask one or two high-leverage questions rather than a giant questionnaire.

### 2. Validate the thesis lightly

Before producing polished docs, pressure-test:
- Who is the user or actor?
- What painful job are they trying to do?
- What is the smallest useful v1?
- What is explicitly out of scope?
- What assumption could kill the project?

If the idea is still mushy, use a challenge/grill skill first.

### 3. Infer the surface type

Pick the right product surface from the project:

- **UX surface** — web/mobile/dashboard/visual app → specify screens, flows, components, states. Include design direction for new products at least at a high level, plus anti-patterns to avoid.
- **CLI surface** — terminal-first tool → specify commands, flags, JSON output, errors, exit codes.
- **API/library surface** — SDK/backend/package → specify public interfaces, examples, errors, compatibility.
- **Hybrid surface** — combine only the surfaces that matter for v1.

Do not force UX docs onto a CLI/library project. Do not ignore UX for visual/operator products.

### 4. Write concise working docs

Docs should be decisions and assumptions, not essays. Prefer bullets, tables, examples, and explicit non-goals.

### 5. Plan vertical slices

Implementation should be planned as tracer bullets: thin slices that prove value end-to-end. Avoid horizontal milestones like “build backend”, “build frontend”, “write tests”.

### 6. Leave the plan maintainable

The implementation plan is a working document. Include status and notes fields so agents can update it as reality changes.

## File requirements

### `planning-docs/prd.md`

Audience: product and engineering alignment.

Include:
- product thesis: “This is X for Y who need Z”;
- problem statement from the user’s perspective;
- target users / actors;
- goals and success criteria;
- v1 scope;
- explicit non-goals;
- user journeys or workflows;
- user stories where useful;
- functional requirements;
- non-functional requirements: privacy, performance, reliability, accessibility, cost, platform constraints;
- terminology/glossary if new terms appear;
- assumptions and open questions.

Keep implementation details out unless they are product-shaping decisions.

### `planning-docs/architecture.md`

Audience: implementers and reviewers.

Include:
- system overview;
- runtime model: local, hosted, hybrid, CLI-driven, API-driven, offline-first, etc.;
- major modules and responsibilities;
- data flow, preferably with Mermaid or a compact text diagram;
- persistence model;
- integration boundaries and external dependencies;
- security and privacy assumptions;
- failure modes and recovery behaviour;
- testing strategy at a high level.

Call out deep module opportunities where complexity should hide behind a simple public interface: parsers, normalizers, policy engines, state machines, adapters, API clients.

### `planning-docs/surface-spec.md`

Audience: whoever implements the user-facing or developer-facing surface.

Infer which sections apply.

#### UX section

Use for apps, dashboards, mobile products, websites, and visual tools.

Include:
- global shell/navigation;
- page-by-page or screen-by-screen structure;
- primary user flows;
- interaction states;
- empty, loading, error, offline, and permission-denied states;
- suggested component names;
- shared data contracts per page;
- copy/content requirements;
- accessibility notes;
- design direction and anti-patterns.

#### CLI section

Use for terminal-first tools.

Include:
- commands and subcommands;
- flags/options;
- input/output formats;
- JSON/machine-readable mode if relevant;
- exit codes;
- examples;
- failure messages.

#### API/library section

Use for APIs, SDKs, packages, and backend/library-first products.

Include:
- public interface shape;
- core concepts and terminology;
- example calls;
- errors and edge cases;
- versioning/backwards compatibility;
- behaviour-focused test examples.

### `planning-docs/source-map.md`

Audience: data-layer implementer.

Include:
- expected data sources: local files, APIs, CLIs, databases, RPCs, logs, user input, config, browser state, etc.;
- source-of-truth rules;
- environment variable overrides;
- read/write boundaries;
- normalized output contracts;
- scope model: global, per-user, per-workspace, per-project, per-wallet, per-chain, per-entity, etc.;
- refresh/caching expectations;
- privacy/sensitive-data handling;
- assumptions needing confirmation.

If a path/API is unknown, write the assumption and how to verify it. Do not leave “TODO: find data” as the whole plan.

### `planning-docs/implementation-plan.md`

Audience: implementer or coding agent.

This is a **working document**, not a static plan. It should be safe for agents to update as milestones complete or assumptions change.

Start with:

```markdown
# Implementation Plan

## Current status

- Overall status: Not started / In progress / Blocked / Complete
- Last updated: YYYY-MM-DD
- Current milestone: Milestone N — name
- Current blocker: None / description
- Next action: one concrete next step

## Change log / notes

- YYYY-MM-DD — Initial plan created.
```

Then include milestones in dependency order. Each milestone should have:

```markdown
## Milestone N — Name

Status: Not started / In progress / Blocked / Complete
Goal: one sentence
Notes: working notes, discoveries, changed assumptions
Verification: command, manual check, or acceptance signal

### Slices

- [ ] Slice 1 — end-to-end behaviour or capability
- [ ] Slice 2 — end-to-end behaviour or capability
```

Rules:
- Use vertical slices, not horizontal layers.
- First slice should prove the architecture and core value.
- Include likely files/areas only when known.
- Include test strategy per milestone.
- Include verification commands where known.
- Keep deferred work parked clearly.

Default milestone shape:
1. Repo/bootstrap/hygiene.
2. Domain/source discovery.
3. First end-to-end tracer bullet.
4. Core workflow expansion.
5. Surface hardening.
6. Tests, docs, observability, release readiness.
7. Deferred extras.

### `planning-docs/risks.md`

Audience: decision-maker and implementer.

Include:
- product risks;
- technical risks;
- UX/API/CLI risks;
- security/privacy risks;
- delivery risks;
- scope creep traps;
- mitigations;
- kill/pivot conditions;
- assumptions to validate first.

### `planning-docs/agent-guidance.md`

Audience: future AI agents and contributors.

Use this instead of editing root `AGENTS.md` by default. The planning pack is usually private/working; root `AGENTS.md` should only change when the repo owner wants persistent repo-wide instructions.

Include:
- what the product is;
- current priority;
- non-goals;
- planning-docs structure;
- domain language / glossary pointer;
- testing expectations;
- UX/API/CLI expectations;
- security/privacy rules;
- local verification commands;
- how agents should update `implementation-plan.md` status and notes.

## Quality rules

### Choose a sharp wedge

Bad:
- “A platform for everything.”
- “A dashboard for all data.”
- “A generic AI assistant for X.”

Better:
- “A policy firewall for autonomous agents spending programmable money.”
- “A local-first observability console for scheduled agent work.”
- “A CLI that gives agents reliable, JSON-shaped access to UK rail disruption data.”

### Prefer vertical slices

A good implementation slice:
- proves one narrow user/developer flow;
- uses real data or clearly-labelled fixtures;
- exercises the public interface;
- is behaviour-testable;
- is demoable/verifiable when complete.

### Be honest about mocks and prototypes

Mocks and prototypes are fine. Lying about them is not. Label behaviour as real, mocked, simulated, fixture-backed, dry-run, or future integration.

### Treat code quality as product scope

Planning docs should encourage:
- small composable modules;
- obvious names;
- domain readers/adapters separate from UI;
- typed contracts where the language supports it;
- behaviour-focused tests;
- no giant sludge files;
- no speculative plugin systems unless core to v1.

## Common failure modes

1. **Starting with the scaffold** — scaffolding before product shape is clear creates a repo-shaped todo list.
2. **Writing one giant PRD** — separate product requirements, architecture, surface shape, sources, risks, and implementation.
3. **Letting implementation detail become the pitch** — use implementation details in architecture, not positioning.
4. **Leaving data sources hand-wavy** — name sources and define contracts.
5. **Smuggling v2 into v1** — park broad integrations and plugin systems unless they are the wedge.
6. **Weak testing decisions** — “add tests” is not a plan; name behaviours and interfaces.
7. **Forgetting the plan is live** — update status/notes as milestones complete or assumptions change.

## Final review checklist

Before calling the pack done, verify:

- [ ] Files are under `planning-docs/`.
- [ ] Existing repo has `planning-docs/` gitignored unless user requested otherwise.
- [ ] Product thesis is one sentence and sharp.
- [ ] Target users/actors are specific.
- [ ] v1 scope and non-goals are explicit.
- [ ] Surface type was inferred: UX, CLI, API/library, or hybrid.
- [ ] Sources, paths, APIs, env vars, and boundaries are named.
- [ ] Architecture includes modules, data flow, persistence, and integration boundaries.
- [ ] Implementation plan has current status, notes, milestones, slices, and verification.
- [ ] Risks include product, technical, security/privacy, and delivery risks.
- [ ] Mocked/simulated/dry-run behaviour is clearly labelled where relevant.

## Closing move

After generating the pack, respond with:

1. Files created or updated.
2. The strongest product thesis.
3. The biggest unresolved decision.
4. The first implementation slice or next planning question.
