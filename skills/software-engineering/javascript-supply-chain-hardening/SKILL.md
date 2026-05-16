---
name: javascript-supply-chain-hardening
description: Harden JavaScript and TypeScript projects against npm supply-chain risk with package-manager policy, build-script trust policy, lockfile hygiene, pinning, and CI install gates.
---

# JavaScript Supply-Chain Hardening

Use this when you need to reduce supply-chain risk in a JavaScript or TypeScript repository, especially after npm registry/package compromise news, before shipping a public package, or when cleaning up inconsistent package-manager usage.

This is not a silver bullet. It is a pragmatic first line of defence: make installs deterministic, slow down adoption of brand-new package releases, remove package-manager drift, and ensure CI proves the repo still builds.

## What Done Looks Like

A repo is only hardened when the policy is committed and verified:

- One package manager is used consistently, preferably `pnpm` for new hardening work.
- `package.json` declares a `packageManager` version.
- The repo has a committed lockfile for that package manager.
- New package releases are delayed before install where supported, usually with a 3-day age gate.
- CI installs with a frozen lockfile.
- CI runs the repo's real quality gates: `validate`, `check`, or the available lint/typecheck/test/build scripts.
- Package build scripts are denied by default or explicitly approved with a reviewed trust policy.
- Node, pnpm, Docker base images, and CI actions are pinned intentionally instead of floating silently.
- Pin update automation exists, or there is an explicit manual review cadence.
- Published packages use provenance/two-factor release controls where the registry supports them.
- Old lockfiles and stale CI commands are removed unless intentionally kept.

## Quick Audit

Start by inspecting the repo before changing anything:

```bash
git status --short
node --version
corepack --version || true
ls
```

Then check package-manager state:

```bash
node -e "const p=require('./package.json'); console.log({packageManager:p.packageManager, scripts:Object.keys(p.scripts||{}).sort()})"
for f in package-lock.json yarn.lock pnpm-lock.yaml bun.lock bun.lockb; do [ -e "$f" ] && echo "$f"; done
find .github/workflows -maxdepth 2 -type f 2>/dev/null || true
find . -maxdepth 3 \( -iname 'Dockerfile*' -o -name 'docker-compose*.yml' -o -name 'compose*.yml' \) 2>/dev/null || true
```

Classify the repo:

- App, library, CLI, monorepo, or documentation site.
- Private/internal or public/published.
- Current package manager: npm, yarn, pnpm, bun, or mixed.
- Existing CI provider and install commands.
- Dockerfiles or deployment workflows that install dependencies independently.
- Existing quality scripts in `package.json`.
- Packages that need install-time build scripts, such as native modules, bundlers, ORMs, or browser automation packages.

Do not blindly migrate a repo with unclear constraints. If a tool choice is intentional, preserve it and harden around it.

## pnpm Hardening Checklist

For a typical repo, pnpm is a good default because it supports deterministic installs, strict dependency layout, and delayed adoption of new releases.

1. Enable Corepack if needed:

   ```bash
   corepack enable || true
   ```

2. Add or update `packageManager` in `package.json`:

   ```json
   {
     "packageManager": "pnpm@10.23.0"
   }
   ```

   Use the current stable pnpm version for the project. Keep CI and docs on the same major version.

3. Add `.npmrc` with a release-age gate:

   ```ini
   minimum-release-age=4320
   ```

   `4320` minutes is 3 days. This slows down adoption of newly published dependency versions, which gives the ecosystem time to detect obvious malicious releases.

4. Add an install-script trust policy. In pnpm 10, approve only the packages whose install/build scripts are expected and reviewed:

   ```bash
   pnpm approve-builds
   ```

   This writes the approved package list into project config, commonly `onlyBuiltDependencies` and/or ignored build-script entries. Review the generated config like source code. Keep the list short; examples that may legitimately need approval include `esbuild`, `sharp`, `@prisma/client`, `playwright`, or other native/tooling packages actually used by the repo.

   For newer pnpm versions, use the current equivalent trust-policy setting such as `allowBuilds`. Do not blindly copy an old config shape across pnpm majors; check the installed pnpm docs/help and keep the package-manager version pinned.

5. Install and verify the lockfile:

   ```bash
   pnpm install
   pnpm install --frozen-lockfile
   ```

6. Remove obsolete lockfiles only after pnpm install succeeds:

   ```bash
   rm -f package-lock.json yarn.lock bun.lock bun.lockb
   ```

7. Update scripts, docs, Dockerfiles, and CI that still call `npm`, `npx`, `yarn`, or `bun` unless the mixed setup is deliberate.

8. Run the repo's real gates. Inspect scripts first, then run only the scripts that exist:

   ```bash
   node -e "const p=require('./package.json'); console.log(Object.keys(p.scripts||{}).sort().join('\n'))"
   ```

   Prefer one aggregate gate if present:

   ```bash
   pnpm run validate
   # or
   pnpm run check
   ```

   If there is no aggregate script, run the available individual gates, for example:

   ```bash
   pnpm run lint
   pnpm run typecheck
   pnpm test
   pnpm run build
   ```

## GitHub Actions Pattern

A minimal Node CI job should install pnpm before enabling pnpm cache in `actions/setup-node`:

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 10.23.0
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - run: pnpm run validate
```

If the repo has no aggregate `validate` script, run the scripts that actually exist:

```yaml
      - run: pnpm run lint
      - run: pnpm run typecheck
      - run: pnpm test
      - run: pnpm run build
```

For apps that need environment variables at build time, use dummy values with the correct shape in CI. Never put production secrets in workflow files.

## Pinning Policy for CI, Docker, and Workflows

Pin the toolchain wherever dependencies are installed. A repo is not hardened if local installs use pnpm but Docker or CI still floats versions.

Check for these files and update them together:

```bash
find .github/workflows -maxdepth 2 -type f 2>/dev/null || true
find . -maxdepth 3 \( -iname 'Dockerfile*' -o -name 'docker-compose*.yml' -o -name 'compose*.yml' \) 2>/dev/null || true
```

Good defaults:

- Pin `packageManager` in `package.json`, e.g. `pnpm@10.23.0`.
- Pin `pnpm/action-setup` to the same pnpm major/minor used locally.
- Pin Node in CI and deployment images, e.g. `node-version: 22` or `FROM node:22.11.0-slim` rather than `node:latest`.
- For higher-security repos, pin GitHub Actions and Docker base images by digest/SHA, then use Dependabot or Renovate to keep those pins updated.
- Make Docker builds use the same lockfile discipline:

```Dockerfile
FROM node:22.11.0-slim
WORKDIR /app
RUN corepack enable
COPY package.json pnpm-lock.yaml .npmrc ./
RUN pnpm install --frozen-lockfile
COPY . .
RUN pnpm run build
```

Avoid floating tags like `node:latest`, unpinned package-manager installs like `npm i -g pnpm`, and CI snippets that silently upgrade the package manager.

Pinning creates maintenance work. Add automation or write down the manual cadence:

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: npm
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

For stricter repos, prefer digest/SHA pins plus Dependabot/Renovate updates over mutable tags that never get reviewed.

## Docker Build Hygiene

If the repo ships a container, also check the Docker context and install behaviour:

- Add a `.dockerignore` so secrets, local caches, `.git`, and `node_modules` are not copied into the build context.
- Copy dependency manifests before source files so Docker layer caching does not hide install drift.
- Use `pnpm install --frozen-lockfile` or `pnpm fetch` + offline install patterns; do not use plain `pnpm install` in production Docker builds.
- Do not run package-manager installs from remote shell scripts inside Dockerfiles.
- If using multi-stage builds, ensure every stage that installs dependencies uses the same pinned package-manager policy.

A minimal `.dockerignore` starting point:

```gitignore
.git
node_modules
.pnpm-store
.env
.env.*
npm-debug.log*
pnpm-debug.log*
yarn-debug.log*
.DS_Store
```


## Lockfile Review

A lockfile change is code. Review it instead of treating it as generated noise.

Check for:

- Unexpected new direct dependencies.
- Large dependency-tree changes from a tiny package.json edit.
- New install scripts in transitive packages.
- Git, tarball, file, or non-registry dependency sources.
- Brand-new package versions when no release-age gate was active.
- New or changed approved-build/trust-policy entries.
- Package name confusion: typosquats, abandoned packages, or surprising maintainers.

Useful commands:

```bash
git diff -- package.json pnpm-lock.yaml .npmrc pnpm-workspace.yaml .github/workflows Dockerfile 'Dockerfile*'
pnpm audit --audit-level moderate || true
pnpm outdated || true
```

Treat `audit` output as triage input, not gospel. The aim is to understand risk, not blindly churn dependencies.

## Existing npm/yarn/bun Projects

Prefer improving the repo in-place over doing a performative migration.

- If npm is kept, use `npm ci` in CI and commit `package-lock.json`.
- If yarn is kept, use immutable installs and a committed lockfile.
- If bun is kept, make sure CI uses the same bun version and lockfile strategy.
- If migrating, remove old lockfiles and update all install docs/scripts in the same change.

Mixed package managers are a smell. Keep them only when there is a documented reason.

## Published Packages and CLIs

For public packages, hardening local development is useful, but it does not automatically protect downstream users.

Before release:

- Confirm package contents with the package manager's dry-run/pack command:

  ```bash
  pnpm pack --dry-run
  ```

- Verify CI is green from a clean install.
- Check that generated files, bins, exports, and README instructions still match reality.
- Use npm provenance for CI-based publishing where supported:

  ```bash
  pnpm publish --provenance
  ```

- Require 2FA for registry accounts and avoid long-lived publish tokens where trusted publishing is available.
- Publish only after package-manager and lockfile changes are understood.

A CI-only hardening change does not always require an immediate release. If package contents, runtime dependencies, or user-facing install instructions changed, batch it into the next patch release.

## Common Pitfalls

1. **Thinking an age gate fixes the existing lockfile.** It does not. It only affects future resolution/install behaviour. Still review suspicious lockfile changes.

2. **Using the wrong config key.** In `.npmrc`, use pnpm's kebab-case config: `minimum-release-age=4320`, not camelCase.

3. **Installing pnpm too late in GitHub Actions.** `actions/setup-node` with `cache: pnpm` expects pnpm to exist. Run `pnpm/action-setup` first.

4. **Leaving stale CI commands behind.** A migrated repo should not still run `npm ci`, `yarn install`, or `bun install` unless that is intentional.

5. **Approving every install script.** Trust policy is only useful if the allowlist is small and reviewed. If everything is approved, you have mostly recreated the default risk.

6. **Floating Docker and CI toolchains.** `node:latest`, unpinned pnpm installs, and mutable action references can bypass the repo policy. Pin versions; use digest/SHA pins for stricter environments.

7. **Pinning without updates.** Frozen versions reduce surprise but can rot. Pair pins with Dependabot/Renovate or an explicit review cadence.

8. **Copying secrets into Docker images.** A missing `.dockerignore` can leak `.env`, local caches, or repo metadata into image layers/build contexts.

9. **Leaking secrets into CI.** Use dummy build-time values with the right shape. Do not paste real tokens, API keys, or database URLs into workflow files.

10. **Breaking framework builds by blocking dependency build scripts.** Some frameworks and ORMs need explicit generation steps. For example, Prisma apps often need `prisma generate` before `next build`.

11. **Treating formatting as security.** If a legacy repo fails only on old formatting noise, keep install/build security green first and plan formatting cleanup separately.

## Verification Checklist

- [ ] `package.json` declares the intended package manager.
- [ ] Exactly one intended lockfile is committed.
- [ ] `.npmrc` or equivalent install policy is committed where supported.
- [ ] CI uses frozen/immutable installs.
- [ ] CI runs real repo gates.
- [ ] Install-script trust policy is present and reviewed where pnpm supports it.
- [ ] Dockerfiles and deployment workflows use the same package-manager and lockfile policy.
- [ ] Node, pnpm, CI actions, and Docker base images are pinned intentionally.
- [ ] Pin update automation or a manual review cadence exists.
- [ ] `.dockerignore` prevents secrets/caches from entering container build contexts where Docker is used.
- [ ] Published packages use provenance/2FA/trusted publishing where supported.
- [ ] Docs and scripts no longer reference obsolete package-manager commands.
- [ ] Lockfile changes have been reviewed.
- [ ] Local working tree is clean after the hardening change.
