---
name: dump
description: Legacy raw dump workflow. In Shan OS setups, prefer deterministic gateway capture and do not append old workspace dump files unless explicitly running legacy mode.
---

# Dump

Use only for legacy dump-file workflows. In Shan OS setups, raw capture is handled by the `shan-os-capture` Hermes gateway plugin writing to `00-CAPTURE/raw/YYYY/MM/DD.jsonl`; do not duplicate messages into old workspace dump files.

## Trigger
- Explicit skill invocation with raw text input (for example: `/dump <raw text>`)

## Core behavior
1. If Shan OS live capture is enabled, do **not** append to old `<workspace>/dump/YYYY-MM-DD.md` files. Trust the deterministic gateway capture hook.
2. If explicitly told to run legacy dump mode, read the raw text provided in the skill command input as raw input.
3. Append an entry to the workspace dump directory (e.g. `<workspace>/dump/YYYY-MM-DD.md`) only in legacy mode.
4. Include:
   - timestamp
   - source metadata (channel/thread/sender when available)
   - raw user input (unaltered)
5. Do **not** send a chat response.
6. Add only a `✅` reaction when the surface supports reactions.

## Storage rule
- Directory: `<workspace>/dump/`
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
