---
name: local-app-screenshots-and-gif
description: Capture screenshots and generate a tour GIF from a locally running web app for README, announcements, or social posts.
---

# Local App Screenshots & Tour GIF

Capture screenshots from a locally running app and produce a polished tour GIF for READMEs, announcements, or social posts.

## Prerequisites

- App running locally (dev server or built preview)
- ImageMagick (`magick`) installed
- FFmpeg installed
- Browser automation tools available

## Step 1: Start the app

```bash
# If dev server
npm run dev  # or yarn dev, pnpm dev

# If built app, serve it
npm run build && npx serve -s dist -l 3000
```

Confirm the app loads in browser before proceeding. Note the port.

## Step 2: Capture screenshots

Navigate to each page and capture with browser vision tools. Copy the cached screenshot to your target directory:

```bash
mkdir -p /path/to/project/docs/screenshots  # or public/readme/
```

For each page:
1. Navigate to the URL
2. Wait 2 seconds for data/loading to settle
3. Capture screenshot
4. Copy from cache to your target dir

Rename files sequentially so the order is clear:

```bash
# Rename to generic ordered names
mv homepage.png    docs/screenshots/screen-01.png
mv dashboard.png   docs/screenshots/screen-02.png
mv settings.png    docs/screenshots/screen-03.png
mv reports.png     docs/screenshots/screen-04.png
mv profile.png     docs/screenshots/screen-05.png
```

**Pitfall:** Full-document-height screenshots can be very tall. A page that scrolls to 2500px will produce a 1280x2500 image. This matters for GIF consistency.

## Step 3: Content safety audit

Before publishing, check each screenshot for:
- Personal names, email addresses, phone numbers
- API keys, tokens, passwords
- Private chat content or user preferences
- Internal URLs that shouldn't be public
- Config/settings pages exposing sensitive defaults

Remove or skip any screenshots with sensitive content. For GIF frames, just exclude those pages entirely.

**Pitfall:** Settings and profile pages are the most common source of leaks — username in file paths, personal details in form fields, or internal service URLs in configuration displays.

## Step 4: Generate the tour GIF

The key insight: all frames must be the same dimensions or you get ugly padding.

```bash
# 1. Resize and crop each screenshot to a fixed viewport (e.g., 800x720)
mkdir -p /tmp/gif-frames
for f in screen-01.png screen-02.png screen-03.png screen-04.png screen-05.png; do
  magick "$f" -resize 800x -crop 800x720+0+0 +repage "/tmp/gif-frames/${f}"
done

# 2. Verify all frames are identical dimensions
for f in /tmp/gif-frames/*.png; do identify "$f" | awk '{print $1, $3}'; done

# 3. Create concat list with 2.5s per slide
cat > /tmp/gif-frames/list.txt << 'EOF'
file 'screen-01.png'
duration 2.5
file 'screen-02.png'
duration 2.5
file 'screen-03.png'
duration 2.5
file 'screen-04.png'
duration 2.5
file 'screen-04.png'
EOF

# 4. Build the GIF with ffmpeg (palette-based for quality)
ffmpeg -y -f concat -safe 0 -i /tmp/gif-frames/list.txt \
  -vf "fps=15,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
  -loop 0 \
  /path/to/project/public/readme/tour.gif
```

**Key flags:**
- `fps=15` — smooth enough, keeps file size down
- `scale=800:-1` — 800px wide, auto height (should be uniform from crop)
- `palettegen/paletteuse` — much better color quality than default GIF encoding
- `-loop 0` — infinite loop
- Last file listed twice without duration — prevents ffmpeg cutting the last frame

## Step 5: Commit and push

```bash
git add public/readme/
git commit -m "docs: add screenshots and tour GIF"
git push
```

## Tips

- Target 500KB-1MB for the GIF. Above 2MB is too heavy for README rendering.
- 6-8 pages is the sweet spot for a tour GIF. More gets tedious.
- 2-3 seconds per slide is enough for viewers to register the content.
- If the app has a sidebar, the cropped viewport view is usually more impactful than full-page since it looks like a real screen.
- Update the README to embed the GIF in a centered div at the top, individual screenshots in a grid below.
