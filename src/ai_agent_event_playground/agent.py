"""EventBot agent definition: its model, tools, and constructor.

Built on the Microsoft Agent Framework + OpenAI. The runnable entry point
lives in ``main.py``.
"""

from datetime import date
from typing import Annotated

from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient

MODEL = "gpt-5.4-nano"


def days_until(
    event_date: Annotated[str, "The event date in YYYY-MM-DD format."],
) -> str:
    """Count the days from today until the given event date."""
    delta = (date.fromisoformat(event_date) - date.today()).days
    if delta > 0:
        return f"{delta} day(s) until {event_date}."
    if delta == 0:
        return f"{event_date} is today!"
    return f"{event_date} was {-delta} day(s) ago."


def suggest_activities(
    event_type: Annotated[str, "Kind of event, e.g. 'birthday', 'conference', 'wedding'."],
) -> str:
    """Suggest a few activities suited to the given type of event."""
    ideas = {
        "birthday": "cake tasting, a photo booth, and a group game",
        "conference": "lightning talks, a networking lunch, and a Q&A panel",
        "wedding": "a first dance, toasts, and a live band",
    }
    return ideas.get(event_type.lower(), "an icebreaker, food stalls, and music")


def build_agent(*, api_key: str | None = None) -> Agent:
    """Construct EventBot.

    Pass ``api_key`` to construct without touching the environment (handy for
    tests); otherwise the OpenAI client reads ``OPENAI_API_KEY`` from the env.
    """
    client = OpenAIChatClient(MODEL, api_key=api_key)
    return Agent(
        client,
        instructions=(
            "You are EventBot, a concise event-planning assistant. "
            "Use the available tools to answer questions about timing and activities."
        ),
        name="EventBot",
        tools=[days_until, suggest_activities],
    )
