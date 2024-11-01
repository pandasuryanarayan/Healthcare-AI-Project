from agents.industry_research_agent import research_industry
from agents.use_case_generation_agent import generate_use_cases
from agents.resource_collection_agent import collect_resources

def main():
    industry = "Healthcare"
    insights = research_industry(industry)
    
    use_cases = generate_use_cases(insights)
    
    resources = collect_resources(use_cases)
    
    with open('data/use_cases.md', 'w') as f:
        for case in use_cases:
            f.write(f"- {case}\n")
    
    with open('data/resources.md', 'w') as f:
        for resource in resources:
            f.write(f"{resource}")

if __name__ == "__main__":
    main()
