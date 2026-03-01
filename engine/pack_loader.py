from __future__ import annotations

from pathlib import Path
import yaml

def load_pack(pack_dir: Path) -> dict:
    meta = yaml.safe_load((pack_dir / "pack.yaml").read_text())
    drills = yaml.safe_load((pack_dir / "drills.yaml").read_text())
    scenarios = yaml.safe_load((pack_dir / "scenarios.yaml").read_text())
    rubrics = yaml.safe_load((pack_dir / "rubrics.yaml").read_text())
    return {"meta": meta, "drills": drills, "scenarios": scenarios, "rubrics": rubrics}
