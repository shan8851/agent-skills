# Worked Example

A fictional, shortened session. The user is a developer thinking about a side project.

## User

> I want to build a tool that watches my team's pull requests and posts a weekly digest to chat. Should I build this?

## Turn 1 (thesis, project-type check, one question)

> **The thesis is:** a weekly pull request digest for a small engineering team so they can see what shipped without reading every PR.
>
> **Project type:** this sits between *work leverage* (it's for your current team) and *potential product*. I'd treat it as work leverage first. The smallest step that would make it count is a digest your team actually reads for three weeks.
>
> **Question:** Who reads the digest, and what do they do differently after reading it?
>
> **Why it matters:** if nobody changes what they do, it's a notification nobody opens.
>
> **My default answer:** your manager and two teammates in other time zones, who use it to spot work they should review or know about.

*(Stops here and waits.)*

## Turn 2

User: "Mostly the manager. They currently ask in stand-up what everyone did."

> Good, that's a concrete job: replace the "what did you do this week?" round in stand-up.
>
> **Question:** What does your code host or chat tool already offer for this?
>
> **Why it matters:** most code hosts and chat integrations already send PR notifications or summaries. If one covers 80% of this, you're building the last 20%.
>
> **My default answer:** the built-in notifications are per-PR and noisy; nothing groups by person or theme. (Unverified: I can't search from here. Check your code host's scheduled reminders and any chat integrations first.)

## Turn 3

User: "We tried the built-in one. Everyone muted it."

> Then the gap isn't data, it's summarising: group by theme, not by PR.
>
> **Question:** Is a plain grouped list enough for v1, or do you need written summaries of each PR?
>
> **Why it matters:** written summaries add a model call, cost and a chance of getting things wrong; a grouped list is a weekend.
>
> **My default answer:** grouped list first; add summaries only if the manager still asks questions in stand-up.

User: "Grouped list. Give me the verdict."

## Assessment

```markdown
## Thesis
A weekly grouped digest of merged PRs that replaces the "what did you do?" round in stand-up.

## Sharpest version
A once-a-week answer to one manager question, grouped by theme.

## Biggest risks
- It becomes another muted notification.
- Grouping by theme is harder than it looks if PR titles are poor.

## Competitive reality
Built-in code host notifications exist and were muted; chat integrations probably exist (unverified). As a product it's crowded. As team tooling it's fine.

## Key decisions made
- Reader is the manager.
- v1 is a grouped list, no written summaries.

## Open questions
- How will PRs be grouped: labels, folders or title prefixes?

## Alternatives
1. Grouped list from labels (fastest, depends on labelling discipline).
2. Written summaries per theme (most useful, more cost and more errors).
3. Park it and add a "shipped this week" line to the stand-up template (boring, free).

## Strength score
7/10 (medium confidence)
- Problem clarity: 2/2
- Outcome clarity: 1/2 (no measure of "it worked" yet)
- Feasibility: 2/2
- Risk posture: 1/2
- Leverage/impact: 1/2

## Recommendation
Prototype: a grouped list for three weeks. Keep it if the manager stops asking the stand-up question.

## Next decision
How to group PRs.
```
