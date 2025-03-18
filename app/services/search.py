import os
from app.core.dependencies import get_serpapi_client

# Get SerpAPI client
client_serpapi = get_serpapi_client()

def get_search_result(query):
    """Perform web search to answer questions about current events, people, or general knowledge"""
    r = client_serpapi.search({
        "q": query,
        "engine": "google",
    })

    results = ''
    for res in r['organic_results']:
        results += res['snippet'] + '\n'

    return results