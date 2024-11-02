from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv('TAVILYCLIENT_API_KEY')
client = TavilyClient(api_key=api_key)

def research_industry(industry):
    search_query = f"{industry} healthcare trends 2023"
    results = client.search(search_query)

    insights = []
    for result in results['results']:
        insights.append({
            'title': result['title'],
            'url': result['url'],
            'content': result['content']
        })

    return insights