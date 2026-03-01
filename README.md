# Adaptive Training Engine (Template)

A **pack-driven training engine** that helps you build a personalised practice loop for **anything** — technical or not — and keep it all in your terminal.

> practice → feedback → iterate → save proof

This repo is intentionally **generic**. It gives you the *framework* (packs + tracks + artifacts + CLI UX).  
You bring the subject. You decide what “good” means. The engine helps you run the loop consistently.

---

## What this gives you (in plain terms)

If you’ve ever tried to “get better” at something and drifted after a week, this is the fix:

- A **structured loop** you can actually stick to (drills + scenarios)
- A **pack system (YAML)** so you can swap subjects and restructure fast
- A **track system** so you can focus (e.g., fundamentals vs deep dive vs interview mode)
- **Local artifacts** so your practice leaves a trail (notes, outputs, summaries)
- A clean terminal UI (no wall-of-text), with offline demo mode by default

It’s basically a **personal training gym**, but configurable, and built for deliberate practice.

---

## Why this is useful

Most learning fails for boring reasons:
- no repeatable structure
- no feedback loop you trust
- no record of what you did
- too hard to iterate once you start

This template makes iteration cheap:
- change the pack, not the code
- run sessions, save outputs, tweak, repeat

---

## Template features

### Terminal UX
- Menu-driven flows (drills, scenarios, switching tracks/packs)
- Pretty markdown “cards” (readable output)
- Offline demo behavior by default (no provider configured)

### Packs (YAML)
Define training content without editing Python:
- tracks (focus modes)
- modules (topic groupings)
- drill/scenario shapes
- rubrics (scoring anchors)

Start by copying `packs/example_generic`.

### Local artifacts (private by default)
Outputs are written to `lab/` and **gitignored**:
- sessions
- notes
- summaries
- artifacts

So you can practice freely without leaking anything.

---

## Repository layout

```text
engine/                 # generic engine code
  cli.py                # menu + orchestration
  ui.py                 # rich terminal UI
  progress.py           # local progress state (json)
  pack_loader.py        # reads YAML packs
  artifacts.py          # writes outputs to lab/
  agent.py              # provider hook (implement your LLM here)
packs/
  example_generic/      # sample pack (toy)
    pack.yaml           # tracks/modules/topics
    drills.yaml         # drill specs
    scenarios.yaml      # scenario specs
    rubrics.yaml        # scoring anchors
lab/                    # outputs (gitignored)
scripts/
  run.sh                # runner + venv + deps