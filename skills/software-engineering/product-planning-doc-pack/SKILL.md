---
name: product-planning-doc-pack
description: Create a tight planning pack for a new software product before implementation — PRD, implementation plan, UI spec, source map, and repo-local AGENTS.md.
---

# Product Planning Doc Pack

Use this when a user has a promising product direction but implementation has not started yet, especially for public OSS apps where clarity, scope control, and codebase shape matter.

## When this skill fits

Use it when you need to turn a messy idea into an execution-ready planning bundle, not just a loose brainstorm.

Good fit:
- new app/product repo before scaffolding
- public open-source product with a real quality bar
- local-first/devtools/operator products where data sources and UX need clarifying
- user wants planning to be granular before coding

Not a fit:
- tiny one-file utilities
- already-implemented repos that just need a task list
- pure implementation plans with no product/UX uncertainty

## Output pack

Create these files early:

1. `README.md`
   - one-paragraph product summary
   - product shape / scope bullets
   - planned v1 surfaces
   - links to docs

2. `docs/prd.md`
   Include:
   - goal
   - architecture summary
   - target user
   - product principles
   - positioning
   - v1 scope
   - explicit non-goals
   - UI/design direction
   - data sourcing strategy
   - technical architecture
   - success criteria
   - engineering quality bar

3. `docs/implementation-plan.md`
   Break delivery into small milestones with tiny slices.
   Include:
   - bootstrap
   - discovery/data layer
   - major user-facing surfaces
   - polish/productisation
   - deferred milestones
   - testing expectations

4. `docs/ui-spec.md`
   Define page-by-page structure.
   Include:
   - global shell
   - nav
   - filter model
   - page sections
   - suggested component names
   - empty/error-state behaviour
   - shared data contracts
   - styling rules

5. `docs/source-map.md`
   Make source assumptions explicit.
   Include:
   - likely source paths
   - env overrides
   - reader boundaries
   - output contracts
   - scope model (global vs per-entity vs workspace)
   - what still needs confirmation

6. `AGENTS.md`
   Add repo-specific working rules for future agents/contributors.
   Include:
   - what the product is
   - priorities
   - non-goals
   - structure expectations
   - testing expectations
   - UX expectations

## Practical workflow

### 1. Ground yourself in the user's real pattern
Inspect any existing repos, dashboards, READMEs, or product surfaces they already built.
Look for:
- what they naturally optimize for
- what they already found painful
- where their taste actually is
- what should be preserved vs dropped

### 2. Choose a sharp wedge
Do not let the product become "generic platform for everything."
Force a clear thesis.
Examples:
- visibility-first, not chat-first
- read-mostly, not orchestration-first
- native-first, not framework-agnostic

### 3. Lock the defaults
Make explicit choices on:
- target user
- branding direction
- v1/non-v1 boundary
- local-first vs hosted
- native integration vs abstraction layer

### 4. Plan for real paths and env vars early
If the product reads local state, name the expected source roots now.
Document env overrides in the PRD/source map instead of leaving them fuzzy.
This prevents ugly retrofits later.

### 5. Design multi-scope behaviour deliberately
If data may be global vs per-user vs per-workspace, define that upfront.
Do not wait until implementation to invent filtering semantics.

### 6. Treat code quality as product scope
For public OSS projects, the planning docs should explicitly require:
- small composable components
- obvious names
- domain readers separate from UI
- unit tests for parsing/normalization/helpers
- no giant sludge files

## Recommended milestone shape

A good default order:
1. bootstrap shell + repo hygiene
2. setup/discovery/inventory
3. highest-signal read surface
4. supporting read surfaces
5. most complex operational surface
6. polish/productisation
7. deferred extras

For local/operator tools, prefer this order:
- inventory/setup first
- then data/import layer
- then sessions
- then scheduled tasks
- then optional usage/cost

## Naming guidance

In docs, suggest boring, intent-revealing component and reader names.
Push against vague names like:
- `DashboardThing`
- `MegaCard`
- `utils`

Prefer:
- `CronJobsTable`
- `ScheduledTasksTable`
- `ActivityFeedCard`
- `readSessionSummaries`
- `normalizeApiResponses`

## Quality checks before finishing

Before calling the planning pack done, verify:
- v1 scope is narrow and explicit
- non-goals are written down
- env vars and source roots are named
- multi-tenant / multi-scope behaviour is defined if relevant
- UI pages have sections and component names
- tests are mentioned in the plan, not left implicit
- repo-local `AGENTS.md` exists

## Common failure modes

### 1. Jumping straight to scaffold
Bad when source paths, data boundaries, and page structure are still vague.

### 2. Writing only one giant PRD
A PRD alone is not enough. Split product, UI, source assumptions, and milestone plan.

### 3. Leaving data sources hand-wavy
If the app depends on local files/state, document expected paths and env overrides early.

### 4. Letting "extensibility" bloat v1
Do not start with plugin-system brain. Ship the sharp native product first.

### 5. Forgetting contributor guidance
Public OSS repos need a repo-local `AGENTS.md` or equivalent guidance so future work stays aligned.

## Handy closing move

After generating the doc pack, recommend the next step in this order:
1. review/tighten docs
2. confirm actual source paths
3. convert milestone 0 into tiny executable tasks
4. only then scaffold the repo
