# Worked Example

A fictional example. The user has a voice profile (kept outside the skill) with these relevant rules: opens with the point, short paragraphs, contractions, dry humour, no false contrasts, uses numbers as digits, never ends with a rallying call.

## Brief

> Write a short post for my team channel saying we've moved this week's deploy freeze from Thursday to Friday, because Monday's a public holiday. Usual rule: nothing merges to main after 17:00 unless it's a fix with someone on call. Keep it light.

Format: chat post. Audience: own team. Goal: everyone knows the new freeze day. Length: under 80 words.

## First AI draft (the kind to avoid)

> 📢 Important Update: Deploy Freeze Schedule Change
>
> In order to accommodate the upcoming public holiday, we're excited to share that the deploy freeze will now take place on Friday rather than Thursday. This isn't just a date change — it's about giving everyone the breathing room they need. Let's keep shipping great things together! 🚀

## Draft in voice (after the critic pass)

> Deploy freeze moves to Friday this week, not Thursday. Monday's a public holiday, so we're giving ourselves one more day to land things.
>
> Same rules as usual: nothing merges to main after 17:00 Friday unless it's a fix and someone's on call to watch it.
>
> If that breaks a plan you had, shout today rather than Friday at 16:58.

## Critic note

```markdown
**Round 1: Good**
- Weak: v1 opened with "Just a heads-up:" (preamble; profile says open with the point).
- Weak: "Same rules as usual" assumes everyone knows the rules; fine for this team, would need a link for a wider channel.
- Checked: no banned phrases, no false contrast, under 80 words.
- Fixed: cut the preamble.

**Round 2: Excellent**
- Remaining weakness: "16:58" is a joke that only lands if people have done exactly that; keep it if that's true of this team.
```

## What changed and why

- Opened with the fact, not an announcement header.
- Cut the emoji, the "excited to share", the false contrast and the rallying ending.
- Kept one dry line, because the profile's samples use one.
- Every fact (days, holiday, 17:00 rule) came from the brief. If the cut-off time hadn't been given, the draft would say `[cut-off time]` rather than invent one.
