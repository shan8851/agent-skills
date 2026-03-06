# agent-skills

![Shan Skills](./assets/skills-header-only.png)

Skills I use regularly with coding agents.

Use these as a starting point and adapt to your own workflow.

## Install via Skills CLI

```bash
# List skills in this repo
npx skills add shan8851/agent-skills --list

# Install all skills globally
npx skills add shan8851/agent-skills -g --all

# Install selected skills globally
npx skills add shan8851/agent-skills --skill writing-voice --skill challenge-me -g -y

# Install to project scope (no -g)
npx skills add shan8851/agent-skills --skill research-review
```

Useful commands:

```bash
npx skills list
npx skills remove <skill-name>
npx skills update
```

## Available skills

- `agent-self-improvement`  
  Weekly propose-only review of dumps, memory, context, skills, and crons to suggest workflow improvements.

- `challenge-me`  
  Stress-tests ideas, plans, projects, and writing concepts with rigorous iterative challenge and tradeoff analysis.

- `dump`  
  Captures raw user dumps into workspace-local markdown logs with no chat response.

- `memory-curation`  
  Curates and promotes memory with signal-first judgment so only durable rules/preferences are stored long-term.

- `research-review`  
  Unified review workflow for links/repos/posts/videos/topics with safe defaults and concise TL;DR output.

- `weekly-focus-brief`  
  Produces a user-centric weekly focus brief from dump/memory signals with concrete actions.

- `write-a-skill`  
  Creates/refines skills with clear triggers, lean structure, and reusable references/scripts.

- `writing-voice`  
  Drafts and polishes posts/emails in user voice with lightweight humanizer + critic pass support.

## Site

Browse a UI version at:

- https://skills.shan8851.com
