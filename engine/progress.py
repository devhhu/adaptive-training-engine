from __future__ import annotations

import json
from pathlib import Path

DEFAULT_PROGRESS = {
    "active_pack": "example_generic",
    "active_track": "core",
    "sessions_completed": 0,
}

def load_progress(path: Path) -> dict:
    if not path.exists():
        return DEFAULT_PROGRESS.copy()
    return json.loads(path.read_text())

def save_progress(path: Path, progress: dict) -> None:
    path.write_text(json.dumps(progress, indent=2, sort_keys=True))
