# Decision Guides

## When to add scripts
Add scripts when one or more are true:
- the operation is deterministic and repeated often
- reliability matters more than creative variation
- manual/tool-generated code would be re-written every run
- you need explicit error handling or consistent formatting

Do not add scripts just because you can.

## When to split files
Split out references when one or more are true:
- `SKILL.md` is getting bloated and hard to scan
- the skill covers multiple domains/lanes
- advanced details are only needed in some runs
- examples or schemas would crowd core instructions

Keep core workflow in `SKILL.md`; put depth in `references/`.
