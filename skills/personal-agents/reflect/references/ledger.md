# Follow-up ledger (optional)

A short markdown file that carries a few follow-ups and themes between reflections, so the agent can notice when something gets done, goes quiet or becomes due, without nagging.

It is **working state**, not a record. The user's notes and explicit updates decide what's true. Every commitment in the ledger must also exist in a note. If the ledger is lost, rebuild it from the notes.

## Location

Anywhere outside the main notes, for example `notes/.reflect/ledger.md`. Keep it out of note searches used by `recall`.

## Format

```markdown
# Reflection ledger

Last reflection: 2026-10-11 (window 2026-10-04 to 2026-10-11)

## Open

### Book boiler service
- Kind: commitment
- Status: open — no update since it was noted
- Source: notes/inbox.md (2026-09-28)
- Due: 2026-10-31 (as stated)
- Last raised: 2026-10-04
- Raise again: when due date is within a week, or on new evidence

### Sleep and late screens
- Kind: theme
- Status: noted 3 times in 2 weeks
- Sources: journal/2026-10-02, 2026-10-07, 2026-10-09
- Last raised: never
- Raise again: next reflection, once

## Closed

### Renew passport
- Resolved 2026-10-06: "passport arrived" (journal/2026-10-06)
```

## Kinds and statuses

- **Kind:** `commitment` (the user said they will), `follow-up` (worth checking on), `concern`, `theme`. Ideas don't need an entry unless the user asks to revisit them.
- **Status:** `open` (unresolved in the notes, not proven undone), `in progress` (activity reported), `waiting` (on someone or something named), `resolved`, `dropped` (the user decided to stop).

## Reconciling

- Change status only on evidence in a note or an explicit user update. Reading a note doesn't complete its tasks.
- Match by meaning, not exact title. Don't create a second entry for the same item.
- If unsure whether a note settles an item, leave it and say so.
- Keep the earlier status in a short line when it changes. A resolved item can reopen on new evidence.
- `capture` may add a source line when a capture clearly updates an item ("that's done"). It doesn't run a review.

## Raising items

Raise an open item only when:
- it has a due date that's close or past;
- there's new evidence about it;
- the user agreed a check-in; or
- there's real urgency.

Otherwise leave it, even if unconfirmed. Don't call anything overdue unless there was a stated date. If the user asks "what's still open?", list everything open.

## Suggestions

If you suggested something and the user didn't take it up, record it as a suggestion, not a commitment. It becomes a commitment only when the user says so (and it's saved in their notes).
