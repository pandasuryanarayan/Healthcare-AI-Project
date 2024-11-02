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
    for local_dataset in local_datasets:
        print(f"Searching for: {local_dataset}")  # Debug statement
        datasets = search_datasets(local_dataset)

        if not datasets:
            print("No datasets found.")  # Debug statement
        
        for dataset in datasets:
            dataset_name = dataset.id  # Get the dataset name
            print("resource dataset name:\n", dataset_name)
            score = fuzz.partial_ratio(local_dataset, dataset_name)
            print(f"Comparing with: {dataset_name}, Score: {score}")  # Debug statement

            if score > 30:  # Adjust the score threshold as needed
                matching_datasets.append({
                    "name": dataset.author,
                    "url": f"https://huggingface.co/datasets/{dataset.id}"
                })

    # Print the matching datasets and their URLs
    if matching_datasets:
        for dataset in matching_datasets:
            print(f"Name: {dataset['name']}, URL: {dataset['url']}")
    else:
        print("No matching datasets found.")