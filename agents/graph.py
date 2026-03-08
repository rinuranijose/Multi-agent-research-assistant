from langgraph.graph import StateGraph
from typing import TypedDict

from agents.planner_agent import planner_agent
from agents.research_agent import research_agent


class AgentState(TypedDict):
    question: str
    plan: str
    search_result: str
    answer: str


builder = StateGraph(AgentState)

builder.add_node("planner", planner_agent)
builder.add_node("research", research_agent)

builder.set_entry_point("planner")

builder.add_edge("planner", "research")

builder.set_finish_point("research")

graph = builder.compile()