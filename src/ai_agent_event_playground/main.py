"""Runnable entry point for the EventBot example agent.

Loads the API key, then runs a sample prompt through the agent defined in
``agent.py``. The model decides when to call the local Python tools.
"""

import asyncio

from dotenv import load_dotenv

from ai_agent_event_playground.agent import build_agent


async def _run(prompt: str) -> None:
    agent = build_agent()
    response = await agent.run(prompt)
    print(response.text)


def main() -> None:
    load_dotenv()
    prompt = (
        "I'm planning a birthday party on 2026-07-01. "
        "How many days away is it, and what should we do?"
    )
    asyncio.run(_run(prompt))


if __name__ == "__main__":
    main()
