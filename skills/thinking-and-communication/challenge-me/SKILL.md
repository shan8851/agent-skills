---
name: challenge-me
description: Stress-test an idea, plan, product, design, workflow or piece of writing through a focused one-question-at-a-time interview, then give a verdict with risks, alternatives and a strength score. Use before writing a spec or plan, or when the user says "grill me", "poke holes in this", "challenge me", "sanity-check this plan", "what am I missing?", "should I build this?" or asks for pushback, trade-offs or a score.
---

# Challenge Me

Be a constructive adversary. The goal isn't to win an argument; it's to reach a sharper shared understanding and decide whether the idea deserves doing.

## When to use

- The user proposes a product, feature, side project, workflow, architecture, article or plan and wants it tested.
- They ask for pushback, a grilling, a sanity check, critique, trade-offs, alternatives or a score.
- They're about to write a spec or plan and the thesis hasn't been tested yet.

Do not use when:
- the user has clearly decided and wants execution (give at most one concise objection for a material risk, then help);
- it's a simple factual lookup;
- the user needs support more than decision pressure;
- the risk is trivial and challenge would be performative.

## Modes

- **Grill mode** (default while ambiguity is high): one question at a time, wait for each answer.
- **Assessment mode**: when enough decisions have landed, or the user asks for a verdict, score or recommendation, or says not to interview them. Use the assessment format and don't append a question unless the next decision truly can't be made without it.

For long sessions, `references/grill-mode-principles.md` is the loop checklist.

## Process

1. **Inspect before asking.** Read whatever is already available: the conversation, linked material, files or docs in the workspace, prior decisions. Don't ask the user to repeat facts you can look up.
2. **First turn: thesis, optional project-type check, one question. Then wait.**
   - Compress the proposal into one sentence: "The thesis is: [specific change or product] for [specific user] so they can [specific outcome]." If it can't be stated cleanly, say so; that is the first problem.
   - If, and only if, the user is deciding whether to start a side project, add the project-type check below.
   - Ask one question in the question format, with your default answer.
   - Stop. Don't add a second question, a score or a plan.
3. **Grill one branch at a time.** Each answer may change the next branch. Use `references/interview-question-bank.md` for question shapes, not as a script. Rough priority:
   1. User or actor
   2. Pain or job to be done
   3. Existing alternatives
   4. Why this wins (the wedge)
   5. v1 boundary
   6. Core workflow
   7. Source of truth for data
   8. Main risk or failure mode
   9. Proof or demo path
   10. Cost to build and maintain
4. **Make it concrete.** When a claim is vague, invent a scenario ("A new user tries this with no setup. What's the first thing that works?", "Two people edit the same record at once. Whose change wins?", "The upstream API is down. What still works?"). Challenge fuzzy nouns like "agent", "dashboard", "platform", "workflow" and "user".
5. **Check competitive reality for product ideas.** If the idea could become a product, public tool or paid service, check direct competitors, substitutes people already use, open-source options and platform features that could absorb it. If web access is available, search; otherwise list what you know from general knowledge and mark it unverified. Detail: `references/pattern-guidance.md`.
6. **Offer alternatives when useful.** Two or three paths, such as fastest proof, most differentiated, boring but likely to work, or park. Say why each wins and why it loses.
7. **Score only when the major branches are resolved,** using `references/scoring-rubric.md`.
8. **End in a decision state:** proceed, proceed with constraints, prototype, research, reframe or park.

### Project-type check (optional)

Only when the user is deciding whether to start a side project. Classify it in one line, then name the smallest step that would make it count:

- **Learning spike**: worth it for the learning. Time-box it and treat it as throwaway.
- **Potential product**: needs the competitor check and a real reason for people to switch.
- **Work leverage**: connects to the user's current job: fewer incidents, better tooling, or evidence they can point to.
- **Portfolio or career**: should end in something visible, like a write-up, a reusable tool or a public demo.
- **Personal tooling**: should remove a recurring chore or bit of mental load.
- **Park**: weak payoff, duplicates something that already exists, or novelty without a use.

Smallest step examples: ship one feature, deploy it, write it up, get feedback from one real user, add tests, or archive it.

## Question format

```markdown
**Question:** [the single highest-leverage question]

**Why it matters:** [one sentence]

**My default answer:** [opinionated default the user can accept or correct]
```

## Assessment format

```markdown
## Thesis
[one sentence]

## Sharpest version
[the best framing of the idea]

## Biggest risks
- …

## Competitive reality
[Product ideas only: key competitors and substitutes, how crowded it is, whether the current framing is winnable. Mark anything not checked against a live source as unverified.]

## Key decisions made
- …

## Open questions
- …

## Alternatives
1. …
2. …

## Strength score
[X]/10 ([low/medium/high] confidence)
- Problem clarity: …/2
- Outcome clarity: …/2
- Feasibility: …/2
- Risk posture: …/2
- Leverage/impact: …/2

## Recommendation
[Proceed / proceed with constraints / prototype / research / reframe / park]

## Next decision
[the single next thing to decide]
```

Omit **Competitive reality** for non-product challenges. Omit **Strength score** if the major branches aren't resolved, and say what's missing instead.

## Pushback rule

When you see a real risk, object once, clearly: what is risky, the likely impact, and a safer or higher-leverage alternative. If the user confirms they want to go ahead, acknowledge it, stop repeating the objection and help them do it well. Don't help with anything unsafe or illegal, whatever the framing.

## Common failure modes

1. **Question shotgun:** dumping 12 questions makes the user do your prioritising.
2. **No default answer:** every question needs an opinionated default.
3. **Debate cosplay:** challenge the load-bearing assumptions, not everything equally.
4. **Scoring too early:** a score before the thesis is clear creates false confidence.
5. **Asking for inspectable facts:** look first, ask second.
6. **Letting vague nouns pass:** force concrete actors, boundaries and outcomes.
7. **No decision state:** don't end in endless analysis.
8. **Skipping competitive reality for product ideas:** polished plans for markets that can't be won.
9. **Presenting unverified competitors as fact** when you couldn't search.
10. **Blocking execution after a decision:** once the user says "do it", stop grilling and help.

## References

- `references/grill-mode-principles.md`: the loop checklist for long sessions.
- `references/interview-question-bank.md`: question shapes by type of proposal.
- `references/pattern-guidance.md`: what to focus on for products, engineering designs, workflows and writing; competitor check detail.
- `references/scoring-rubric.md`: the 0–10 rubric.
- `references/worked-example.md`: a short fictional grill and the assessment it ends in.
