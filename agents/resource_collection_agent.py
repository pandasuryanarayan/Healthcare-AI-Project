from huggingface_hub import HfApi
from fuzzywuzzy import fuzz
from dotenv import load_dotenv
import os

def collect_resources():
    load_dotenv()

    # Fetch Hugging Face API token from environment variables
    api_token = os.getenv('HUGGINGFACE_TOKEN')

    # Initialize the Hugging Face API
    api = HfApi("https://huggingface.co", api_token)

    # Load your local datasets file
    with open('data/datasets_md_text.txt', 'r') as f:
        local_datasets = [line.strip() for line in f.readlines()]

    # Function to search datasets on Hugging Face
    def search_datasets(query):
        datasets = api.list_datasets(search=query)
        return datasets

    # Search for matching datasets using fuzzy matching
    matching_datasets = []

    # Comparison Entries
    matching_datasets_comparison_results = []

    for local_dataset in local_datasets:
        matching_datasets_comparison_results.append(f"Searching for: {local_dataset}\n")
        datasets = search_datasets(local_dataset)

        if not datasets:
            matching_datasets_comparison_results.append("No datasets found.\n")
        
        for dataset in datasets:
            dataset_name = dataset.id  # Get the dataset name
            score = fuzz.partial_ratio(local_dataset, dataset_name)
            matching_datasets_comparison_results.append(f"Comparing with: {dataset_name}, Score: {score}\n")

            if score > 30:  # Adjust the score threshold as needed
                matching_datasets.append({
                    "name": dataset.author,
                    "url": f"https://huggingface.co/datasets/{dataset.id}"
                })

    # Print the matching datasets and their URLs or Statement
    
    if matching_datasets:
        # for dataset in matching_datasets:
        #     print(f"Name: {dataset['name']}, URL: {dataset['url']}")
        print("Dataset found in Hugging Face... Collecting datasets...")
    else:
        print("No matching datasets found.")

    # Save all Comparison Entries to a file
    with open('data/matching_datasets_comaparison_results.txt', 'w') as dataset_comparison_file:
        dataset_comparison_file.writelines(matching_datasets_comparison_results)

    # Save the matching datasets to a file
    with open('data/huggingface_datasets.txt', 'w') as output_file:
        if matching_datasets:
            for dataset in matching_datasets:
                output_file.write(f"Name: {dataset['name']}, URL: {dataset['url']}\n")
        else:
            output_file.write("No matching datasets found.\n")

    print(f"Matching datasets saved to huggingface_datasets.txt")
    print("Resource Collected.")