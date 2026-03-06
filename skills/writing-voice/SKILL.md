---
name: writing-voice
description: Draft, rewrite, and polish posts/emails/announcements in the user's authentic voice. Use when the user asks “write this in my voice”, wants a draft for social/email/blog, asks to humanize output, or says “run the critic on this”.
---

# Writing Voice

Draft in the user's voice, then iterate fast.

## References
- Read `references/voice-dna-framework.md` first.
- Read `references/voice-dna-template.md` and replace placeholders for your user.
- Use `references/humanizer-mini.md` for a lightweight anti-AI cleanup pass.
- Use `references/critic-protocol.md` when user asks to run the critic.

## Modes
- `draft` (default): create a fresh draft in voice.
- `humanize-mini`: clean an existing draft with the lightweight pass.
- `critic`: run iterative self-critique when user says "run the critic on this".

## Workflow (draft mode)
1) Confirm brief quickly if missing essentials:
- format (post/email/thread/note)
- audience
- goal/CTA
- length target

2) Draft v1 in the target voice:
- follow voice DNA rules strictly
- keep claims concrete
- use real writing samples as primary calibration source

3) Run mini humanizer pass (light touch):
- convert list-heavy blocks into prose where it reads better
- remove unnecessary emoji
- remove em dashes
- normalize title-case headings when it clashes with voice style

4) Run voice QA before sending:
- banned phrases check
- forbidden formatting check
- tone match check against the user’s own writing samples
- ensure cleanup did not flatten personality

5) Return draft + review prompt:
- ask for targeted edits (tone, structure, examples, length, CTA)
- offer quick v2/v3 iterations

## Critic mode ("run the critic on this")
Run up to 3 rounds max.

Per round:
1) Critic review against voice DNA rules + writing samples + current brief.
2) Assign rating: `Needs Work`, `Good`, or `Excellent`.
3) If `Excellent`, stop.
4) If below `Excellent`, provide specific feedback tied to exact rule/sample mismatch, then revise.

Output for critic mode:
- final revised draft
- short critic log with round ratings + key fixes

## Iteration protocol
When feedback arrives:
- preserve core message
- apply requested deltas only
- keep voice consistency
- return revised draft directly, then ask if they want one more pass

## Output style
- Default: one clean draft, no meta commentary.
- Voice fidelity beats over-cleaning: keep personality, opinions, and natural rhythm.
- If useful, append a short "Options" block with 2-3 alternative hooks or endings.
