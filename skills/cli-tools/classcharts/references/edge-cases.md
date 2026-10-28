# Edge cases

Short cases for what goes wrong most often. All names and details are fictional.

## 1. Not installed

`command -v classcharts` prints nothing.

Don't install it unprompted. Ask:

> ClassCharts isn't set up on this machine yet. Want me to install it? It's `npm install -g @shan8851/classcharts-agent` and needs Node.js 22.18 or later. After that, you'll need to sign in once yourself.

If `node --version` is older than 22.18, say so. Don't try to work around it.

## 2. Installed, but nobody has signed in

`classcharts pupils` exits with code 2:

```
No ClassCharts login found. A person needs to run `classcharts setup` once (or set CLASSCHARTS_EMAIL and CLASSCHARTS_PASSWORD).
```

Tell the user:

> You need to sign in once. In a terminal on this machine, run `classcharts setup` and enter your ClassCharts parent email and password when it asks. The password stays on this machine. Please don't send it to me here.

If they paste the password into chat anyway, don't use it. Tell them to run `setup` themselves, and suggest changing the password because it's now in the chat history.

## 3. Rate-limited login

Exit code 2:

```
ClassCharts sent the login back to its sign-in page. Usually that's too many attempts (wait a few minutes, don't retry in a loop); otherwise the email or password is wrong.
```

Don't retry straight away and don't loop. Answer:

> ClassCharts is temporarily blocking sign-ins (too many attempts). I'll need to wait a few minutes before trying again.

If it fails the same way after a real wait (five minutes or more), the saved details are probably wrong. Suggest re-running `classcharts setup`.

## 4. More than one child

`classcharts pupils` lists two children, Alex and Sam. The question is "what homework is outstanding?" with no name.

Run `homework --todo --pupil Alex` and `homework --todo --pupil Sam`, then answer per child with a short line each. If the question names one child, use `--pupil` for that child only. If a name doesn't match, `pupils` shows the exact names to use.

## 5. Holiday or INSET day

"Is there school tomorrow?" `day tomorrow` returns:

```
Monday 2026-11-02
  No lessons (weekend, holiday or INSET day).
```

Answer with what the tool knows:

> ClassCharts shows no lessons tomorrow, so it looks like a holiday or INSET day. The next day with lessons is Tuesday 3 November.

Get the second part from `day next`. Don't say the school is closed for a strike, weather or anything else unless an announcement says so. If the parent is unsure, `announcements` may have the reason.

## 6. The school hides a section

"How's attendance?" returns:

```
Alex's school doesn't show attendance in ClassCharts.
```

(`{"hiddenBySchool": "attendance"}` with `--json`.) This is the school's choice in ClassCharts, not a broken login. Say so in one line and suggest asking the school office. Don't retry.

## 7. A request to write

"Can you tick off the French homework?" or "Give consent for the trip."

> I can only read ClassCharts, not change anything. You can tick it off (or give consent) in the ClassCharts app.

Don't look for a workaround, and don't claim it's done.

## 8. A bad behaviour week

`behaviour` returns:

```
0 positive, 3 negative (C2 Disruption 2, Late to lesson 1)
- Mon 2026-10-26 · C2 Disruption -1 (Maths)
- Tue 2026-10-27 · C2 Disruption -1 (Maths)
- Thu 2026-10-29 · Late to lesson -1 (Science)
```

In a family chat:

> Behaviour this week: 3 negative points (two "C2 Disruption" in Maths, one late to Science). No positives logged this week.

Factual, short, no guess at what "C2" means at this school, no advice and no tone. If there's an upcoming detention, add it with the date and time. The parents decide what to do.

## 9. Overdue items in an ordinary question

"What's due this week?" `week` shows two items due this week, and `[todo]` homework from last week appears in `digest` or `homework --todo`. If you've seen overdue `[todo]` items, mention them first, even though they weren't asked about. They're usually what the parent most needs to know.

## 10. Attachments

`homework --full --json` includes `attachments[].url`. These links are signed and expire. In a chat, name the file and say it's in ClassCharts. Don't paste the URL. If the user is working with you directly and needs the file, fetch it promptly and don't store the link.
