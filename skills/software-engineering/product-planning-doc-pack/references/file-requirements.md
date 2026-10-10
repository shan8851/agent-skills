# Planning pack: file requirements

What each file in `planning-docs/` should contain. Load this while writing the pack. Drop any section that would not change what gets built.

## `planning-docs/prd.md`

Audience: product and engineering alignment.

Include:
- product thesis: "This is X for Y who need Z";
- problem statement from the user's perspective;
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

## `planning-docs/architecture.md`

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

Call out deep module opportunities where complexity should hide behind a simple public interface: parsers, normalisers, policy engines, state machines, adapters, API clients.

## `planning-docs/surface-spec.md`

Audience: whoever implements the user-facing or developer-facing surface.

Infer which sections apply.

### UX section

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

### CLI section

Use for terminal-first tools.

Include:
- commands and subcommands;
- flags/options;
- input/output formats;
- JSON/machine-readable mode if relevant;
- exit codes;
- examples;
- failure messages.

### API/library section

Use for APIs, SDKs, packages, and backend/library-first products.

Include:
- public interface shape;
- core concepts and terminology;
- example calls;
- errors and edge cases;
- versioning/backwards compatibility;
- behaviour-focused test examples.

## `planning-docs/source-map.md`

Audience: data-layer implementer.

Include:
- expected data sources: local files, APIs, CLIs, databases, RPCs, logs, user input, config, browser state, etc.;
- source-of-truth rules;
- environment variable overrides;
- read/write boundaries;
- normalised output contracts;
- scope model: global, per-user, per-workspace, per-project, per-team, per-entity, etc.;
- refresh/caching expectations;
- privacy/sensitive-data handling;
- assumptions needing confirmation.

If a path/API is unknown, write the assumption and how to verify it. Do not leave "TODO: find data" as the whole plan.

## `planning-docs/implementation-plan.md`

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

## Slices

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

## `planning-docs/risks.md`

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

## `planning-docs/agent-guidance.md`

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
- how agents should work through the plan: one milestone at a time, verifying each slice before moving on;
- how agents should update `implementation-plan.md` status and notes.
