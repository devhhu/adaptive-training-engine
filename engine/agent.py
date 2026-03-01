from __future__ import annotations

import os
from typing import Optional, Tuple, List

def run_agent(prompt: str, history: Optional[List[dict]] = None) -> Tuple[List[dict], str]:
    """
    Template agent. Provider-agnostic.

    - If LLM_API_KEY is NOT set -> offline demo mode.
    - Users can replace this file or extend it with providers.
    """
    if history is None:
        history = []
    history.append({"role": "user", "content": prompt})

    if not os.getenv("LLM_API_KEY"):
        text = (
            "### Offline Demo Mode\n"
            "Set `LLM_API_KEY` (and implement your provider) to generate real sessions.\n\n"
            "**Prompt received:**\n"
            f"```\n{prompt[:800]}\n```\n"
            "\n**Next:** replace `engine/agent.py` with your Anthropic/OpenAI provider.\n"
        )
        history.append({"role": "assistant", "content": text})
        return history, text

    text = "LLM integration is not implemented in this template. See docs to add a provider."
    history.append({"role": "assistant", "content": text})
    return history, text
