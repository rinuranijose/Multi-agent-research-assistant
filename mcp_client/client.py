
from fastmcp import Client

client = Client("http://localhost:8001/mcp")


async def search_web(query):

    async with client:
        result = await client.call_tool(
            "web_search",
            {"query": query}
        )
    print(result)
    return str(result)