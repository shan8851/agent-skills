# CI and Docker

Last verified: 2026-10-11 against GitHub's "Secure use reference" for Actions, the pnpm 11 release notes and the Node.js releases page. Re-check action versions and Node release lines each time you use this.

## GitHub Actions

Rules:
- **Pin every third-party action to a full-length commit SHA**, with the version in a comment. GitHub's docs say this is currently the only way to use an action as an immutable release; a tag can be moved if the action's repo is compromised. Check the SHA comes from the action's own repo, not a fork.
- Let Dependabot or Renovate update the SHA pins (they update the SHA and the comment). Note that Dependabot doesn't raise *security alerts* for SHA-pinned actions, so keep version updates switched on.
- Organisations and repos can enforce SHA pinning with a GitHub Actions policy setting. Suggest it to the user; don't change it yourself.
- Take the pnpm version from `packageManager` in `package.json` rather than repeating it in the workflow.
- Use a current Node.js LTS line (see nodejs.org/en/about/previous-releases). pnpm 11 needs Node.js 22 or later.
- Set `permissions:` to the minimum (`contents: read` for a build job).
- Use dummy values with the right shape for build-time environment variables. Never commit real secrets.

How to find the SHA for a release (replace the owner, repo and tag):

```bash
gh api repos/actions/checkout/git/ref/tags/<tag> --jq .object.sha
# If .object.type is "tag" (an annotated tag), resolve it once more:
gh api repos/actions/checkout/git/tags/<sha-from-above> --jq .object.sha
```

Tools such as `pinact` or Renovate's `helpers:pinGitHubActionDigests` preset can pin a whole workflow at once.

Example workflow. The SHAs are placeholders: look up the current release of each action and fill them in.

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<full-commit-sha> # vX.Y.Z
      - uses: pnpm/action-setup@<full-commit-sha> # vX.Y.Z — reads the version from packageManager
      - uses: actions/setup-node@<full-commit-sha> # vX.Y.Z
        with:
          node-version: <current LTS major, e.g. from .nvmrc>
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - run: pnpm run validate   # or the lint / typecheck / test / build scripts that exist
```

Install pnpm (`pnpm/action-setup`) **before** `actions/setup-node` with `cache: pnpm`, or the cache step can't find pnpm.

Keeping the Node version in `.nvmrc` or `.node-version` and using `node-version-file:` keeps local and CI in step.

## Dependabot

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: npm          # also covers pnpm and yarn lockfiles
    directory: /
    schedule:
      interval: weekly
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
  - package-ecosystem: docker
    directory: /
    schedule:
      interval: weekly
```

Dependabot updates aren't held back by your package manager's release-age setting. Dependabot has its own `cooldown` option for delaying new versions; check GitHub's current Dependabot docs for its syntax before relying on it. Renovate has `minimumReleaseAge`.

## Dockerfile

```Dockerfile
# Pin the base image by digest; find it with `docker buildx imagetools inspect node:<tag>`.
FROM node:<current-LTS>-slim@sha256:<digest>
WORKDIR /app

# Node.js 25+ images don't bundle Corepack. Either install it (pinned) or install the
# exact pnpm version from package.json's packageManager field.
RUN npm install -g corepack@<version> && corepack enable

# Copy everything pnpm reads for policy BEFORE installing. Without pnpm-workspace.yaml,
# allowBuilds / minimumReleaseAge aren't applied and approved build scripts don't run.
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
# Copy .npmrc only if it exists and holds no secrets. For a private registry token,
# use a build secret instead: RUN --mount=type=secret,id=npmrc,target=/root/.npmrc ...
COPY .npmrc ./

RUN pnpm install --frozen-lockfile
COPY . .
RUN pnpm run build
```

Notes:
- `COPY` fails if a listed file doesn't exist. Drop lines for files the repo doesn't have.
- In a monorepo, also copy each workspace package's `package.json`, or use `pnpm fetch` (which needs only the lockfile and `pnpm-workspace.yaml`) followed by `pnpm install --offline --frozen-lockfile`.
- Every stage that installs dependencies needs the same files and the same pinned pnpm.
- Never `curl | sh` an installer inside a Dockerfile, and avoid unpinned `npm i -g pnpm`.

## .dockerignore

```gitignore
.git
node_modules
.pnpm-store
.env
.env.*
*.log
.DS_Store
coverage
```

Without it, `.env` files, local caches and Git history can end up in the build context and image layers.
