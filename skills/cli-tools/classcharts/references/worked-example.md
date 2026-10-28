# Worked example: an evening digest for a family chat

All names and details are fictional.

## The request

Wednesday, 19:40, in a family group chat:

> Anything I need to know for school?

## 1. Check the tool and the login

`command -v classcharts` finds it. No need to run `pupils` first: if setup hadn't been done, the next command would exit with code 2 and "No ClassCharts login found".

## 2. One call

A general check-in is what `digest` is for. Don't run `day`, `homework`, `announcements` and `behaviour` separately.

```bash
classcharts digest
```

```
Alex · Wednesday 2026-10-28

Next school day · Thursday 2026-10-29 · week 2
  08:30–15:00  Maths, English ×2, French, PE, Science

Homework to do (due by 2026-11-11)
  - [todo] due Tue 2026-10-27 · History: Source analysis worksheet (30 min, Mr B Teacher)
  - [todo] due Thu 2026-10-29 · French: Vocab test prep (20 min, Mme D Teacher)
  - [todo] due Mon 2026-11-02 · Art: Spellings and definitions (15 min, Miss C Teacher)

Detentions
  None.

Behaviour (last 7 days)
  4 positive (Commendation 3, Excellent Effort 1), 1 negative (C1 Low-level disruption 1)

Announcements (last 7 days)
  - Mon 2026-10-26 · Year 8 museum trip, 13 November [consent needed] (Mrs A Office) [1 attachment]
  - Fri 2026-10-23 · Head of School Bulletin (Mrs A Office) [2 attachments]

Attendance (this school year)
  98.6% (since August 98.6%), 1 absence
```

## 3. Read it

- **History is overdue.** It was due Tuesday and is still `[todo]`. That goes first. `[todo]` means nobody has ticked it off in ClassCharts, so it may have been handed in on paper. Say "still showing as not done", not "Alex didn't do it".
- **French is due tomorrow.** That's next.
- **The trip needs consent.** `[consent needed]` means a parent has to respond in ClassCharts. The agent can't. If the deadline matters, `announcements --full` would show the letter's full text and any reply-by date. Here the title is enough to flag it.
- **Behaviour:** four positives are worth a line of credit. One "C1" is reported as given, briefly, with no guess at what C1 means at this school and no comment.
- **Week 2** is the timetable rotation. It's useful context in a reply about tomorrow, not news.
- **Detentions "None"** and a normal attendance figure don't need mentioning unless asked.
- **Attachments:** name them if useful; don't fetch or post the signed links.

## 4. The reply

> Two bits for school:
> • History source-analysis worksheet was due Tuesday and still shows as not done in ClassCharts.
> • French vocab test prep is due tomorrow (Thursday).
> Also: the Year 8 museum trip on 13 Nov needs a parent's consent in the ClassCharts app.
> Good week otherwise: 3 commendations and an excellent-effort point. (One C1 for low-level disruption too.)
> Tomorrow is a normal day, 08:30–15:00, with PE.

Why this shape:
- Actions first, in date order: overdue, then tomorrow, then the consent request.
- The positive is celebrated; the negative is one factual bracket, not a talking-to.
- No table, no headings, no empty sections, no URLs.
- "Shows as not done in ClassCharts" keeps the `[todo]` meaning honest.
- PE is mentioned because a parent might need to pack a kit. That's a small judgement call. Leave it out if it isn't useful for your family.

## What a plain prompt tends to do instead

- Runs four or five separate commands instead of `digest`.
- Says "the teacher hasn't marked History as complete", treating the tick as a grade.
- Offers to "confirm consent for the trip", which the tool can't do.
- Explains what "C1" probably means, or adds advice about the disruption point.
- Lists every section, including "No detentions" and the attendance percentage, in a long formatted block.
