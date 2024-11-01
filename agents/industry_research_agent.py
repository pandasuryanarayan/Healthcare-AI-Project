from tavily import TavilyClient
client = TavilyClient(api_key="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")

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