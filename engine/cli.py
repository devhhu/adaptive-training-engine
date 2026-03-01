from __future__ import annotations

from pathlib import Path

from .ui import clear, header, card, pause, menu, MenuItem
from .progress import load_progress, save_progress
from .pack_loader import load_pack
from .agent import run_agent
from .artifacts import save_artifact

ROOT = Path(__file__).resolve().parents[1]
PACKS_DIR = ROOT / "packs"
LAB_DIR = ROOT / "lab"
PROGRESS_PATH = ROOT / "progress.json"

def main():
    progress = load_progress(PROGRESS_PATH)
    save_progress(PROGRESS_PATH, progress)

    pack_slug = progress["active_pack"]
    pack_dir = PACKS_DIR / pack_slug
    pack = load_pack(pack_dir)
    meta = pack["meta"]

    history = None

    items = [
        MenuItem("1", "Quick Drill", "One question at a time"),
        MenuItem("2", "Scenario", "Stage-based with constraints"),
        MenuItem("3", "Switch Track", "Change active track"),
        MenuItem("4", "Switch Pack", "Choose a different pack"),
        MenuItem("0", "Exit", ""),
    ]

    while True:
        clear()
        header("Adaptive Training Engine", f"Pack: {meta['slug']} | Track: {progress['active_track']}")
        choice = menu("Main Menu", items, default="1")

        if choice == "0":
            break

        if choice == "3":
            tracks = list(meta["tracks"].keys())
            md = "## Tracks\\n" + "\\n".join([f"- **{t}**: {meta['tracks'][t]['description']}" for t in tracks])
            card(md, title="Tracks")
            new_track = input("\\nSet active track: ").strip() or progress["active_track"]
            if new_track in meta["tracks"]:
                progress["active_track"] = new_track
                save_progress(PROGRESS_PATH, progress)
            continue

        if choice == "4":
            available = [p.name for p in PACKS_DIR.iterdir() if p.is_dir()]
            card("## Packs\\n" + "\\n".join([f"- {p}" for p in sorted(available)]), title="Packs")
            new_pack = input("\\nSet active pack: ").strip() or progress["active_pack"]
            if (PACKS_DIR / new_pack).exists():
                progress["active_pack"] = new_pack
                progress["active_track"] = "core"
                save_progress(PROGRESS_PATH, progress)
                pack_slug = new_pack
                pack_dir = PACKS_DIR / pack_slug
                pack = load_pack(pack_dir)
                meta = pack["meta"]
            continue

        if choice == "1":
            prompt = (
                "Create a short drill. Ask ONE question at a time, wait for my answer, then score 1-5 with brief feedback. "
                f"Use track='{progress['active_track']}'. End after 6 questions with 3 takeaways."
            )
            history, text = run_agent(prompt, history)
            card(text, title="Drill")
            p = save_artifact(LAB_DIR / "drills", "drill", meta["slug"], text)
            card(f"Saved: `{p}`", title="Artifact", border="green")
            progress["sessions_completed"] += 1
            save_progress(PROGRESS_PATH, progress)
            pause()
            continue

        if choice == "2":
            prompt = (
                "Run a 3-stage scenario with ambiguity. After each stage, ask me for next steps, then score. "
                f"Use a constraints ladder. Track='{progress['active_track']}'. "
                "End with: 'What would you change to prevent this?'"
            )
            history, text = run_agent(prompt, history)
            card(text, title="Scenario")
            p = save_artifact(LAB_DIR / "scenarios", "scenario", meta["slug"], text)
            card(f"Saved: `{p}`", title="Artifact", border="green")
            progress["sessions_completed"] += 1
            save_progress(PROGRESS_PATH, progress)
            pause()
            continue

if __name__ == "__main__":
    main()
