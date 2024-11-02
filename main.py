from agents.industry_research_agent import research_industry
from agents.use_case_generation_agent import generate_use_cases
from agents.dataset_generation_agent import generate_datasets
from agents.md_to_text import extract_datasets_from_md
from agents.resource_collection_agent import collect_resources

def main():
    industry = "Healthcare"
    insights = research_industry(industry)
    print(f"Insights Gathered for {industry}.")

    # Save insights to insights.md
    with open('data/insights.md', 'w') as f:
        f.write("# Insights on Suggested Industry\n\n")
        for insight in insights:
            f.write(f"{insight}\n")
    
    use_cases = generate_use_cases(insights)
    print("Use Case Generated on Insights.")

    # Save use cases to use_cases.md
    with open('data/use_cases.md', 'w') as f:
        f.write("# Collected Use Cases on Insights\n\n")
        for case in use_cases:
            f.write(f"{case}\n")
    
    datasets = generate_datasets(use_cases)
    print("Datasets Generated for Use Cases.", datasets)

    # Save datasets to datasets.md
    with open('data/datasets.md', 'w') as f:
        f.write("# Datasets Suggestions based On Use Cases\n\n")
        for dataset in datasets:
            f.write(f"{dataset}\n")
    
    extract_datasets_from_md("data/datasets.md","data/datasets_md_text.txt")
    print("Extracted Datasets from MD to TEXT.")

    collect_resources()
    print("Resource Collected.")

if __name__ == "__main__":
    main()
