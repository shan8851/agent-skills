# Publishing packages safely

Last verified: 2026-10-11 against docs.npmjs.com/trusted-publishers. Check the current page before setting this up; supported providers and minimum versions change.

Hardening the repo doesn't protect people who install your package. Publishing is where a stolen token does the most damage.

## 1. npm trusted publishing (lead with this)

Trusted publishing lets CI publish using short-lived OpenID Connect (OIDC) credentials instead of a long-lived npm token.

- **Supported:** GitHub Actions (GitHub-hosted runners), GitLab CI/CD (GitLab.com shared runners) and CircleCI cloud. Self-hosted runners aren't supported at the time of checking.
- **Needs:** npm CLI 11.5.1 or later and Node.js 22.14.0 or later in the publish job.
- **Set up:** on npmjs.com, open the package's settings and add a trusted publisher (repo owner, repo name, workflow file name, and optionally an environment). The package must already exist on npm, so the very first publish may need doing another way.
- **Workflow permissions (GitHub Actions):** the publish job needs `id-token: write`.
- **Provenance:** generated automatically for public packages published from public repos via GitHub Actions or GitLab; no `--provenance` flag needed. CircleCI doesn't generate it.

Minimal GitHub Actions publish job (SHAs are placeholders; see `ci-and-docker.md`):

```yaml
on:
  release:
    types: [published]

permissions:
  contents: read
  id-token: write

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: npm-publish        # optional: add required reviewers to this environment
    steps:
      - uses: actions/checkout@<full-commit-sha> # vX.Y.Z
      - uses: pnpm/action-setup@<full-commit-sha> # vX.Y.Z
      - uses: actions/setup-node@<full-commit-sha> # vX.Y.Z
        with:
          node-version: <current LTS major>
          registry-url: https://registry.npmjs.org
      - run: pnpm install --frozen-lockfile
      - run: pnpm run build
      - run: npm --version            # must be ≥ 11.5.1 for OIDC; upgrade npm in the job if not
      - run: npm publish
```

This uses `npm publish` because npm's docs describe OIDC with the npm CLI. If you want `pnpm publish`, check pnpm's current docs for its trusted-publishing support first.

## 2. Lock down tokens

After trusted publishing works:
- On npmjs.com, under the package's **Publishing access**, choose "Require two-factor authentication and disallow tokens". Trusted publishers keep working.
- Revoke old automation and granular tokens that are no longer needed.
- npm also supports a staged-publish option where CI publishes need a maintainer's approval before going public; check the current docs if the user wants that.

These are account settings: tell the user what to change; don't change them yourself.

## 3. Before every release

- `pnpm pack --dry-run` (or `npm pack --dry-run`) and read the file list: no `.env`, test fixtures with real data, or source maps you didn't mean to ship.
- CI green from a clean, frozen install.
- `bin`, `exports` and README install instructions match reality.
- Publish only after lockfile and package-manager changes are understood.

A CI-only hardening change doesn't need a release. If runtime dependencies or install instructions changed, include it in the next patch release.
