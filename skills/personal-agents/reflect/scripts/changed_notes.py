"""List notes that are new or changed since the last reflection. Optional helper.

Read-only for notes: it only writes its own small state file.
Python 3.9+, standard library only.

  python changed_notes.py scan --notes notes/            # what changed since last checkpoint
  python changed_notes.py scan --notes notes/ --full     # treat every note as new
  python changed_notes.py checkpoint --notes notes/      # mark the scanned versions as reflected on

Fingerprints (SHA-256) catch edits to old notes, which dates and file times miss.
A file edited after the scan stays pending for next time.
"""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

SKIP_DIRS = {".git", ".obsidian", ".reflect", "templates", "node_modules"}


def fingerprints(notes):
    found = {}
    for path in sorted(notes.rglob("*.md")):
        rel = path.relative_to(notes)
        if SKIP_DIRS.intersection(rel.parts) or path.is_symlink():
            continue
        found[rel.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return found


def load(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default
    except (ValueError, OSError):
        print(f"{path.name} is unreadable; starting fresh (notes are unaffected).")
        return default


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=("scan", "checkpoint"))
    parser.add_argument("--notes", type=Path, required=True, help="notes folder")
    parser.add_argument("--state", type=Path, help="state folder (default: <notes>/.reflect)")
    parser.add_argument("--full", action="store_true", help="scan: ignore the last checkpoint")
    args = parser.parse_args()

    notes = args.notes.resolve()
    if not notes.is_dir():
        parser.error(f"Not a folder: {notes}")
    state_dir = (args.state or notes / ".reflect").resolve()
    state_file, pending_file = state_dir / "state.json", state_dir / "pending.json"
    state = load(state_file, {"last_checkpoint": None, "files": {}})
    current = fingerprints(notes)

    if args.command == "scan":
        seen = {} if args.full else state["files"]
        changed = {p: h for p, h in current.items() if seen.get(p) != h}
        removed = sorted(set(seen) - set(current))
        save(pending_file, {"full": args.full, "files": changed})
        print(json.dumps({
            "last_checkpoint": state["last_checkpoint"],
            "new_or_changed": sorted(changed),
            "removed": removed,
        }, indent=2))
        return

    pending = load(pending_file, None)
    if pending is None:
        parser.error("Run scan first.")
    files = {} if pending["full"] else {p: h for p, h in state["files"].items() if p in current}
    done = {p: h for p, h in pending["files"].items() if current.get(p) == h}
    files.update(done)
    save(state_file, {"last_checkpoint": datetime.now(timezone.utc).isoformat(timespec="seconds"), "files": files})
    pending_file.unlink()
    still = sorted(p for p, h in current.items() if files.get(p) != h)
    print(json.dumps({"checkpointed": len(done), "still_pending": still}, indent=2))


if __name__ == "__main__":
    main()
