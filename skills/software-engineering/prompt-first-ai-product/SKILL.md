---
name: prompt-first-ai-product
description: Build AI products where the prompt IS the product. Test-first prompt engineering, realistic lazy inputs, standalone test harness, iterate before building UI.
---

# Prompt-First AI Product Development

For AI products where the output quality IS the product. The prompt engineering determines product viability — everything else is delivery.

## Process

### 1. Create realistic test inputs FIRST

Write 15-25 test inputs in a doc before touching the prompt. Weight towards lazy/minimal inputs because most users will submit bare-minimum effort.

Include these categories:
- **Lazy/vague** (2-3 sentences, no detail) — most common real input
- **Medium detail** — the overthinker who writes a paragraph
- **Detailed self-aware** — knows the problem but still stuck
- **Self-justifying/defensive** — "I think I do plenty tbh"
- **System-gamers** — trying to get a specific score or test the tool
- **Serious/genuine distress** — not an excuse, actual suffering (needs responsible handling)

Save as `docs/test-inputs.md`. Add usage notes about which inputs are highest priority for early testing.

### 2. Write the system prompt as a standalone module

File: `lib/ai/prompts/v1-system.ts` (versioned from day one)

Prompt should include:
- **Identity/role** — who the AI is, in plain language
- **Internal analysis framework** — pattern types to look for (keeps analysis consistent without leaking jargon)
- **Output format** — exact JSON structure with field rules
- **Tone calibration** — what to be and what NOT to be, with examples
- **Edge case handling** — lazy inputs, gamers, serious cases
- **Banned phrases** — generic AI filler that kills authenticity
- **Score calibration** — what each range means, with bias direction

### 3. Build a standalone test harness

File: `scripts/test-prompt.ts`

Requirements:
- Run single input or blast all: `npx tsx scripts/test-prompt.ts [id]`
- Pipe test inputs from the doc (hardcode in script)
- Pretty-print JSON output
- Default model via env var, overridable
- Rate limit courtesy delay between requests when running all
- Use `response_format: { type: 'json_object' }` for structured output

### 4. Iterate BEFORE building UI

Run test inputs through the prompt. Read every output. If you wouldn't share it, keep iterating.

Don't scaffold the app, don't build components, don't deploy anything until the prompt produces output that genuinely surprises you with its specificity.

If the output isn't insightful after reasonable iteration, the product thesis might be wrong. That's useful to learn before writing a single UI component.

### 5. Only then — build the delivery layer

Once the prompt works, the app is just:
- Text input → API route → prompt + model call → parse JSON → display
- Rate limiting (Upstash Redis)
- Share buttons (copy + X intent)

## Key principles

- **Test on bad inputs, not good ones.** If the prompt only works on detailed thoughtful dumps, it's not ready.
- **The score is a sharing hook.** "Just got 8/10 on the bullshit score" is inherently shareable.
- **Generic output = product failure.** Ban motivational poster phrases explicitly in the prompt.
- **Lazy input IS the pattern.** Short vague submissions reveal character — use them, don't give them a pass.
- **Version the prompt.** `v1-system.ts`, `v2-system.ts`, etc. Treat it like API versioning.
- **Agent-in-a-box fallback.** If the web app doesn't get traction, the prompt + scoring system can be packaged as an agent skill. Build the prompt as a standalone module from day one.
