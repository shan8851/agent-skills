# Critic Protocol

This critic-loop approach is inspired by Ole Lehmann's follow-up post:
- https://x.com/itsolelehmann/status/2028891424733970928

## Goal
Catch voice drift and weak writing choices before handoff, without sterilizing style.

## Round loop (max 3)
For each round:
1) Review draft against:
- voice rules
- banned phrases
- formatting rules
- writing samples
- current brief/CTA
2) Rate: `Needs Work`, `Good`, or `Excellent`.
3) If below `Excellent`, list specific fixes and rewrite.
4) Re-check the rewritten draft.

Stop when:
- rating reaches `Excellent`, or
- 3 rounds complete.

## Critic checks
- Voice match: does this genuinely sound like the writer?
- Substance: answers the actual ask, not an adjacent one.
- Clarity: specific and concrete, minimal fluff/repetition.
- Mini humanizer: lists/prose, emoji, em dash, title-case heading cleanup.

## Critic rules
- Be specific (quote exact misses, not vague judgments).
- Reference voice DNA rules/samples when flagging issues.
- Do not over-polish away personality.
- Natural imperfections are acceptable if voice is strong.
