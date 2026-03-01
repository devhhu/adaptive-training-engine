from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.text import Text

console = Console()

def clear() -> None:
    console.clear()

def header(title: str, subtitle: str | None = None) -> None:
    t = Text(title, justify="center", style="bold")
    console.print(Panel(subtitle or "", title=t, border_style="cyan"))

def card(md: str, title: str = "Coach", border: str = "cyan") -> None:
    md = (md or "").strip()
    if not md:
        return
    console.print(Panel(Markdown(md, code_theme="monokai"), title=title, border_style=border))

def pause(msg: str = "Press Enter to continue...") -> None:
    try:
        input(f"\n  {msg}")
    except KeyboardInterrupt:
        pass

@dataclass(frozen=True)
class MenuItem:
    key: str
    label: str
    desc: str = ""

def menu(title: str, items: Sequence[MenuItem], default: str = "1") -> str:
    table = Table(title=title, header_style="bold cyan")
    table.add_column("Key", style="bold cyan", width=5)
    table.add_column("Action")
    table.add_column("Notes", style="dim")
    for it in items:
        table.add_row(it.key, it.label, it.desc)
    console.print(table)
    return Prompt.ask("\nSelect", default=default).strip()
