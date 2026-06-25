from langchain_community.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = list(ddgs.text("Latest AI news", max_results=5))

print(results)
@tool
def search(query: str)->str:
    """
    Search the web for a query and return the results.
    """
    search_tool = DuckDuckGoSearchRun()
    return search_tool.run(query)


print(search.invoke({"query": "What is the capital of France?"}))