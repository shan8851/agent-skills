---
name: javascript-supply-chain-hardening
description: Harden a JavaScript or TypeScript repo against npm supply-chain attacks with one pinned package manager, a committed lockfile, a release-age delay, an allowlist for install scripts, frozen installs in CI and Docker, SHA-pinned CI actions, and trusted publishing for packages. Use when the user says "harden npm installs", "lock down pnpm", "supply chain security for this repo", "what should we do after the latest npm compromise", or is cleaning up mixed package managers before shipping.
---

# JavaScript Supply-Chain Hardening

Reduce the chance that a malicious or compromised npm package runs on a developer machine, in CI or in production, and make installs repeatable.

This is a **first line of defence, not a guarantee**. The aim is to make installs deterministic, delay brand-new releases, stop dependency install scripts running unless reviewed, keep CI and Docker on the same policy, and publish without long-lived tokens.

Package-manager security settings change quickly. Every setting below names the version it needs. **Check the current docs and the installed version before writing config**, and never copy a config shape across major versions. The references record when their facts were last verified.

## When to use

- "Harden npm installs", "lock down pnpm", "supply chain security for this repo".
- After a public npm compromise, to check the repo wouldn't have pulled the bad version.
- Before publishing a package or CLI, or when tidying a repo that mixes npm, yarn, pnpm and bun.

Do not use when:
- the user wants a full security audit or penetration test (this covers dependencies and installs only);
- the repo isn't JavaScript or TypeScript;
- the user only wants one dependency upgraded.

## Rules that matter most

1. **Audit before changing anything.** Read what's there first: package manager, lockfiles, CI, Dockerfiles, scripts.
2. **Ask before migrating package managers.** Hardening the current one is often enough. If the user agrees to migrate, remove the old lockfile and update every script, doc, CI job and Dockerfile in the **same commit**.
3. **Put settings where the current docs say.** For pnpm 11 and later, `.npmrc` holds only registry and auth settings; everything else goes in `pnpm-workspace.yaml`. Settings in the wrong file are silently ignored on older versions.
4. **Pin deliberately, and say how to check "current".** Never hardcode a version from memory. Look it up (`npm view pnpm dist-tags`, the Node.js releases page, each action's releases) and record it.
5. **Keep allowlists short.** A build-script or release-age exception list that includes everything is no policy at all.
6. **Never put real secrets in workflow files, Dockerfiles or committed `.npmrc` files.**
7. **Commit or push only when the user asks.**

## Process

1. **Audit.** Run the checks in `references/audit-commands.md` and classify the repo: app, library, CLI or monorepo; public or private; current package manager(s); CI provider; Dockerfiles; packages that need install scripts (native modules, `esbuild`, `sharp`, Prisma, Playwright and similar).

2. **Decide the package manager with the user.** If one is already used consistently, keep it and harden it. If the repo is mixed or the user wants to switch, recommend one (pnpm is a strong default for its build-script and release-age controls), explain the cost, and **wait for a yes** before migrating.

3. **Pin the package manager.** Set `packageManager` in `package.json` to the current version (`npm view pnpm dist-tags`; for pnpm 11 and later, `devEngines.packageManager` also works). Corepack is not bundled with Node.js 25 and later, so don't rely on `corepack enable` alone: install Corepack explicitly (`npm install -g corepack`), or let pnpm manage its own version from `packageManager`.

4. **Write the install policy** in the right file for the version in use. For pnpm, see `references/pnpm-config.md`. In short:
   - **Release-age delay:** `minimumReleaseAge` in minutes (pnpm ≥10.16; defaults to 1440, one day, from pnpm 11). 4320 (3 days) is a sensible repo setting.
   - **Install scripts:** pnpm ≥10.26 and all of pnpm 11: `allowBuilds` map (`esbuild: true`). pnpm 10 before 10.26: `onlyBuiltDependencies` list, which pnpm 11 removed. Keep `strictDepBuilds: true` (the default from pnpm 11) so unreviewed scripts fail the install.
   - **Exotic sources and trust:** `blockExoticSubdeps: true` (pnpm ≥10.26, default from 11) and `trustPolicy: no-downgrade` (pnpm ≥10.21).
   - For npm, yarn or bun, use `references/other-package-managers.md`.

5. **Install and verify.** Run a normal install, review what the build-script prompt or warning asks for, approve only what the repo really needs, then run a frozen install (`pnpm install --frozen-lockfile`) to prove the lockfile is complete.

6. **Bring CI and Docker onto the same policy.** Use `references/ci-and-docker.md`:
   - frozen installs only;
   - the toolchain version taken from `packageManager`, not a separate hardcoded number;
   - Node on a current LTS line (check nodejs.org/en/about/previous-releases);
   - GitHub Actions pinned to full commit SHAs, with a version comment, and kept up to date by Dependabot or Renovate;
   - the Dockerfile copies `pnpm-workspace.yaml` as well as `package.json`, the lockfile and any non-secret `.npmrc`, before installing;
   - a `.dockerignore` so `.env` files and `node_modules` stay out of the build context.

7. **Run the repo's real checks.** List the scripts in `package.json`, then run the aggregate one if it exists (`validate`, `check`, `ci`) or else lint, typecheck, test and build. Fix any that the new policy breaks, often a package that needs its build script approved or an explicit generate step such as `prisma generate`.

8. **Harden publishing** if the repo publishes to npm. Lead with npm trusted publishing (OIDC from CI, no long-lived token, provenance generated automatically). See `references/publishing.md`.

9. **Review the lockfile diff as code.** Look for unexpected new packages, git or tarball sources, new install scripts, and large tree changes from a small edit.

10. **Report** in the format below.

## Output format

```markdown
**Package manager:** [name@version], pinned via [packageManager/devEngines]; [kept / migrated from X with the user's agreement]
**Policy:** [file] — release age [n] [unit]; build scripts allowed for [list]; [other settings]
**CI:** [frozen install, actions pinned to SHAs, Node line]
**Docker:** [changes, or "no Dockerfile"]
**Publishing:** [trusted publishing set up / recommended / not published]
**Checks run:** [commands and results]
**Left for the user:** [e.g. "enable 'Require 2FA and disallow tokens' on npmjs.com", "turn on the org SHA-pinning policy"]
**Re-check:** settings verified against docs on [date]; re-check after the next major package-manager release.
```

## Common failure modes

- **Config in the wrong file:** pnpm 11+ ignores non-auth settings in `.npmrc`, and older versions ignore keys they don't know. Check with `pnpm config get <key>`. pnpm 12 fails on unrecognised `pnpm-workspace.yaml` keys when the project pins a matching version, which catches typos.
- **Units mixed up:** pnpm counts release age in minutes, npm in days, bun in seconds, and yarn takes a duration string such as `"3d"`.
- **Old keys on a new major:** `onlyBuiltDependencies`, `neverBuiltDependencies` and `ignoredBuiltDependencies` were removed in pnpm 11. Use `allowBuilds` (pnpm offers a codemod: `pnpx codemod run pnpm-v10-to-v11`).
- **Docker install ignores the policy:** `pnpm-workspace.yaml` wasn't copied before `pnpm install`, so build-script approvals are missing and the build fails, or the policy silently doesn't apply.
- **Assuming Corepack is there:** it isn't bundled from Node.js 25.
- **Thinking the age delay fixes the existing lockfile.** It only affects new resolution. Versions already locked stay locked.
- **Approving every build script** or adding every package to an exclude list, which recreates the default risk.
- **Tags instead of SHAs for actions:** a tag can be moved if the action's repo is compromised.
- **Pins that never move:** pinning without Dependabot or Renovate (or a written review cadence) leaves the repo on old, vulnerable versions.
- **Silent migration:** switching package manager without asking, or leaving the old lockfile and stale `npm ci` commands behind.
- **Secrets in CI or images:** real tokens in workflow files, or a `.npmrc` with an auth token copied into a Docker layer.

## References

- `references/audit-commands.md`: commands for the initial audit and the lockfile review.
- `references/pnpm-config.md`: annotated `pnpm-workspace.yaml` for pnpm 10 and 11+, with version notes.
- `references/ci-and-docker.md`: GitHub Actions workflow with SHA pins, Dependabot config, Dockerfile and `.dockerignore`.
- `references/other-package-managers.md`: npm, yarn and bun equivalents.
- `references/publishing.md`: npm trusted publishing, provenance and token lockdown.
