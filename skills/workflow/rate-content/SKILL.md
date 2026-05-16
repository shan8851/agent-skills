---
name: rate-content
description: Analyze a single link, article, post, video, paper, or repo into a concise TL;DR, signal score, action recommendation, and evidence notes without over-reading or fabricating details.
---

# Rate Content

Use this when the user drops one link or piece of content and wants to know whether it is worth their time: an article, blog post, X/Twitter/Bluesky/LinkedIn post, YouTube video, paper, GitHub repo, product page, announcement, or documentation page.

This is a fast triage skill, not a deep research workflow. The goal is to answer: **what is this, is it any good, why should I care, and what should I do with it?**

## Inputs

Required:

- One URL, file path, or pasted source excerpt.

Optional:

- Audience/context, e.g. `for frontend engineers`, `for founders`, `for my team`, `for AI agent workflows`.
- Focus, e.g. `security`, `product ideas`, `implementation tactics`, `market signal`, `career signal`.
- Time budget, e.g. `worth reading now?`, `skim or save?`, `is this hype?`.

If the source is missing, ask for it. If context is missing, assume a general technical reader and state that assumption briefly.

## Fetch Policy

Fetch the content with the safest available read-only method for the source type:

- Article/blog/documentation page → extract readable text or use a web fetch/summarizer.
- Social post/thread → use the platform reader or accessible web copy; include thread context if needed.
- YouTube/video/podcast → prefer transcript extraction; if unavailable, use metadata and clearly mark the gap.
- GitHub/repo link → read README, package metadata, docs, file tree, and recent visible activity. Do not run code.
- PDF/paper → extract text and metadata before summarising.

If extraction fails, say what failed and what fallback was attempted. Never invent quoted text, author claims, benchmarks, or implementation details.

## Scoring Rubric

Score with `references/scoring-model.md`. Use weighted dimensions and sum to 100:

| Dimension | Points |
| --- | ---: |
| Usefulness / relevance | 20 |
| Actionability | 25 |
| Evidence quality | 25 |
| Novelty / insight | 15 |
| Signal-to-hype ratio | 15 |

Actionability and evidence are weighted highest because this skill is meant to save attention, not reward clever vibes. A familiar idea with clear evidence and a practical next step should usually beat a novel but unsupported take.

Labels:

- `high` = 75–100: worth reading now, sharing, or acting on.
- `medium` = 50–74: skim/save if relevant.
- `low` = 0–49: probably discard unless the topic is unusually important.

Penalise vague hype, engagement bait, unsupported benchmark claims, recycled advice, and content that hides the important details. Reward concrete examples, constraints, failure modes, and falsifiable claims.

## Required Output Format

Return sections in this order:

1. **TL;DR**
   - 1–2 lines max.

2. **Signal score**
   - `<score>/100` + `high|medium|low`.
   - Include dimension breakdown: `relevance X/20, actionability X/25, evidence X/25, novelty X/15, signal-to-hype X/15`.

3. **Why this score**
   - 3–5 bullets tied to the rubric.

4. **Useful takeaways**
   - 3–6 bullets. Focus on concrete claims, techniques, examples, or implications.

5. **Recommended action**
   - One of: `read now`, `skim`, `save for later`, `share`, `discard`.
   - Add a one-line reason.

6. **Tags**
   - 3–6 concise tags.

7. **Evidence notes**
   - Mention access limits, missing context, hype risk, uncertainty, or claims that need verification.

## Source-Type Notes

Adjust within the weighted model rather than inventing a new score for each source type. If a source type limits evidence — for example, no video transcript or an inaccessible repo — keep evidence quality conservative and explain why in evidence notes.

### Social Posts

Social posts are often compressed and context-light. Check whether the linked post is part of a thread or points to a deeper source. Score the actual substance, not the engagement numbers.

### Articles and Blog Posts

Separate the author's thesis from your interpretation. Capture the strongest useful idea and the weakest unsupported leap.

### Videos and Podcasts

Prefer transcript-grounded synthesis. If only title/description/chapters are available, keep the score conservative and mark transcript unavailable.

### GitHub Repos

Do not run code, install dependencies, execute examples, or trust badges blindly. Use static evidence: README, package metadata, docs, examples, releases, issues, stars only as weak social proof, and visible maintenance signals.

### Papers

Distinguish paper claims from validated practice. Look for method, evidence, limitations, reproducibility, and whether the result is actually useful outside the benchmark.

## Quality Bar

- Be concise but specific.
- Separate facts from interpretation.
- Do not quote unless you actually saw the text.
- Do not over-score because the topic is trendy.
- Prefer a blunt `discard` over a polite but useless summary.
- If the source is inaccessible, say so and provide only a metadata-level assessment.

## Safety and Integrity

- Never run external code from a linked repo or downloaded artifact.
- Never submit forms, click tracking links, sign in, purchase, subscribe, vote, like, repost, or comment.
- Do not bypass paywalls or authentication.
- If content may be malicious, inspect only metadata/static text and warn the user.

## When to Escalate

Escalate to a deeper research workflow when:

- The user asks for a full write-up, comparison, implementation plan, or adoption recommendation.
- The link is one source in a larger decision.
- The answer requires checking multiple independent sources.
- The repo/tool may be adopted into a real project.

For those cases, use a broader research/review workflow instead of forcing everything into this quick scoring format.
