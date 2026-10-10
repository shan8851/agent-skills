# Building the tour GIF: variants and tuning

Load this when the user is on Windows PowerShell, doesn't have ImageMagick, or the GIF comes out too big.

## Why the concat list ends the way it does

ffmpeg's concat demuxer applies each `duration` to the `file` line above it, but it ignores the duration on the last entry. Listing the final frame once more with no duration makes the real last frame keep its full duration. So for N frames the list has N `file`/`duration` pairs, then one extra `file` line repeating frame N. Never repeat an earlier frame, and never leave a frame out.

Correct list for five frames:

```text
file 'screen-01.png'
duration 2.5
file 'screen-02.png'
duration 2.5
file 'screen-03.png'
duration 2.5
file 'screen-04.png'
duration 2.5
file 'screen-05.png'
duration 2.5
file 'screen-05.png'
```

## PowerShell (Windows)

Git Bash or WSL can run the bash snippets in `SKILL.md` as they are. In PowerShell:

```powershell
New-Item -ItemType Directory -Force .tmp/gif-frames | Out-Null
Get-ChildItem docs/screenshots/screen-*.png | ForEach-Object {
  magick $_.FullName -resize 800x -background white -gravity north -extent 800x500 ".tmp/gif-frames/$($_.Name)"
}
magick identify -format "%f %wx%h`n" .tmp/gif-frames/*.png

Set-Location .tmp/gif-frames
$frames = Get-ChildItem screen-*.png | Sort-Object Name
$lines = foreach ($f in $frames) { "file '$($f.Name)'"; 'duration 2.5' }
$lines += "file '$($frames[-1].Name)'"
Set-Content -Path list.txt -Value $lines -Encoding ascii
Get-Content list.txt

ffmpeg -y -f concat -safe 0 -i list.txt -vf "fps=10,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 ../../docs/screenshots/tour.gif
```

Write `list.txt` as ASCII (or UTF-8 without a BOM). A BOM at the start of the file can make ffmpeg fail to parse the first line.

## Resizing with ffmpeg only (no ImageMagick)

Scale to 800px wide, crop anything taller than 500px, and pad anything shorter, so every frame ends up 800×500:

```bash
for f in docs/screenshots/screen-*.png; do
  ffmpeg -y -loglevel error -i "$f" \
    -vf "scale=800:-2,crop=800:'min(ih,500)':0:0,pad=800:500:0:0:color=white" \
    ".tmp/gif-frames/$(basename "$f")"
done
```

Check sizes with:

```bash
for f in .tmp/gif-frames/*.png; do
  printf '%s ' "$f"; ffprobe -v error -show_entries stream=width,height -of csv=p=0 "$f"
done
```

## Making the GIF smaller

Try these in order, rebuilding and checking the size each time:

1. Fewer frames: drop the weakest one or two.
2. Lower frame rate: a slideshow doesn't need more than `fps=10`; `fps=5` also works.
3. Narrower frames: 640px wide instead of 800px (change both the resize and the `-extent`/`pad` size).
4. Fewer colours: `palettegen=max_colors=128` and `paletteuse=dither=bayer:bayer_scale=5`.
5. If it's still over about 2 MB, suggest an MP4 or WebM instead (`ffmpeg -f concat -safe 0 -i list.txt -vf fps=10 -pix_fmt yuv420p tour.mp4`). GitHub READMEs can embed a video uploaded through the web editor, but a GIF works everywhere.

## Timing

- 2–3 seconds per slide is enough to register a screen. Use longer only for dense screens.
- To give one slide longer, edit its `duration` line in `list.txt` after generating it.
