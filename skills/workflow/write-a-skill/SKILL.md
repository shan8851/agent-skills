---
name: write-a-skill
description: Create or refine agent skills with clear triggers, lean structure, and reusable references/scripts. Use when the user asks to create, rewrite, package, or improve a skill for recurring workflows.
---

# Write a Skill

Build practical skills that are easy to trigger and easy to maintain.

## Always start with intent capture
Ask for the minimum context needed before drafting:
- what job this skill should do
- top use cases it must handle
- what "good output" looks like
- constraints (tone, tooling, safety, portability)

If details are missing, ask concise questions first instead of guessing.

## Build flow
1) Define scope and trigger language.
2) Draft `SKILL.md` (frontmatter + core workflow).
3) Move detailed/rarely-needed material into `references/`.
4) Add `scripts/` only when deterministic operations justify it.
5) Review with user and iterate quickly.

## Structure standard
Use this layout by default:
- `SKILL.md` (required)
- `references/` (optional, preferred over giant top-level docs)
- `scripts/` (optional, only when justified)
- `assets/` (optional, only when output artifacts need files)

See `references/skill-structure.md`.

## Quality rules
- Keep `SKILL.md` lean; put depth in references.
- Description must be explicit about triggers (`Use when ...`).
- Prefer concrete steps over generic advice.
- Avoid environment-specific leakage unless explicitly intended.

## Decision helpers
- `references/decision-guides.md` for:
  - when to add scripts
  - when to split files
- `references/review-checklist.md` for optional QA before handoff.

## Handoff pattern
After drafting, ask:
- "Does this cover your real use cases?"
- "What's missing or over-specified?"
- "Should I make this stricter or more flexible?"
