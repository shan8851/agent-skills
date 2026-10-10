# Worked example: "what did I decide about…"

Fictional user. Notes in `notes/`. No chat-history tool available.

## Question

> What did I decide about the kitchen worktops?

## What the agent does

1. **In context:** nothing about worktops.
2. **Agent memory:** `MEMORY.md` has no mention.
3. **Notes:** `rg -n -i "worktop|counter|quartz|oak" notes/` finds:
   - `notes/projects/kitchen.md`, heading `## 2026-06-14`: "Going with oak worktops. Quartz is nicer but £1,900 more and I'd rather put that towards the boiler."
   - `notes/inbox.md`, heading `## 2026-09-02`: "Fitter says oak near the sink needs oiling every few months. Might switch the sink run to quartz? Need a quote."
4. **Newer entries:** searched again for "quartz", "quote", "fitter" after 2 September. Nothing later.
5. **Chat history:** no tool available. Session logs: not needed, the notes answer it.

## Answer

**Answer:** You decided on oak worktops in June, mainly on cost: quartz was £1,900 more and you preferred to put that towards the boiler. In September you wondered about quartz just for the sink run, but that was an idea pending a quote, not a decision.
**Source:** `notes/projects/kitchen.md` (2026-06-14); `notes/inbox.md` (2026-09-02).
**Confidence:** High for the oak decision (explicit, with reasons). The sink-run idea is unresolved.
**Possibly superseded by:** The 2 September note questions part of it. Nothing newer found, and no record of a quote.

## Why this is good

- The reason comes from the note, not from general opinions about oak.
- The September idea is reported as an idea, not a change of decision.
- It checked for anything after September before answering.
- It says chat history wasn't searchable only where that matters, and here it didn't.
