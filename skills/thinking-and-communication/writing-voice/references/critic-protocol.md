# Critic Protocol

Use when the user says "run the critic on this".

## Goal

Catch voice drift and weak writing choices before the user sends anything, without sterilising the style.

## Round loop (max 2 rounds)

For each round:
1. Review the draft against:
   - the voice profile, if there is one (otherwise the generic rules in `voice-dna.md`);
   - the anti-filler checklist and banned phrases;
   - formatting rules;
   - register and channel fit;
   - the writing samples;
   - the brief and call to action.
2. Name the weaknesses, quoting the exact lines.
3. Rate it: `Needs work`, `Good` or `Excellent`.
4. If below `Excellent`, fix the named issues and re-check.

Stop when the rating reaches `Excellent` or after 2 rounds, whichever comes first.

**Before rating `Excellent`, name at least one remaining weakness**, however small (a slightly soft ending, a line that could be shorter). If you can't find one, you haven't looked hard enough. `Excellent` means the remaining weaknesses are minor, not that there are none.

## Critic checks

- **Voice match:** does it genuinely sound like the writer's samples?
- **Substance:** does it answer the actual ask, not an adjacent one?
- **Clarity:** specific and concrete, no fluff or repetition?
- **Structure:** does it start fast and keep momentum?
- **Register:** right for the audience and channel, without going corporate?
- **Humaniser residue:** list spam, emoji, title-case headings, preamble or recap.

## Critic rules

- Be specific. Quote exact misses, not vague judgements.
- Point to the profile rule or sample behind each flag.
- Don't polish away personality. Natural imperfections are fine if the voice is strong.
- If a line is sharp, specific and human, protect it.

## Critic log format

```markdown
**Round 1: Good**
- Weak: "[quoted line]" (generic opener; profile says open with the point)
- Fixed: cut the recap paragraph

**Round 2: Excellent**
- Remaining weakness: the last line is a little soft; fine to keep if you like it.
```
