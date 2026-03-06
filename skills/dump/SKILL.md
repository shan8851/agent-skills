---
name: dump
description: Capture raw user dumps passed to the skill invocation into workspace-local markdown logs with no chat response.
---

# Dump

Use when a user wants quick, low-friction raw capture of thoughts/notes.

## Trigger
- Explicit skill invocation with raw text input (for example: `/dump <raw text>`)

## Core behavior
1. Read the raw text provided in the skill command input as raw input.
2. Append an entry to `/home/shan/.openclaw/workspace/dump/YYYY-MM-DD.md`.
3. Include:
   - timestamp
   - source metadata (channel/thread/sender when available)
   - raw user input (unaltered)
4. Do **not** send a chat response.
5. Add only a `✅` reaction when the surface supports reactions.

## Storage rule
- Directory: `/home/shan/.openclaw/workspace/dump/`
- File per day: `YYYY-MM-DD.md`
- Append-only.
- Use absolute paths only (never `~`).

## Guardrails
- No summarising or rewriting during capture.
- No analysis during capture.
- No auto-promotion to long-term memory.
- No auto-creation of tasks/crons/messages.

## Entry template
Use the exact template in `references/entry-template.md`.

## Workflow note
Channel-specific workflows may map `dump:`-prefixed messages (or dedicated dump channels) to this skill, but that routing behavior lives outside this skill.
