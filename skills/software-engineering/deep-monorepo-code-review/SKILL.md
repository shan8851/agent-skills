---
name: deep-monorepo-code-review
description: Deep-review a monorepo after a major refactor or rewrite by validating the branch, splitting API/web/runtime review lanes, and synthesizing a tight triage list.
---

# Deep Monorepo Code Review

## When to use

After a major refactor, rewrite, or large-scale change in a monorepo. This is NOT for small PRs — it's for validating structural integrity across packages after significant rework.

Good fit:
- Monorepo with 2+ packages/workspaces
- Large branch with structural changes (renames, moves, new packages)
- Post-refactor validation before merge
- Pre-release confidence check

Not a fit:
- Single-package changes
- Small PRs (< 20 files)
- Routine feature work

## The Process

### 1. Branch validation

Before reviewing code, confirm the branch is in a reviewable state:

```bash
# Confirm branch exists and is up to date
git log --oneline main..HEAD | head -20

# Check for merge conflicts or stale state
git merge-base --is-ancestor main HEAD && echo "Clean branch" || echo "Needs rebase"

# Count scope of change
git diff --stat main..HEAD | tail -5

# Verify tests pass on the branch
# (run whatever test command the project uses)
```

If the branch doesn't compile, has failing tests, or is massively behind main — stop and fix those first. Reviewing broken code wastes everyone's time.

### 2. Split into review lanes

Don't review everything at once. Split into independent lanes based on package boundaries:

| Lane | Focus |
|------|-------|
| **API/Core** | Business logic, data models, internal APIs |
| **Web/UI** | Components, pages, state management, styles |
| **Runtime/Infra** | Build config, CI, deployment, shared utilities |

For each lane:
1. List all changed files in that lane
2. Read each file
3. Note issues with severity (critical / important / minor)
4. Move to next file — don't jump between lanes

### 3. File-by-file review

For each changed file:

```bash
# Get the diff for this specific file
git diff main..HEAD -- path/to/file.ts
```

Check for:
- **Broken imports** — paths that changed, missing exports
- **Dead code** — exports that nothing imports anymore
- **Type safety** — any `any`, type assertions, or lost type narrowing
- **Naming drift** — renamed exports not updated everywhere
- **Missing tests** — new logic without test coverage
- **API contract changes** — function signatures that changed without updating consumers

### 4. Cross-package consistency

After reviewing each lane independently, check for cross-cutting issues:

```bash
# Find all exports from shared packages
grep -r "export " packages/shared/src/

# Check if they're actually imported elsewhere
grep -r "from '@scope/shared'" packages/
```

Look for:
- Shared types that diverged between packages
- Utility functions duplicated instead of shared
- Config inconsistencies (tsconfig, eslint, etc.)
- Version mismatches in shared dependencies

### 5. Synthesize triage list

Combine all findings into a single prioritized list:

```markdown
## Review: [branch name] → main

### Critical (blocks merge)
- [ ] [file]: [issue description]

### Important (should fix before merge)
- [ ] [file]: [issue description]

### Minor (can fix later)
- [ ] [file]: [issue description]

### Observations (not issues, worth noting)
- [pattern noticed across the codebase]
```

### 6. Smoke test verification

Before signing off:

```bash
# Full build
npm run build  # or whatever build command

# Full test suite
npm run test

# Type checking
npx tsc --noEmit

# Lint
npm run lint
```

All four must pass. If any fail, add to critical list and stop.

## Common patterns to watch for

| Pattern | Why it matters |
|---------|---------------|
| Renamed exports not updated in consumers | Runtime crash on import |
| Shared types with different shapes in different packages | Silent data corruption |
| New dependencies not added to package.json | Works locally (cached), breaks in CI |
| Test files not updated after refactors | False confidence in passing suite |
| Barrel exports that re-export everything | Tree-shaking breaks, bundle bloat |
| Config files (tsconfig, etc.) out of sync | Inconsistent builds across packages |

## Tips

- Review lanes in parallel with subagents if the monorepo is large
- Don't get distracted by style issues — focus on correctness
- If a lane has 0 issues, say so explicitly (silence is ambiguous)
- Keep the triage list actionable — every item should have a clear fix
- Timebox: 30 minutes per lane max. If you're spending longer, the branch needs splitting.
