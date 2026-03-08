from fastmcp import FastMCP

mcp = FastMCP("ResearchTools")

# Mock search database
MOCK_DATA = {
    "capital of france": "The capital of France is Paris.",
    "capital of india": "The capital of India is New Delhi.",
    "population of india": "1.47 billion.",
    }

@mcp.tool()
def web_search(query: str) -> str:
    """
    Mock web search tool.
    """
    print("QUERY RECEIVED:", query)
    query = query.lower()

    for key in MOCK_DATA:
        if key in query:
            print("Ans is there in DB",MOCK_DATA[key])
            return MOCK_DATA[key]

    return "No search results found."

if __name__ == "__main__":
    mcp.run(transport="http", port=8001)