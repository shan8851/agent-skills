---
name: product-planning-doc-pack
description: Turn a software product, feature, tool or app idea into a short set of working planning docs before any code is written - PRD, architecture, surface spec (UX, CLI or API), data sources, a milestone-by-milestone implementation plan built from thin end-to-end slices, risks and agent guidance. Use when the user says "write a PRD", "make a planning pack", "scope this properly", "plan this before we build it", "prepare docs before building", or has a promising but fuzzy idea for a new repo or substantial feature.
---

# Product Planning Doc Pack

Turn a promising but unclear software idea into a compact set of working documents that make it clear what to build first and why.

The job is **planning, not implementation and not launch prep**. A good pack lets someone (or a coding agent) start the first slice tomorrow knowing who it's for, what's in and out of v1, how it fits together, where the data comes from, and what could kill it.

Avoid documentation theatre. If a section doesn't change what gets built, tighten it or delete it.

## When to use

- Starting a new product, tool, library, CLI, API or substantial feature.
- Creating a repo before scaffolding it.
- Turning a messy idea into a PRD plus build plan.
- "Write a PRD", "make a planning pack", "scope this properly", "prepare docs before building".
- There's real uncertainty about product, UX, API, data or architecture.

Do not use when:
- the change is small and obvious;
- a PRD already exists and the user only wants implementation tasks;
- the user only wants brainstorming, or wants the idea challenged (use the `challenge-me` skill if installed);
- the product is finished and the user wants demo or launch material;
- the user explicitly wants code now and accepts the ambiguity.

## Output location

Write files under `planning-docs/`:

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

Optional: `eval-plan.md` for AI or model-heavy products; `research-notes.md` when outside research shaped decisions.

Add `planning-docs/` to `.gitignore` by default, for new and existing repos, unless the user wants the pack committed. It keeps working plans out of the project's real docs. Use `agent-guidance.md` instead of editing a root `AGENTS.md` or `CLAUDE.md`, unless the repo owner asks.

## Process

1. **Ground the context.** In an existing repo, read the README, manifests, existing docs, relevant tests, routes, schemas, commands or UI, and any `AGENTS.md`/`CLAUDE.md`. For a new project, look at linked docs, similar tools or competitors. If something can be inspected, inspect it. If not, ask one or two high-value questions, not a questionnaire.

2. **Pressure-test the idea lightly.** Who is the user? What painful job are they doing? What's the smallest useful v1? What's explicitly out? What assumption could kill it? If the idea is still mushy, suggest the `challenge-me` skill (if installed) before writing polished docs.

3. **Pick the surface type.**
   - **UX:** web, mobile, dashboard or visual app. Specify screens, flows, components and states, plus high-level design direction and anti-patterns.
   - **CLI:** commands, flags, JSON output, errors, exit codes.
   - **API or library:** public interfaces, examples, errors, compatibility.
   - **Hybrid:** only the surfaces that matter for v1.

   Don't force UX docs onto a CLI or library. Don't skip UX for a visual or operator-facing product.

4. **Write the docs** using `references/file-requirements.md` for what each file needs. Write decisions and assumptions, not essays: bullets, tables, examples and explicit non-goals.

5. **Plan vertical slices.** Plan the build as tracer bullets: thin slices that prove value end to end. Avoid horizontal milestones like "build backend", "build frontend", "write tests". The first slice should prove the architecture and the core value.

6. **Leave the plan maintainable.** `implementation-plan.md` is a working document with a status block and notes, so whoever builds it can update it as reality changes. To execute it, the user's agent can work milestone by milestone: build one slice, run its verification, update the status and notes, then move on.

7. **Run the final checklist** below, then reply in the output format.

## Quality rules

**Choose a sharp wedge.**

Weak: "A platform for everything." "A dashboard for all data." "A generic AI assistant for X."

Sharper:
- "A CLI that gives on-call engineers JSON access to incident timelines."
- "A booking app that lets members of a small gym reserve classes from their phone."
- "A local-first log viewer for scheduled jobs on one machine."

**Prefer vertical slices.** A good slice proves one narrow user or developer flow, uses real data or clearly labelled fixtures, goes through the public interface, can be tested by behaviour, and can be demonstrated when done.

**Be honest about mocks.** Mocks and prototypes are fine; pretending they're real isn't. Label behaviour as real, mocked, simulated, fixture-backed, dry-run or future integration.

**Treat code quality as scope.** Encourage small composable modules, obvious names, data readers and adapters kept separate from UI, typed contracts where the language supports them, behaviour-focused tests, and deep modules that hide complexity behind a simple interface. No giant files, and no speculative plugin systems unless they're the v1 wedge.

## Output format

After writing the pack, reply with:

```markdown
**Files:** [created or updated, under planning-docs/]
**Thesis:** [one sentence: "X for Y who need Z"]
**Biggest open decision:** [the one that most changes the build, and who decides]
**First slice:** [the first end-to-end slice to build], or the next planning question if it isn't ready
```

## Common failure modes

1. **Starting with the scaffold:** scaffolding before the product shape is clear creates a repo-shaped to-do list.
2. **One giant PRD:** keep requirements, architecture, surface, sources, risks and plan in separate files.
3. **Implementation detail as the pitch:** keep technology choices in `architecture.md`, not the thesis.
4. **Hand-wavy data sources:** name each source and define its contract. "TODO: find data" is not a plan.
5. **Smuggling v2 into v1:** park broad integrations and plugin systems unless they're the wedge.
6. **Weak testing decisions:** "add tests" isn't a plan. Name the behaviours and interfaces to test.
7. **A static plan:** forgetting to give the plan status and notes, so it goes stale after the first milestone.
8. **Questionnaire first:** asking ten questions that reading the repo would have answered.

## Final checklist

- [ ] Files are under `planning-docs/`, gitignored unless the user asked otherwise.
- [ ] The product thesis is one sharp sentence.
- [ ] Target users or actors are specific.
- [ ] v1 scope and non-goals are explicit.
- [ ] The surface type was chosen: UX, CLI, API/library or hybrid.
- [ ] Sources, paths, APIs, environment variables and boundaries are named, with assumptions marked.
- [ ] Architecture covers modules, data flow, persistence and integration boundaries.
- [ ] The implementation plan has a status block, notes, milestones, vertical slices and verification steps.
- [ ] Risks cover product, technical, security/privacy and delivery, with kill or pivot conditions.
- [ ] Mocked, simulated or dry-run behaviour is labelled.

## References

- `references/file-requirements.md`: what each file in the pack must contain, including the implementation-plan template.

With thanks to Matt Pocock's skills for ideas such as tracer bullets and deep modules.
