from langchain_community.llms import Ollama

llm = Ollama(model="phi3")

def planner_agent(state):

    question = state["question"]

    prompt = f"""
     
     You are a planner agent.

Your job is to convert the user's question into a database search query.
IMPORTANT RULES:
- If you use SEARCH_DB, you MUST use the user's question EXACTLY as the query.
- Do not change or add anything in the user query, keep it as it is.
- Do NOT modify, summarize, or shorten the question.
- Output only ONE line.
- No explanation.

User question:
{question}

Return format:
Need to Search for: <search query>
"""
    plan = llm.invoke(prompt)
    plan = plan.split("\n")[0]

    #print("In planner",plan,"Done")
    return {
        "plan": plan
    }