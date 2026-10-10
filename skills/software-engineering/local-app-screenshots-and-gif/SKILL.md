---
name: local-app-screenshots-and-gif
description: Capture consistent screenshots of a locally running web app and turn them into a looping tour GIF for a README, release notes or a social post, after checking every frame for personal or secret data. Use when the user says "take screenshots for the README", "make a demo GIF", "capture the app", "add a tour GIF", or wants images of their local app for docs or an announcement.
---

# Local App Screenshots and Tour GIF

Capture a handful of same-sized screenshots from an app running on the user's machine, check them for anything that shouldn't be public, and stitch them into a small looping GIF.

The job is **accurate, safe images**, not marketing. A good result is a set of screenshots that show the real app at a fixed size and contain nothing private, plus a GIF small enough to load quickly in a README.

## When to use

- "Take screenshots for the README", "make a demo GIF", "capture the app", "add a tour GIF to the docs".
- Refreshing out-of-date screenshots after a UI change.
- Images for release notes, a launch post or a project page.

Do not use when:
- the app isn't a web app you can open in a browser (native desktop or mobile apps need their own capture tools);
- the user wants a narrated video or a recording of real interaction (use a screen recorder; a slideshow GIF isn't that);
- the target is a remote production site with real user data. Ask before capturing anything from it.

## Requirements

- The app runs locally (dev server or built preview).
- Browser automation: Playwright, Puppeteer, or your agent's own browser tool.
- **ffmpeg** (required). Check with `ffmpeg -version`. If it's missing, tell the user how to install it for their OS and stop at the screenshots.
- **ImageMagick 7** (`magick`) for resizing. Check with `magick -version`. If it isn't installed, ffmpeg can do the resizing instead (see `references/gif-build.md`).

## Process

1. **Start the app.** Prefer the project's own scripts: read `package.json` (or the equivalent) and use its `dev`, `preview` or `start` script, e.g. `pnpm dev` or `npm run preview`. Fall back to a generic static server for a built folder only if the project has nothing. Note the URL and port, and confirm the page loads before going further.

2. **Agree the shot list.** Pick 4–8 pages or states that show what the app does. Ask the user if it isn't obvious. Skip settings, profile and admin pages unless the user specifically wants them (see step 4).

3. **Capture at a fixed viewport.** Use whatever browser automation you have, at one fixed viewport such as 1280×800, saving straight to the target folder (e.g. `docs/screenshots/`). With Playwright:

   ```js
   await page.setViewportSize({ width: 1280, height: 800 });
   await page.goto(url, { waitUntil: 'networkidle' });
   await page.screenshot({ path: 'docs/screenshots/screen-01.png', fullPage: false });
   ```

   Puppeteer has the same shape (`page.setViewport`, `page.screenshot({ path, fullPage: false })`). Wait for data and animations to settle before each shot. Name files in tour order: `screen-01.png`, `screen-02.png`, and so on. Keep `fullPage: false`: full-page captures come out at very different heights and spoil the GIF.

4. **Safety-check every screenshot.** Open each image and look for:
   - real names, email addresses, phone numbers, photos of real people;
   - API keys, tokens, passwords, connection strings;
   - private messages, notes or user content;
   - local file paths containing a username, internal hostnames or URLs;
   - settings pages showing sensitive defaults.

   Remove any screenshot that fails, or recapture it with seed or dummy data. Tell the user what you removed and why.

5. **Make same-sized frames.** Copy the approved screenshots into a scratch folder inside the project, such as `.tmp/gif-frames/`, rather than `/tmp` (which doesn't exist on Windows). Then make every frame exactly the same size:

   ```bash
   mkdir -p .tmp/gif-frames
   for f in docs/screenshots/screen-*.png; do
     magick "$f" -resize 800x -background white -gravity north -extent 800x500 ".tmp/gif-frames/$(basename "$f")"
   done
   magick identify -format "%f %wx%h\n" .tmp/gif-frames/*.png   # every line should say 800x500
   ```

   `-extent` crops or pads to the exact size, so a frame that came out a few pixels off still lines up. Without ImageMagick, check sizes with `ffprobe -v error -show_entries stream=width,height -of csv=p=0 <file>`.

6. **Build the concat list.** ffmpeg's concat demuxer needs a `duration` after **every** frame, then the **final frame listed once more with no duration**. Without that extra line ffmpeg ignores the last duration, and the last slide flashes past or disappears. Generate the list rather than typing it, so no frame is missed or repeated:

   ```bash
   cd .tmp/gif-frames
   : > list.txt
   for f in screen-*.png; do
     printf "file '%s'\nduration 2.5\n" "$f" >> list.txt
     last="$f"
   done
   printf "file '%s'\n" "$last" >> list.txt
   cat list.txt
   ```

   For five screenshots the list must read `screen-01` to `screen-05`, each followed by `duration 2.5`, then `file 'screen-05.png'` once more as the last line. Check it before going on.

7. **Encode the GIF** (still inside `.tmp/gif-frames`):

   ```bash
   ffmpeg -y -f concat -safe 0 -i list.txt \
     -vf "fps=10,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
     -loop 0 ../../docs/screenshots/tour.gif
   ```

   The palette pass gives much better colour than ffmpeg's default GIF encoding. `-loop 0` loops forever. For PowerShell, ffmpeg-only resizing and ways to shrink the file, see `references/gif-build.md`.

8. **Check the result.** Open the GIF and watch one full loop: every slide appears, in order, for about the same time, with no jump in size. Check the file size (aim for under 1–2 MB for a README). Then remove `.tmp/gif-frames/`, which only holds generated copies.

9. **Show the user.** Show the screenshots and the GIF, and suggest where to embed them (GIF near the top of the README, stills further down). Edit the README only if asked. Commit or push only when the user asks.

## Output format

Finish with a short summary:

```markdown
**Captured:** [n] screenshots at [width×height] in `[folder]`
**Removed for safety:** [file and reason], or none
**GIF:** `[path]`, [n] frames, [seconds] per frame, [size] KB
**Next:** [e.g. "Embed in the README?" / "Recapture the settings page with seed data?"]
```

## Common failure modes

- **Last slide missing or flashing past:** the concat list doesn't end with the final frame repeated without a duration, or one frame was listed twice and another left out. Generate the list; don't hand-write it.
- **Black bars or jumping frames:** frames are different sizes. Use a fixed viewport, `fullPage: false` and `-extent`, then check the sizes.
- **Half-loaded pages:** spinners and empty tables in the shots. Wait for network idle or a known element before capturing.
- **Leaking personal data:** a username in a file path, a real email in a form, a token on a settings screen. Step 4 is not optional.
- **Huge GIF:** too many frames, too wide, or too high a frame rate. 4–8 frames at 800px wide and 10 fps is usually plenty.
- **Writing outside the project:** `/tmp` paths fail on Windows and leave clutter elsewhere. Keep scratch files in `.tmp/` and remove them afterwards.
- **Pushing without asking:** making images is fine; committing and pushing them is the user's call.

## References

- `references/gif-build.md`: PowerShell versions of the frame and list steps, ffmpeg-only resizing, and options for shrinking a GIF.
