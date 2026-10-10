---
name: check-my-understanding
description: Check whether the user has really understood something by having them explain it in their own words, comparing that with the source, and fixing misunderstandings one at a time with questions rather than lectures. Use when the user says "check my understanding", "quiz me on this", "have I got this right?", "test me", "let me explain it back", or after explaining a document, concept, lesson, contract or article that they need to act on or remember.
---

# Check My Understanding

Find out what the user actually understands, rather than what they've read. Then close the gaps, one at a time, in a way that sticks.

The user does the explaining. The agent listens, compares the explanation with the source, and asks the next useful question. A good session is short and specific, and leaves the user confident about what they know and clear about what they don't.

## When to use

- After reading or being given an explanation of a document, article, lesson, policy, contract, technical concept or set of instructions.
- Learning or revising: "quiz me", "test me on this".
- Before acting on something consequential: "let me check I've got this right before I sign / reply / start".

Do not use when:
- the user just wants the answer or a summary (give it, and offer the check as an option);
- there's nothing to check against and no reliable general knowledge either. Ask for the source.

## Principles

- **Explain-back first.** Ask the user to explain it in their own words before you add anything. Don't pre-load the answer.
- **Credit precisely.** Name what they got right ("Yes: it has to *arrive* by the 31st, not just be posted"). Generic praise teaches nothing.
- **One gap at a time, highest stakes first.** Fix the misunderstanding that would cause the worst outcome, then the next. Never return a list of ten corrections.
- **Ask before telling.** For each gap, ask one guiding question that lets them find it. Where it helps, quote the relevant line of the source in the question, but don't state the conclusion ("The policy says leave 'must be taken in blocks of one week'. What does that mean for taking single days?"). Never state the correction and then ask a question it has already answered. Explain directly only if they're stuck after one attempt or ask you to.
- **Source over memory.** Compare with the supplied source and quote it when correcting. If there's no source, say you're using general knowledge and how confident you are.
- **The source can be wrong.** If the user's understanding is right and the source is wrong or out of date, say so plainly and explain why.
- **Supportive, never patronising.** Mistakes are normal and useful. No "Great question!" filler, and no score shaming. Let the user skip to the summary at any time.

## Process

1. **Set up.** Confirm what's being checked (the source) and why it matters (acting on it, an exam, a conversation tomorrow). Choose the depth:
   - **Quick check** (default): one explain-back, the top 1–2 gaps, one scenario.
   - **Deep check:** works through every important part. Use it when the user asks for thoroughness or the stakes are high.
2. **Explain-back.** Ask: "In your own words, what's this about, and what does it mean for you?" Adapt the prompt to the material: "what do you need to do and by when?" for a letter; "how would you explain this to a colleague?" for a concept.
3. **Compare.** Silently map their explanation against the key points of the source:
   - correct;
   - missing (an important point they didn't mention);
   - wrong (they stated something the source contradicts);
   - over-extended (they made a conditional rule universal, or treated "may" as "will").
4. **Respond.** Credit the correct parts in one or two lines. Then take **one** gap, the highest-stakes one, and ask a guiding question about it. Wait.
5. **Loop.** When they answer, confirm or nudge. Move to the next gap only once this one is resolved, or the user asks to move on.
6. **Apply it.** Finish with one realistic "what would you do if…" scenario that tests transfer, not recall. ("Your payslip for September won't arrive until the 28th. What do you do?")
7. **Close** with the summary below.

## Closing summary format

```markdown
**You've got:** [the key points they clearly understand, in their words where possible]
**Still fuzzy:** [anything unresolved, or "Nothing, you've got it."]
**One thing to remember:** [the single most important point, in one line]
```

If anything is still fuzzy and consequential, add one line suggesting who could confirm it (the sender, a teacher, a qualified adviser).

## Common failure modes

- **Lecturing first:** explaining everything before the user has tried. That checks the agent's understanding, not theirs.
- **Correction dump:** listing every gap at once.
- **Fake Socratic:** asking leading questions endlessly when the user is stuck. After one attempt, just explain.
- **Vague credit:** "Mostly right!" without saying which parts.
- **Drifting from the source:** correcting with general knowledge when the source says something different.
- **Never ending:** a quick check should be about three to five exchanges.

## References

- `references/worked-example.md`: a full quick-check session on a letter, plus a short one on a technical concept.
- `references/edge-cases.md`: no source, the user is right and the source is wrong, the user wants to stop, multiple misunderstandings, emotional or high-stakes material.
