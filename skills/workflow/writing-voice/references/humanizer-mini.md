# Humanizer Mini Pass

This lightweight pass is inspired by:
- blader/humanizer: https://github.com/blader/humanizer
- Wikipedia guide: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

## Purpose
Remove obvious AI-style artifacts without stripping the writer's voice.

## Keep this pass small
Only enforce these checks by default:
1. Lists to prose where appropriate
2. Emoji cleanup
3. Em dash cleanup
4. Title-case heading cleanup when mismatched with voice style

## Rules
- Do not rewrite for generic neutrality.
- Do not remove strong opinions or natural rhythm.
- Preserve the writer's phrasing if it already sounds human.
- If a list is clearer as a list, keep it.

## Quick QA
- Still sounds like the writer in their samples.
- Reads naturally out loud.
- No obvious AI formatting residue.
