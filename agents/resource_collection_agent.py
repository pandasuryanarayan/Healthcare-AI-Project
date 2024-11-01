import requests
import re

def collect_resources(use_cases):
    resources = []
    github_api_url = "https://api.github.com/search/repositories"
    github_token = "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"

    use_cases_string = "\n".join(use_cases)

    print("Use Case: ", use_cases)
    print("Use Case String: ", use_cases_string)

    # Extract headlines using regex
    headlines = re.findall(r'\*\*[\d]+\.\s(.*?)\:\*\*', use_cases_string)

    search_queries = [f"{headline.strip()}" for headline in headlines]

    print("Search Queries: ", search_queries)

    for case in search_queries:
        query = f"{case} dataset"  # Trim the query to fit length
        params = {"q": query, "sort": "stars", "order": "desc", "per_page": 5}
        
        headers = {
            "Authorization": f"Bearer {github_token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "Accept": "application/vnd.github+json",
        }

        response = requests.get(github_api_url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            for item in data["items"]:
                resources.append({
                    "title": item["name"] or "No title available",
                    "url": item["html_url"] or "No url available",
                    "description": item["description"] or "No description available",
                })
        else:
            print(f"Error fetching data from GitHub: {response.status_code} - {response.text}")
    
    print("resources: ",resources)

    # Create Markdown formatted output
    md_output = "# Collected Resources\n\n"
    for resource in resources:
        md_output += f"## [{resource['title']}]({resource['url']})\n"
        md_output += f"{resource['description']}\n\n"

    return md_output.strip()  # Ensure no trailing whitespace