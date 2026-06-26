from langchain_community.tools import tool
from ddgs import DDGS
import requests
from bs4 import BeautifulSoup
import os 
from dotenv import load_dotenv
from rich import print
load_dotenv()

@tool
def search(query: str)->str:
    """
    Search the web for a query and return the results.
    """
    with DDGS() as ddgss:
        results = list(ddgss.text(query, max_results=5))
    
    out = [] 
    for result in results:
        out.append(f"[bold blue]{result['title']}[/bold blue]\n{result['body']}\n[link={result['href']}") 

    return "\n".join(out)  


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

# print(search.invoke({"query": "What is a rag?"}))

# print(scrape_url.invoke({"url": "https://www.ibm.com/think/topics/retrieval-augmented-generation"}))