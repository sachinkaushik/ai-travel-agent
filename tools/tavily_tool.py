import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

_api_key = os.getenv("TAVILY_API_KEY")
client = TavilyClient(api_key=_api_key) if _api_key else None


def tavily_search(query: str) -> str:
    if client is None:
        return "Error: TAVILY_API_KEY is not set."

    try:
        response = client.search(query=query, max_results=5)
    except Exception as e:
        return f"Error searching hotels: {e}"

    results = []
    for i, r in enumerate(response.get("results", []), 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."
        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results) if results else "No hotel results found."

