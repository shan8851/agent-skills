---
name: classcharts
description: Answer a parent's questions about their child's school from ClassCharts (used by many UK secondary schools) with the read-only `classcharts` CLI, covering homework, timetable, announcements, behaviour points, detentions and attendance, plus a one-call daily digest. Use when someone asks "what homework is due?", "anything outstanding?", "what's on tomorrow?", "is there school on Monday?", "what's this week look like?", "has the school sent anything?", "any trips or forms?", "how's behaviour been?", "any detentions?", "how's attendance?" or "anything I need to know?", or wants a school summary for a family chat.
---

# ClassCharts

Read-only CLI for a ClassCharts **parent** account: `classcharts <command> [date] [options]`. It can see what a parent sees in the ClassCharts app. It can't tick homework, reply to consent requests or message teachers.

> The canonical copy of this skill lives in the tool's repo ([shan8851/classcharts-agent](https://github.com/shan8851/classcharts-agent), also printed by `classcharts skill`). This copy is for discovery. If they disagree, trust the one that matches the installed version.

## When to use

- Homework (due, outstanding, overdue, details), lessons for a day or week, whether a day is a school day.
- School announcements, trips, letters and consent forms.
- Behaviour points, detentions, attendance.
- An evening or morning "anything I need to know?" summary.

Do not use for:
- anything that writes (ticking homework, giving consent, messaging the school). Say it's read-only and point the parent to the ClassCharts app;
- other school systems (Arbor, Satchel One, Bromcom and so on);
- interpreting a school's behaviour policy or what a code "really" means. Report it as given and suggest asking the school.

## Before the first command

1. **Check it's installed:** `command -v classcharts` (macOS/Linux) or `where classcharts` (Windows).
2. **If it's missing, ask the user before installing.** Offer `npm install -g @shan8851/classcharts-agent`, which needs Node.js 22.18 or later (`node --version`).
3. **Check there's a login:** `classcharts pupils`. Exit code 2 with "No ClassCharts login found" means nobody has signed in yet.
4. **Sign-in is done by a person, once.** Tell them to run `classcharts setup` in a terminal themselves. It prompts for the parent email and password, tests them, and saves them privately on that machine. Don't ask for the password in chat, don't put it in a command, and don't try to run `setup` yourself: it refuses non-interactive input.

## Pick the command

Start with the narrowest command that answers the question. For a general check-in, `digest` is one call that covers everything.

| Question | Command |
|---|---|
| "Anything I need to know?" / daily summary | `digest` (next school day, homework to do including overdue, detentions, behaviour, announcements, attendance) |
| "What's on tomorrow?" / "Is there school Monday?" | `day tomorrow` / `day monday` |
| "What's the next school day?" (evenings, Fridays, holidays) | `day next` (skips weekends and holidays) |
| "What does this week / next week look like?" | `week` / `week next` |
| "What homework is outstanding?" | `homework --todo` |
| "What homework is due this week?" | `week`, or `homework --from today --to friday` |
| "Tell me more about the art homework" | `homework --full` (full text, links, attachment names) |
| "Has the school sent anything?" / "Any trips or forms?" | `announcements` (`--full` for the whole text) |
| "How's behaviour been?" | `behaviour` (last 7 days; `--from` for longer) |
| "Any detentions?" | `detentions` |
| "How's attendance?" | `attendance` (this school year) |
| "Which children are linked?" | `pupils` (also shows which sections the school turns on) |

- Dates: `YYYY-MM-DD`, `today`, `tomorrow`, `yesterday`, `next`, or a weekday (`friday` means the next Friday, today included).
- More than one child linked: pass `--pupil <first name or id>`, or run once per child when the question is about all of them.
- Text output is already compact. Add `--json` only when you need to process the result.
- One `week` call beats five `day` calls. The login is cached between calls, but don't hammer the API.

## Reading the output

- **`[todo]` / `[done]` is a tick, not a mark.** It shows whether someone ticked the homework off in ClassCharts. It says nothing about whether it was handed in or how it was graded. Never say "the teacher marked it done".
- **`[todo]` homework due before today is overdue.** Mention it first.
- **`week 1` / `week 2`** is the school's two-week timetable rotation, when the school publishes it.
- **"No lessons (weekend, holiday or INSET day)"** means ClassCharts returned no lessons for that date. In term time that usually means a holiday or INSET (staff training) day. Say "no lessons on ClassCharts", not "the school is closed", unless an announcement says so.
- **`[consent needed]`** on an announcement means the school wants a parent's response in ClassCharts. You can't give it. Tell the parents, with the deadline if the announcement gives one.
- **Behaviour reasons and scores are each school's own** ("Commendation", "C2", "S1"). Report them as given. Don't guess what a code means.
- **A section the school doesn't show** (text says the school doesn't show it; `hiddenBySchool` in JSON) is the school's ClassCharts setting, not an error. Say so once and move on.
- Times are in the school's timezone. Gaps between lessons are breaks or lunch. Rooms and teachers are as the school records them.

## Answering well

1. **Lead with anything that needs action:** overdue or soon-due `[todo]` homework, consent requests, upcoming detentions. Then the rest.
2. **Celebrate positives.** Keep negatives and detentions factual and low-key, with no lecturing and no speculation about why. The parents decide how to handle them. In a group chat that includes the child, be especially careful.
3. **Keep it short for a chat:** a few lines, no tables, no headings. Leave out empty sections ("no detentions") unless the user asked about them.
4. **Don't post attachment links in a chat.** Attachment URLs (`--json`, `attachments[].url`) are signed and expire. Name the attachment and say it's in ClassCharts.
5. **Read-only:** if asked to tick homework, give consent or message a teacher, say you can't and that the parent can do it in the ClassCharts app.

## Errors

| Exit code | Message | What to do |
|---|---|---|
| 2 | "No ClassCharts login found" | Setup hasn't been run. Ask a person to run `classcharts setup` in a terminal. |
| 2 | "Sent the login back to its sign-in page" | Usually too many login attempts: ClassCharts blocks logins for a few minutes. **Wait; don't retry in a loop**. Tell the user to try again in about five minutes. If it keeps happening after a wait, the email or password is probably wrong, so they should re-run `setup`. |
| 2 | "Login failed" / "not understood" | Wrong details, or ClassCharts changed its login. Tell the human; don't work around it. |
| 1 | Bad date or another error | The message says what went wrong. Fix the input (for example an inverted `--from`/`--to`) and run once more. |

Never answer from memory or guesswork when the tool fails. "I couldn't reach ClassCharts" is a fine answer.

## Adapting to your setup

- **Claude Code:** install the skill under `~/.claude/skills/classcharts/`, or let the tool write the canonical copy: `classcharts skill > ~/.claude/skills/classcharts/SKILL.md`.
- **Codex / OpenClaw / a chat bot (WhatsApp, Telegram):** the agent needs a shell on the machine where `classcharts setup` was run, because the login is saved per user on that machine (`~/.config/classcharts-agent/.env`). Run setup as the same OS user the bot runs as.
- **Scheduled digest:** a daily `classcharts digest` from cron or your agent's scheduler works well. Once a day is plenty.

## Common failure modes

- Saying a teacher "marked" homework done, or that `[done]` means handed in.
- Calling a no-lessons day a strike, closure or illness without an announcement saying so.
- Retrying a blocked login in a loop instead of waiting.
- Asking for the parent's password in chat, or trying to script `setup`.
- Explaining what a behaviour code means, or moralising about a negative point.
- Pasting attachment URLs into a group chat.
- Offering to give consent or tick homework.

## References

- `references/worked-example.md`: an evening digest turned into a family-chat message, annotated.
- `references/edge-cases.md`: not installed, no login, rate-limited, several children, holidays, hidden sections, write requests, a negative behaviour week.
