# Search tips

## Terms

- Start with the most distinctive words: names, places, product names, numbers.
- Then broaden: synonyms ("car" → "vehicle", the model name, "MOT", "insurance"), related people, the folder the topic would live in.
- Try the user's likely phrasing, not yours. People write "the flat", not "accommodation".
- Case-insensitive search by default.

```bash
rg --files notes/ | rg -i "boiler|heating"
rg -n -i "boiler|heating|plumber" notes/
rg -n -i -C 3 "decided|going with|chose" notes/projects/kitchen.md
```

## Dates

- Prefer dates written in the note (headings, "Event date:"), then filename dates, then file times last.
- Relative dates in a note ("last week") are relative to that note's date, not today.
- If the user gives a rough time ("in the summer"), look at notes in that range first, then widen.

## Checking for something newer

- After finding a match, search the same terms again and look for anything dated later.
- Look for words that signal change: "changed my mind", "actually", "instead", "dropped", "on hold", "done".
- Dashboards, summaries and undated lists can be stale. Trust a dated entry over an undated summary.

## Conflicting sources

| Situation | What to say |
| --- | --- |
| Later note reverses an earlier one | Give the later answer; mention the earlier one and the date it changed. |
| Two notes disagree, no clear order | Say they conflict, quote both briefly with dates, don't pick. |
| Summary disagrees with a dated entry | Prefer the dated entry; flag the summary as possibly stale. |
| Only an idea, never a decision | Say it was considered, not decided. |

## Confidence

- **High:** an explicit, dated statement of the thing asked, with nothing newer.
- **Medium:** clear but indirect, or old with no later confirmation.
- **Low:** inferred from passing mentions, or sources conflict.

## Things to leave out of evidence searches

Agent instruction files, `.git/`, editor state (for example `.obsidian/`), templates and caches. They match lots of terms and aren't the user's record.
