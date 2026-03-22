---
name: memory-curation
description: Curate and promote memory with signal-first judgment. Use when running memory checkpoints, consolidating daily notes, deciding what to store in durable memory, or when the user says “remember this”. Apply a strict rubric so only stable decisions/preferences/policies are promoted to long-term memory.
category: workflow
---

# Memory Curation

Signal-first memory workflow.

## Core rule
Do not treat all context as memory. Prefer quality over volume.

## Workflow
1) Collect candidate facts from recent conversation/work.
2) Score each candidate using `references/promotion-rubric.md`.
3) Route each candidate:
- Durable + behavior-changing → `MEMORY.md`
- Session/day context → daily memory file
- Low-signal/noise → skip
4) Write concise bullets using `references/write-templates.md`.
5) De-duplicate against recent entries before writing.

## Hard guardrails
- Never store secrets, API keys, or sensitive credentials.
- Avoid personal/private details unless explicitly required by the user.
- Prefer one precise bullet over multiple vague bullets.
- If uncertain, keep in daily memory first; promote later if it recurs.

## Promotion defaults
Promote when at least one is true:
- explicit remember intent
- standing policy/guardrail
- stable preference (likely 30+ days)
- canonical tooling/path/routing correction
- recurring operating rule

## Completion behavior
When running silent checkpoint workflows, end with exactly `NO_REPLY`.
