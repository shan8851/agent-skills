---
name: weekly-focus-brief
description: Create a user-centric weekly focus brief from workspace dumps and memory, with concrete actions and practical pattern analysis.
---

# Weekly Focus Brief

Use when running a weekly personal execution review for the user.

## Purpose
Turn raw weekly signals into a concise, actionable focus brief for the upcoming week.

## Trigger
- Weekly cadence (recommended via playbook/cron wrapper)
- Or manual run on demand

## Sources
- `workspace/dump/**` (if missing, continue without failing)
- `workspace/memory/**`

## Output contract
Produce one concise brief with these sections:
1. Weekly momentum summary (2–4 lines)
2. Emerging patterns (max 5 bullets; wins, repeated blockers, trend shifts)
3. Top 3 themes
4. Top 1 risk this week
5. Top 1 leverage move
6. This Week's Focus (5 minimum, 10 maximum) ranked by highest impact
7. Content ideas this week (1–3 max): blog posts, threads, or short opinion pieces suggested from actual context in dumps/memory — not generic prompts. Each idea must have a concrete angle and a one-line "why now" tied to what the user has been doing or thinking about that week.

## Quality rules
- Evidence-backed claims only.
- Recurring claims should be based on repeated signals.
- Prefer concrete actions over abstract motivation.
- Actions should be specific and executable.

## Operating mode
- Propose-only.
- Do not auto-edit files.
- Do not auto-create/update/delete crons.
- Do not auto-send messages.

## Tone guidance
- Direct, practical, and slightly opinionated.
- Call out repeat patterns plainly (especially avoidance loops).
- Prefer one concrete change over generic motivation.

## Format
Use `references/report-template.md`.
Apply checks in `references/quality-checks.md`.
