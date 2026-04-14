---
name: writing-voice
description: Draft, rewrite, humanize, and critique posts/emails/announcements in the user's authentic voice. Use when the user asks "write this in my voice", wants a public or private draft that sounds like them, wants to humanize AI-ish copy, or says "run the critic on this".
---

# Writing Voice

Write like the user actually writes at their best: direct, specific, human, and never AI-polished.

## References
Always load:
- `references/voice-dna.md`
- `references/humanizer-mini.md`
- `references/critic-protocol.md`

If there is a conflict, real writing samples and live feedback win over abstract rules.

## Modes
- `draft` (default): create a fresh draft in the user's voice.
- `humanize-mini`: clean an existing draft without flattening it.
- `critic`: run the critic loop when the user says "run the critic on this".

## Workflow (draft mode)
1) Capture the minimum brief
- format (post/email/blog/thread/note/announcement)
- audience or register
- goal / CTA
- length target
- channel, if it materially affects tone or structure

If essentials are missing, ask only for the missing pieces.

2) Calibrate before writing
- read the voice DNA, especially core rules, anti-filler checklist, banned phrases, and writing samples
- follow the user's current style unless the brief clearly calls for a different register
- preserve honesty, specificity, and natural rhythm

3) Draft v1
- open with the point, scene, or tension quickly
- keep claims concrete
- trust the reader
- prefer strong prose over list spam
- do not smooth the edges into generic “professional” writing

4) Run mini humanizer pass
- use `references/humanizer-mini.md`
- keep this pass light

5) Run voice QA before sending
- banned phrases check
- false-contrast / "This isn't X. It's Y." check
- anti-filler check
- register/channel fit check
- sample match check
- ensure edits didn't sterilize personality

6) Return clean output
- default: one clean draft, no long meta commentary
- treat the first answer as v1, not sacred final copy
- if useful, append a short `Options` block with 2-3 alternative hooks or endings
- invite targeted iteration on tone, structure, examples, length, or CTA

## Critic mode
When the user says "run the critic on this", use `references/critic-protocol.md`.

Return:
- revised draft
- short critic log with round ratings and the key fixes

## Iteration protocol
Use iteration as the main calibration loop.

When feedback arrives:
- preserve the core message
- apply requested deltas only
- keep voice consistency
- keep anything the user wrote themselves unless they ask for a rewrite
- if a line is already distinctly theirs, leave it alone
- prefer tightening, trimming, and swapping weak lines over full rewrites unless the frame is wrong
- treat the user's edits as the highest-signal voice data

## Output style
- Default: one clean draft.
- Voice fidelity beats polish.
- Natural imperfections are fine if the piece sounds like the user.
- Do not explain the point, joke, or lesson twice.
