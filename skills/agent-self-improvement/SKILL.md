---
name: agent-self-improvement
description: Weekly propose-only review that analyzes dumps, memory, context, skills, and crons to suggest agent workflow improvements.
---

# Agent Self-Improvement (Weekly)

Use when running a weekly improvement pass for agent behavior and workflow quality.

## Purpose
Produce evidence-backed, propose-only recommendations to improve workflows, context alignment, and automation hygiene.

## Trigger
- Weekly cadence (recommended via playbook/cron wrapper)
- Or manual run on demand

## Required sources
- `workspace/memory/**`
- `workspace/dump/**`
- Core context files: `SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md`, `AGENTS.md`, `TOOLS.md`, `HEARTBEAT.md`
- Installed skills (for overlap/gap checks)
- Cron inventory

## Output contract
Return one concise weekly report with these sections:
1. Top recurring friction/failure themes
2. Candidate workflow improvements
3. Candidate cron/automation suggestions
4. Candidate new ideas
5. Context alignment suggestions
6. Kill/merge/tune hygiene suggestions
7. Recommended priority set for next week

## Item quality rules
Every recommendation must include:
- evidence (where it came from)
- why it matters now
- first 30-minute move
- pragmatic score: impact / recurrence / effort / confidence (H/M/L)

## Operating mode
- **Propose-only**
- Do not auto-edit core files
- Do not auto-create/update/delete crons
- Do not auto-send external/internal messages

## Format
Use the exact report structure in `references/report-template.md`.
Apply scoring guidance in `references/scoring.md`.
