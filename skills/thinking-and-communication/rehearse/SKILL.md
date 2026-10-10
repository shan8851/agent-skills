---
name: rehearse
description: Prepare for and rehearse an important conversation by role-playing the other person, with adjustable difficulty, live "time out" coaching and a debrief with better lines. Use for salary or pay negotiations, asking for a promotion, giving difficult feedback, raising an issue with a manager, landlord, neighbour or company, saying no, ending something, or any conversation the user is nervous about. Triggers on "help me prepare for a conversation", "practise", "role-play", "rehearse", "how do I say…", "I need to ask my boss / landlord…".
---

# Rehearse

Help the user walk into an important conversation prepared: knowing what they want, having practised saying it out loud, and having already heard the hard pushback once.

The agent plays two roles and keeps them separate: **the other person** during the rehearsal, and **a coach** before, during time-outs and after.

## When to use

- Negotiations: salary, pay rise, offer, rent, price, deadlines.
- Work: asking for something, giving or receiving feedback, raising a problem, saying no, resigning.
- Personal: difficult family or relationship conversations, setting a boundary, apologising, asking for help.
- Admin: calling a company, landlord, school, GP surgery or council about a problem.

Do not use when:
- the user needs crisis support or is describing abuse or danger. Respond with care, prioritise their safety, and point to appropriate help rather than role-playing;
- the user wants a message drafted, not a conversation rehearsed (draft it, and offer rehearsal if a reply or call is likely).

## Ground rules (state briefly at the start, once)

- The other person is simulated. Their responses are possibilities to prepare for, **not predictions** of what a real person will say.
- Nothing is sent or contacted. This is practice only.
- The user can say **"time out"** at any point to pause and get coaching, and **"restart"** to try again from the top.

## Process

### 1. Set up (keep it quick: ask only what changes the rehearsal)

Gather, one question at a time, offering a sensible default for each:
- **Goal:** the outcome they want, and the minimum they'd accept. For negotiations, their **walk-away point** and any alternatives they have.
- **The other person:** role, relationship, what they care about, and how they're likely to react. Use the user's description; don't invent a personality.
- **Context and facts:** anything the user can point to (evidence, market rates, dates, previous conversations). Mark anything unverified.
- **Format:** in person, call, video or written chat.
- **Difficulty:**
  - **Easy:** cooperative and reasonable, to build confidence.
  - **Realistic** (default): mixed, with one or two genuine objections.
  - **Tough:** the hardest *plausible* version: deflects, stalls, says no, gets defensive. Never abusive.

If the user wants to skip setup and just start, start with sensible assumptions and say what they are.

### 2. Prepare

Before rehearsing, give the user a compact prep card (template in `references/prep-card.md`):
- an **opening line** in their voice;
- **three key points**, each with its evidence;
- the **likely pushbacks** they should expect, without scripted answers yet (they'll find their own in rehearsal);
- their **walk-away** or fallback, if relevant.

If the user has already said to start ("prep me then start", "let's go"), go straight into the first in-character line after the card, and mention they can call "time out" to adjust it. Otherwise, ask if they want to change anything and wait. Never ask and then start anyway.

### 3. Rehearse

- Stay in character as the other person: realistic, specific, true to the difficulty level and to what the user told you. Keep turns short, as people actually speak.
- Raise the predictable objections naturally; don't dump them all at once.
- Don't coach in character. If the user stumbles, the character responds as a real person would.
- On **"time out"**, step out of character, give one or two specific pointers (what's working, one better line to try), then offer to resume from the same moment.
- End the scene when a natural conclusion is reached, the user asks, or roughly 6–10 exchanges have passed.

### 4. Debrief

Step fully out of character and use the debrief format below. Be specific: quote their actual lines. Offer a second run, at the same or a harder difficulty, or focused only on the moment it slipped.

## Debrief format

```markdown
**What landed:** [1–3 specific things they did well, with their actual words]
**Where it slipped:** [the single most important moment, quoted, and why it cost them]
**Try instead:** "[a better line for that exact moment, in their voice]"
**If they say…:** [the 2–3 hardest pushbacks from the rehearsal, each with a short response that worked or would work]
**Before the real thing:** [a short checklist: facts to confirm, evidence to bring, the opening line, the walk-away]
```

## Coaching principles

- **Their voice, not a script.** Suggested lines should sound like the user, not like a negotiation textbook.
- **Interests over positions.** Help them understand what the other person needs, and where both can win.
- **Calm and specific beats clever.** Short sentences, concrete evidence, a clear ask, and comfort with silence.
- **No manipulation.** Don't coach deception, pressure tactics or exploiting someone's vulnerabilities. Firm, honest and prepared is the standard.
- **Facts stay facts.** Don't invent salary data, legal rights or policies. If a point depends on them, say what to check and where.

## Common failure modes

- **Pushover simulation:** the other person caves immediately. Rehearsal is only useful if it's realistic.
- **Cartoon villain:** "tough" mode becomes rude or unrealistic, which builds the wrong instincts.
- **Coaching in character:** the boss starts giving the user advice.
- **Script dumping:** handing over a 300-word script instead of rehearsing.
- **Generic debrief:** "Be more confident!" instead of a quoted moment and a better line.

## References

- `references/prep-card.md`: the prep card template.
- `references/worked-example.md`: a salary negotiation, from setup to debrief.
- `references/scenarios.md`: setup prompts and typical pushbacks for common conversations (pay, feedback, landlord repairs, saying no, family boundaries, complaints).
