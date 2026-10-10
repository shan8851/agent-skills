# Worked Examples

Fictional examples. Links use `example.com` placeholders; real answers link the actual sources.

## 1. Quick take

**User:** "Is this worth reading?" + a link to a blog post titled *"We cut our CI time by 80% with one config change"*.

The agent fetches the post and reads it in full. It's a 1,500-word post from a company engineering blog. The "one change" is enabling dependency caching; the 80% figure is from one repo, with a before-and-after chart and the config snippet. There's a short section on when caching made things slower.

```markdown
**TL;DR:** An engineering blog post showing how turning on dependency caching cut one team's CI runs from about 20 minutes to about 4, with the exact config.

**Verdict:** Skim. Useful if your CI doesn't cache dependencies yet; nothing new if it does.

**Why**
- The config snippet is concrete and copyable.
- The "when caching hurt" section is the most valuable part: cache invalidation on lockfile changes made some runs slower.
- The headline oversells it: the 80% is one repo, and most of the gain is standard caching.

**Evidence notes**
- One repo, one before-and-after chart, no variance shown.
- Written by the team that did the work; not sponsored.

**Signal:** 3/5 (practical and honest about limits, but familiar)
```

## 2. Deep research (shortened)

**User:** "Look into whether we should switch our small team's docs from a wiki to docs-in-the-repo."

The agent splits this into: what each approach is good at, what teams report after switching, the migration cost, and what fits a small team. It reads two vendor docs pages, one independent write-up, and a community thread.

```markdown
**TL;DR:** For a small team whose docs are mostly about the code, move them into the repo. Keep the wiki for non-engineering pages. The main risk is that non-developers stop contributing.

**Key findings**
- Docs in the repo get reviewed with the code change, so they drift less (https://example.com/independent-write-up).
- Teams report that non-developers edit far less once docs need a pull request (https://example.com/community-thread). Anecdotal, but consistent across replies.
- Most static docs generators need a build step and hosting; a plain folder of Markdown files rendered by the code host needs neither (https://example.com/vendor-docs-a).
- Wiki search across all pages is better than most repo-based setups out of the box (https://example.com/vendor-docs-b).

**Risks and caveats**
- Non-developer contributions drop.
- Migration of old pages is manual; links will break.
- Inference, not sourced: with fewer than ten people, the drift problem may be small enough not to matter.

**Confidence:** Medium. Clear on the trade-offs; thin on data about small teams specifically.

**Next step:** Move one actively maintained page (e.g. the setup guide) into the repo for a month and see whether it stays current.

**Sources**
- Independent write-up (https://example.com/independent-write-up): before-and-after experience from one team.
- Community thread (https://example.com/community-thread): contributor drop-off reports.
- Vendor docs A and B: features and limits of each approach.
```

## 3. Edge case: can't fetch

**User:** "TL;DR this" + a link to a video with no transcript available.

```markdown
I couldn't get a transcript for this video, only the title and description. Based on those alone, it's a 40-minute talk about database indexing for beginners.

If you paste the transcript (most video sites can show one under the description), I'll give you a proper TL;DR and verdict.
```
