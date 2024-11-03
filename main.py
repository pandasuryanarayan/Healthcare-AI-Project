from agents.industry_research_agent import research_industry
from agents.use_case_generation_agent import generate_use_cases
from agents.dataset_generation_agent import generate_datasets
from agents.md_to_text import extract_datasets_from_md
from agents.resource_collection_agent import collect_resources

def main():
    suggested_industries = "Healthcare, Automotive, Finance, Retail"
    industry = input(f"Enter industry (Suggested industries: {suggested_industries}): ")

    insights = research_industry(industry)
    
    use_cases = generate_use_cases(insights)
    
    generate_datasets(use_cases)
    
    extract_datasets_from_md("data/datasets.md","data/datasets_md_text.txt")

    collect_resources()

    # ANSI escape code for bold text
    BOLD = "\033[1m"
    RESET = "\033[0m"
    YELLOW = "\033[33m"

    print(f"{YELLOW}{BOLD}Please note that the results may not be specific to the selected industry. We recommend reviewing the datasets for more relevant insights.{RESET}")

if __name__ == "__main__":
    main()
