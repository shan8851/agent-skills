---
name: recall
description: Find context from past conversations, decisions, or discussions when current session memory falls short. Use when the user asks "did we talk about X?", "where did we decide Y?", or when you can't find something and are about to say "I don't know".
category: workflow
---

# Recall

Structured escalation for finding past context. Stop as soon as you find the answer.

## Trigger
- User asks about a past conversation, decision, or setup
- You're about to say "I can't find it" or "I don't know"
- Any "did we...", "didn't we...", "remind me...", "where is..." question about prior work

## Rules
- Do NOT re-read files already loaded into session context (boot files like MEMORY.md, AGENTS.md, etc are already in your context window at session start).
- Do NOT re-read workspace files you've already accessed this session.
- Follow the escalation order below. Stop as soon as you find the answer.

## Escalation order

### Step 1: Session context (zero cost)
Check what you already know from loaded workspace files. Think before searching.

### Step 2: Recent daily memory files (cheap)
Read the last 7 days of daily memory files. These capture checkpoints, decisions, and context from recent sessions.

Scan for the topic. If found, report the answer and which file had it.

### Step 3: Workspace text search (medium)
Search across workspace directories (memory, dumps, notes) for the topic using grep or similar. If found, read the relevant file section and report.

### Step 4: Chat history search (if available)
If you have access to a chat history search tool (e.g. Discord search, channel logs), search for the topic there. This catches things discussed in chat but never persisted to files.

### Step 5: Session log search (expensive, last resort)
Search raw session transcripts only if steps 1-4 failed. Use ripgrep or grep to find matching session JSONL files, then extract relevant user/assistant messages.

## Output
- Report what you found and where (file path, channel, session ID)
- If nothing found after all steps: say so clearly and suggest it might have been verbal, in a channel you can't search, or never captured
- Never guess or fabricate context

## Anti-patterns
- Do not skip steps or jump to expensive searches first
- Do not re-read boot files that are already in context
- Do not say "I can't find it" without completing at least steps 1-4
