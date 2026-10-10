# pnpm install policy

Last verified: 2026-10-11 against pnpm.io/settings, pnpm.io/settings/build, pnpm.io/settings/dependency-resolution, pnpm.io/supply-chain-security and the pnpm 11 and 12 release posts. pnpm changes quickly: check the docs for the version you're pinning before copying anything here.

## Which file

- **pnpm 11 and later:** `.npmrc` is read for registry and auth settings only. Everything else goes in `pnpm-workspace.yaml` (per project) or `~/.config/pnpm/config.yaml` (global). `pnpm-workspace.yaml` works in a single-package repo too; it doesn't need a `packages:` list. pnpm 11 also stopped reading the `pnpm` field in `package.json` and `npm_config_*` environment variables (use `pnpm_config_*`).
- **pnpm 12:** reports unrecognised `pnpm-workspace.yaml` settings; when the project pins a pnpm version that the running pnpm satisfies, the command fails. Useful for catching typos.
- **pnpm 10:** later 10.x releases read most settings from `pnpm-workspace.yaml` as well as `.npmrc` (check the docs for your exact version) (kebab-case there, e.g. `minimum-release-age`). Prefer `pnpm-workspace.yaml` so the upgrade to 11 needs no move.

To migrate a pnpm 10 config to 11, pnpm suggests: `pnpx codemod run pnpm-v10-to-v11`.

## Settings and the versions that need them

| Setting | What it does | Needs | Default |
|---|---|---|---|
| `minimumReleaseAge` | Minutes a version must have been published before pnpm will install it | ≥10.16 | 1440 from pnpm 11; 0 before |
| `minimumReleaseAgeExclude` | Package names or patterns exempt from the delay | ≥10.16 | none |
| `minimumReleaseAgeStrict` | Fail resolution instead of falling back when nothing old enough matches | ≥11.0 | true if `minimumReleaseAge` is set explicitly |
| `allowBuilds` | Map of packages allowed (`true`) or denied (`false`) to run install scripts | ≥10.26 | unlisted = not allowed |
| `onlyBuiltDependencies` | Older allowlist (array) | pnpm 10 only | **removed in 11** |
| `strictDepBuilds` | Fail the install when a dependency has unreviewed build scripts | ≥10.3 | true from pnpm 11 |
| `dangerouslyAllowAllBuilds` | Lets every dependency run scripts. Don't use it | ≥10.9 | false |
| `blockExoticSubdeps` | Only direct dependencies may come from git or tarball URLs | ≥10.26 | true from pnpm 11 |
| `trustPolicy: no-downgrade` | Fail if a package's publishing trust evidence (e.g. provenance) got weaker than earlier releases | ≥10.21 | off |
| `trustPolicyExclude` | Packages or versions exempt from the trust check | ≥10.22 | none |

## Example: pnpm 11 and later

```yaml
# pnpm-workspace.yaml
# Security settings. Verified against pnpm docs on 2026-10-11; re-check on each pnpm major.

minimumReleaseAge: 4320          # minutes = 3 days (pnpm 11 default is 1440)
minimumReleaseAgeExclude: []     # add only packages you must take on release day, with a reason

strictDepBuilds: true            # default in pnpm 11; keep it explicit
allowBuilds:                     # only packages whose install scripts you've reviewed
  esbuild: true
  # sharp: true
  # core-js: false               # explicitly deny a package that asks

blockExoticSubdeps: true         # default in pnpm 11
trustPolicy: no-downgrade
```

During install, pnpm 11 adds packages with blocked build scripts to `allowBuilds` with a placeholder value for you to set to `true` or `false`. Review each one: does the repo really need that package's script (a native binary, a postinstall download)? If it works without it, set `false`.

## Example: pnpm 10 (before 10.26)

```yaml
# pnpm-workspace.yaml
minimumReleaseAge: 4320          # pnpm ≥10.16
onlyBuiltDependencies:           # removed in pnpm 11; migrate to allowBuilds when upgrading
  - esbuild
trustPolicy: no-downgrade        # pnpm ≥10.21
```

`pnpm approve-builds` lists packages whose scripts were skipped and lets you approve them interactively. Review the config it writes like source code.

## Checking what pnpm sees

```bash
pnpm --version
pnpm config get minimumReleaseAge
pnpm install --frozen-lockfile
```

If a value comes back empty or unexpected, the key is in the wrong file or misspelt, or the version doesn't support it.

## Pinning pnpm itself

- `package.json`: `"packageManager": "pnpm@<exact version>"` (find it with `npm view pnpm dist-tags`). pnpm 11+ also accepts `devEngines.packageManager` with a range, and records the resolved version in the lockfile.
- pnpm 11 can download the pinned version itself (the `pmOnFail` setting; `download` is the default).
- Corepack is not bundled with Node.js 25 and later. If you use it, install it explicitly (`npm install -g corepack`).
- When a new pnpm major ships, the npm `latest` tag may lag behind the new line for a while (pnpm 12 first shipped on a `latest-12` tag). Check `npm view pnpm dist-tags` rather than assuming.
