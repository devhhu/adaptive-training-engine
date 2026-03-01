from __future__ import annotations

from datetime import date
from pathlib import Path

def save_artifact(out_dir: Path, kind: str, slug: str, content: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = f"{date.today().isoformat()}_{kind}_{slug}.md"
    path = out_dir / fname
    path.write_text(content)
    return path
