# Audit and review commands

Last verified: 2026-10-11. Commands are POSIX shell; on Windows run them in Git Bash or WSL, or translate them.

## Initial audit

Run these before changing anything.

```bash
git status --short
node --version
npm --version
pnpm --version 2>/dev/null || echo "no pnpm"
corepack --version 2>/dev/null || echo "no corepack (not bundled from Node.js 25)"
```

Package manager and scripts:

```bash
node -e "const p=require('./package.json'); console.log({packageManager:p.packageManager, devEngines:p.devEngines, scripts:Object.keys(p.scripts||{}).sort()})"
for f in package-lock.json npm-shrinkwrap.json yarn.lock pnpm-lock.yaml bun.lock bun.lockb; do [ -e "$f" ] && echo "lockfile: $f"; done
for f in .npmrc pnpm-workspace.yaml .yarnrc.yml bunfig.toml; do [ -e "$f" ] && echo "config: $f"; done
```

CI, Docker and install commands outside `package.json`:

```bash
find .github/workflows -maxdepth 2 -type f 2>/dev/null
find . -maxdepth 3 -not -path '*/node_modules/*' \( -iname 'Dockerfile*' -o -name 'docker-compose*.yml' -o -name 'compose*.yml' \) 2>/dev/null
grep -rnE '\b(npm (ci|install|i)|npx|yarn( install)?|pnpm (install|i)|bun install)\b' .github Dockerfile* docs README* 2>/dev/null
```

Current versions to pin against (look these up; don't use remembered numbers):

```bash
npm view pnpm dist-tags          # current pnpm release lines
npm view npm dist-tags
# Node.js release lines: https://nodejs.org/en/about/previous-releases
```

## Questions to answer from the audit

- App, library, CLI, monorepo or docs site? Public or private? Published to npm?
- Which package manager(s)? Is a mix deliberate and documented?
- Which packages need install scripts? (native modules, `esbuild`, `sharp`, Prisma, Playwright, Electron and similar)
- Which CI jobs and Dockerfiles install dependencies independently of the local setup?
- Which quality scripts exist (`validate`, `check`, `lint`, `typecheck`, `test`, `build`)?

## Lockfile review

A lockfile change is code. After any install:

```bash
git diff --stat -- package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc .github Dockerfile*
git diff -- pnpm-workspace.yaml package.json
```

Look for:
- new direct dependencies nobody asked for;
- a large tree change from a small `package.json` edit;
- git, tarball, `file:` or other non-registry sources;
- new packages with install scripts, or new `allowBuilds` entries;
- very recent versions if no release-age delay was active;
- typosquats (`lodahs`), abandoned packages, or a surprising change of maintainer.

`pnpm audit` / `npm audit` output is triage input, not a to-do list. Some lockfile scanners only read the first YAML document in a pnpm lockfile and report nothing; check that whatever scanner you use reads it all.
