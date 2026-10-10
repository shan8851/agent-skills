---
name: writing-voice
description: Draft, rewrite, humanise and critique posts, emails, announcements and articles so they sound like the user, learning their voice from their own writing samples. Use when the user says "write this in my voice", "make this sound like me", "make this sound less like AI", "humanise this", "tidy this draft" or "run the critic on this", or wants a public or private draft that sounds like them.
---

# Writing Voice

Write like the user actually writes at their best: direct, specific, human, and not AI-polished.

## When to use

- Drafting a post, email, thread, blog post, note or announcement that should sound like the user.
- Rewriting a draft (theirs or an AI's) so it sounds less generic and less like AI.
- Running a critic pass on a draft before they send or publish it themselves.

Do not use when:
- the user wants neutral house style, formal legal wording or a template that shouldn't sound personal;
- they want facts checked or a topic researched (do that first, then draft);
- they want you to post, send or publish. **Draft only; never post, send or publish on the user's behalf.**

## The voice profile

The skill's `references/voice-dna.md` is a blank template, not anyone's real voice. The user's filled-in profile should live **outside** the installed skill, so skill updates don't overwrite it: for example a `voice-profile.md` in their notes or project. In Claude Code, they can reference it from `CLAUDE.md` so it loads automatically.

At the start:
1. **Look for a profile.** If the user has pointed to one, or one is referenced in project instructions, load it. It overrides the generic defaults.
2. **If there's no profile**, check the conversation for samples of the user's own writing. If there are none, ask for 2–3 short samples (posts, emails, anything they wrote and liked). Offer to build a profile from them using `references/voice-dna.md` as the structure, saved wherever they choose.
3. **Meanwhile, don't block.** If they want a draft now, write it using only the generic anti-filler rules and banned phrases, and say so in one line: "No voice profile yet, so this uses generic anti-filler rules only. Send me 2–3 samples and I'll match your voice."

Real samples and the user's own edits always beat abstract rules.

## Modes

- **Draft** (default): a fresh draft in the user's voice.
- **Humanise**: clean an existing draft without flattening it, using `references/humanizer-mini.md`.
- **Critic**: when the user says "run the critic on this", use `references/critic-protocol.md`.

## Process (draft mode)

1. **Get the minimum brief:** format, audience, goal or call to action, rough length, and channel if it changes tone. Ask only for what's missing and matters.
2. **Calibrate:** read the profile (or the samples), especially core rules, anti-filler checklist, banned phrases and samples. Match the register the brief needs.
3. **Write v1:** open with the point, scene or tension quickly; keep claims concrete; trust the reader; prefer prose to bullet spam; don't sand the edges into generic "professional" copy. Don't invent facts, numbers, quotes or experiences the user hasn't given you. Leave a clear placeholder like `[number]` instead.
4. **Humanise lightly** with `references/humanizer-mini.md`.
5. **Voice QA before returning:** banned phrases; false contrasts ("This isn't X. It's Y.") unless the profile allows them; filler; register and channel fit; match to the samples; personality not sterilised.

## Output format

- One clean draft, no long preamble.
- If no profile was used, one line saying so (see above).
- Optionally, a short **Options** block with 2–3 alternative openings or endings.
- One line inviting targeted changes (tone, length, examples, ending).

Critic mode returns the revised draft plus a short critic log: rating per round, the key fixes, and at least one remaining weakness.

## Iteration

When the user gives feedback:
- keep the core message and apply only the requested changes;
- keep anything the user wrote themselves unless they ask for a rewrite;
- prefer tightening and swapping weak lines over full rewrites, unless the frame is wrong;
- treat the user's edits as the highest-signal voice data, and offer to add durable patterns to their profile.

## Common failure modes

- **Pretending to know the voice:** writing "in their voice" with no profile or samples and not saying so.
- **Generic polish:** smoothing a sharp draft into bland corporate copy.
- **Over-humanising:** stripping lists, headings or dashes the user actually uses.
- **Invented specifics:** made-up numbers, anecdotes or quotes to make a draft feel real.
- **Rubber-stamp critic:** rating a draft Excellent without naming anything that could still be better.
- **Rewriting lines the user wrote** when they only asked for a tidy.
- **Posting or sending** instead of returning a draft.

## References

- `references/voice-dna.md`: blank profile template and generic starter rules. Copy it outside the skill to fill in.
- `references/humanizer-mini.md`: the light clean-up pass.
- `references/critic-protocol.md`: the critic loop.
- `references/worked-example.md`: a brief, a draft and a critic note.
