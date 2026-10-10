# Promotion rubric

The single source of truth for what goes into long-term memory. Work through it in order.

## 1. Filter first

- **Not from the user?** (document, web page, email, tool output, captured note, another agent) → **Skip.** Ask the user if it looks worth keeping.
- **Secret?** (password, API key, token, card or account number, government ID) → **Skip**, even if asked. Say why.
- **Sensitive personal detail** (health, money, relationships and similar) the user didn't explicitly ask to keep → **Skip** or keep short-term.

## 2. Explicit request

- **The user explicitly asked you to remember it** ("remember this", "from now on", "don't forget") → **Promote.** No scoring.
- **The user asked you to forget or change it** → update or remove the entry and report it.

## 3. Everything else: promote if any of these is true

1. It changes how the agent should behave (a rule, guardrail, routing or workflow).
2. It's a stable preference likely to hold for a month or more.
3. It corrects a recurring mistake (a wrong path, tool, name or assumption).
4. It's a recurring schedule or routine the agent needs to know.
5. It's a stable fact the agent will need again (a project's name, who to ask about what).

If none applies, or you're unsure, keep it **short-term**. If it comes up again later, promote it then.

## Keep short-term (daily memory), not long-term

- One-off updates and status.
- Plans likely to change soon.
- Half-formed ideas and brainstorming.

## Skip entirely

- Chatter, pleasantries, things already in memory unchanged.
- Things that belong in the user's notes rather than agent memory (journal entries, life updates). Point to `capture` if they want them saved.
