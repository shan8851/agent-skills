# Link Signal Scoring Model

Use weighted dimensions and sum to 100. The score is still a judgment call, but the weighting forces the useful debate into the open.

## Default Weights

| Dimension | Points | What it measures |
| --- | ---: | --- |
| Usefulness / relevance | 20 | Does this matter for the user's stated context or likely decision? |
| Actionability | 25 | Can someone do, test, adopt, avoid, or decide something concrete after reading? |
| Evidence quality | 25 | Are claims backed by examples, data, code, demos, citations, or clear reasoning? |
| Novelty / insight | 15 | Is there a non-obvious frame, tactic, result, or connection? |
| Signal-to-hype ratio | 15 | Is the source specific and grounded rather than vague, performative, or engagement-bait? |

Actionability and evidence get the highest weights because generic but actionable/evidenced material is often more useful than novel-but-vibes content. Novelty matters, but it should not dominate unless the user's goal is trend discovery.

## Dimension Rubrics

### 1. Usefulness / Relevance (0-20)

- 0-6: Barely relevant, mostly background, or only useful to a very different audience.
- 7-13: Some relevance, but the user would need to translate it heavily.
- 14-20: Directly relevant to the user's context, decision, project, or stated focus.

### 2. Actionability (0-25)

- 0-8: Mostly opinion, observation, or announcement. No clear next step.
- 9-17: Some tactics, examples, or implications, but incomplete.
- 18-25: Clear steps, checklist, implementation idea, decision rule, or behaviour change.

### 3. Evidence Quality (0-25)

- 0-8: Assertion-heavy. No visible support beyond confidence or popularity.
- 9-17: Mixed evidence: examples but no depth, data without context, demos without limitations.
- 18-25: Well supported by concrete examples, source code, data, citations, reproducible method, or honest limitations.

### 4. Novelty / Insight (0-15)

- 0-4: Common/recycled advice or obvious restatement.
- 5-10: Some fresh framing, useful synthesis, or under-discussed implication.
- 11-15: Genuinely non-obvious idea, tactic, result, or connection.

### 5. Signal-to-Hype Ratio (0-15)

- 0-4: Mostly hype, vague claims, audience capture, or engagement bait.
- 5-10: Mixed. Some substance, but padded or oversold.
- 11-15: Dense, specific, caveated, and grounded.

## Label Mapping

- `high` = 75-100: read now, share, or act.
- `medium` = 50-74: skim or save if the topic is relevant.
- `low` = 0-49: discard unless the topic itself is important.

## Recommended Action Mapping

Use the score plus context:

- `read now` — high score and directly relevant to current work/decision.
- `share` — high or high-medium score with a clear audience who would benefit.
- `save for later` — medium/high score, but not relevant right now.
- `skim` — medium score or useful but padded content.
- `discard` — low score, inaccessible source, or unsupported hype.

## Source-Type Adjustments

### Social posts / short threads

- Do not reward engagement metrics directly.
- Evidence may come from a linked source, code snippet, screenshot, or concrete example.
- Keep scores conservative if the post is only a claim with no backing.

### Articles / blog posts

- Reward clear thesis + concrete examples + stated tradeoffs.
- Penalize generic thought leadership that could have been written without domain experience.

### Videos / podcasts

- Score transcript-grounded substance, not production value.
- If transcript is unavailable, cap evidence quality at 12 unless metadata provides unusually strong support.

### GitHub repos

- Use static evidence only unless the user explicitly asks for execution.
- Reward docs, examples, tests, release history, package metadata, and clear maintenance signals.
- Stars are weak social proof, not evidence quality.

### Papers

- Reward method clarity, limitations, reproducibility, and whether the result matters outside the benchmark.
- Penalize benchmark-only claims with no practical path to use.

## Confidence Notes

Always include evidence notes when:

- Content extraction failed or was partial.
- The source is behind auth/paywall.
- The score relies on metadata rather than full content.
- The claims are plausible but unverified.
- The source is a repo/tool that would need deeper review before adoption.
