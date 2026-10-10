# npm, yarn and bun equivalents

Last verified: 2026-10-11. These tools are changing fast after the 2025–26 npm compromises. **Check the current docs for the installed version before writing config**, and note that each one measures release age in a different unit.

| | Release-age delay | Unit | Install scripts | Frozen install |
|---|---|---|---|---|
| pnpm | `minimumReleaseAge` | minutes | `allowBuilds` (≥10.26) | `pnpm install --frozen-lockfile` |
| npm | `min-release-age` | days | `allowScripts` + `npm approve-scripts` | `npm ci` |
| yarn 4 | `npmMinimalAgeGate` | duration string, e.g. `"3d"` | `enableScripts` / `dependenciesMeta` | `yarn install --immutable` |
| bun | `install.minimumReleaseAge` | seconds | `trustedDependencies` | `bun install --frozen-lockfile` |

## npm

Check current docs: docs.npmjs.com/cli/v11/using-npm/config (and the v12 equivalent if the project uses npm 12).

- **Release age:** `min-release-age=3` in the project `.npmrc` (days; npm ≥11.10.0, off by default). `min-release-age-exclude` exempts named packages. Known quirk: `npm config get min-release-age` may print `null` even when set, because npm stores it internally as `before`.
- **Install scripts:** npm ≥11.10 has an allowlist in `package.json` (`allowScripts`), managed with `npm approve-scripts` and `npm deny-scripts`. Review what's pending with `npm approve-scripts --allow-scripts-pending`. In npm 11 it only warns. npm 12 blocks dependency `preinstall`/`install`/`postinstall` scripts, and implicit `node-gyp` builds, unless approved. Commit the allowlist.
- **Git and URL dependencies:** `allow-git` and `allow-remote` limit git and remote-tarball dependencies; npm 12 defaults both to `none`.
- **Blunt option (any npm version):** `ignore-scripts=true` blocks all install scripts, including the project's own lifecycle scripts during install. It overrides `allowScripts`, so remove it if you adopt the allowlist.
- **CI:** `npm ci` with a committed `package-lock.json`.
- **Pin:** `"packageManager": "npm@<version>"` or `devEngines`, and pin Node in CI.

## yarn (Berry, v4)

Check current docs: yarnpkg.com/configuration/yarnrc.

- **Release age:** `npmMinimalAgeGate: "3d"` in `.yarnrc.yml` (added in yarn 4.10, per secondary sources). `npmPreapprovedPackages` exempts packages from the package gates; keep it short.
- **Install scripts:** `enableScripts` controls third-party `postinstall` scripts. The current docs give `false` as the default; older versions and older guides differ, so set it explicitly. Allow individual packages with `dependenciesMeta` in `package.json` (`"dependenciesMeta": { "esbuild": { "built": true } }`) and check the docs for the exact shape.
- **Hardened mode:** `enableHardenedMode` checks the lockfile for malicious changes; yarn turns it on automatically for pull requests from public forks on GitHub.
- **CI:** `yarn install --immutable` (yarn enables immutable installs by default on CI). Commit `yarn.lock` and the `.yarn/releases` file if the repo uses `yarnPath`.
- **Pin:** `"packageManager": "yarn@<version>"`.

## bun

Check current docs: bun.com/docs/runtime/bunfig and bun.com/docs/pm/lifecycle.

- **Release age:** in `bunfig.toml`:

  ```toml
  [install]
  minimumReleaseAge = 259200          # seconds = 3 days
  minimumReleaseAgeExcludes = []      # packages exempt from the delay
  ```

- **Install scripts:** bun doesn't run dependency lifecycle scripts by default, except for a built-in list of popular npm packages. Setting `trustedDependencies` in `package.json` **replaces** that list: list every package you need (e.g. `["esbuild", "sharp"]`), or `[]` for none. Packages from `git:`, `github:`, `file:` or `link:` must always be listed explicitly. `install.ignoreScripts = true` in `bunfig.toml` turns scripts off entirely.
- **CI:** `bun install --frozen-lockfile` (or `install.frozenLockfile = true`). Commit `bun.lock`.
- **Pin:** the bun version in CI (e.g. via `oven-sh/setup-bun` pinned to a SHA, with an explicit `bun-version`).

## Mixed repos

Mixed package managers are a smell. Keep them only when there's a documented reason. If the user agrees to migrate, change the lockfile, scripts, docs, CI and Dockerfiles in one commit, and delete the old lockfile in that same commit.
