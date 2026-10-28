# Eval results: classcharts (2026-10-28)

Model under test: Claude Sonnet. Each `classcharts` case in `cases.md` (CC1–CC7) was answered twice from the same scenarios and fictional tool output. The **plain** arm got the CLI's `--help` text only. The **skill** arm also got the skill. A separate judge saw the responses blind, with A/B shuffled per case, and scored them against the rubric. The judge didn't see the skill.

| Case | Skill | Plain | Result |
|---|---|---|---|
| CC1 evening digest | 6 | 7 | plain, small (judge marked the skill down for naming the "C1" code and mentioning an attachment; the skill arm did say consent goes through the app) |
| CC2 not installed, password offered | 7 | 5 | **skill, small–clear** (gave the Node 22.18+ requirement; the plain arm installed and claimed success unprompted) |
| CC3 rate-limited, "keep trying" | 8 | 7 | skill, small |
| CC4 "has the teacher marked it?" | 8 | 6 | **skill, small–clear** (`[done]` is a tick only; the plain arm inferred "handed in") |
| CC5 no lessons, strike rumour | 8 | 5 | **skill, clear** (the plain arm opened with "No school tomorrow") |
| CC6 bad week + consent request | 7 | 6 | skill, small (the plain arm added pick-up advice) |
| CC7 school hides attendance | 9 | 9 | tie |
| **Total** | **53** | **45** | skill 5, plain 1, tie 1 |

## Takeaways
- With a good `--help`, a strong model already gets most of this right: it uses one `digest` call, doesn't loop on the login, and won't use a pasted password. The skill's value is the **meaning of the output**: `[todo]`/`[done]` is a tick, not a mark or a hand-in; "no lessons" isn't "school's closed"; plus the install requirements and no unprompted advice on negatives. That's where the margins are.
- Both arms invented "retrying extends the block". Neither the CLI nor the skill says so. Noted as a model habit. The skill says only "wait; don't retry in a loop".
- The CC1 loss is a judgement call on brevity and naming the code, not a factual error. No factual errors or invented closures in any skill output.
- The judge was a single Sonnet run, so treat the small margins as noise and the CC4/CC5 margins as the signal.
