from langchain_community.llms import Ollama
from mcp_client.client import search_web

llm = Ollama(model="phi3")

async def research_agent(state):

    plan = state["plan"]
    plan = plan.replace("Need to Search for:", "").strip()
    search_result = await search_web(plan)

    prompt = f"""
You are a research assistant.

Plan:
{plan}

Tool result:
{search_result}

Provide the final answer for the user.
"""

    answer = llm.invoke(prompt)
    #print("In research agent",answer,search_result,"Done")
    return {
        "answer": answer,
        "search_result": search_result
    }