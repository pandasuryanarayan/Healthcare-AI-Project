import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the API key
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

def generate_datasets(use_cases):
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Construct the prompt to generate dataset keywords
    prompt = (
        "Based on the following AI use cases, provide an array of datasets from Hugging Face associated with each specific use case "
        "in the following format:\n\n"
        "1. Use Case Title\n\n"
        "[\n"
        '    "Dataset 1",\n'
        '    "Dataset 2",\n'
        '    "Dataset 3",\n'
        "    ...\n"
        "]\n\n"
        "Respond with just the datasets name available in Hugging Face specifically, without additional descriptions ():\n"
    )
    for case in use_cases:
        prompt += f"- {case.strip()}\n"
    
    # Generate dataset keywords using Gemini
    response = model.generate_content(prompt)
    datasets = response.text.strip().split("\n")
    
    # Save datasets to datasets.md
    with open('data/datasets.md', 'w') as f:
        f.write("# Datasets Suggestions based On Use Cases\n\n")
        for dataset in datasets:
            f.write(f"{dataset}\n")

    print("Datasets Generated for Use Cases.")
    print("Datasets saved to datasets.md")
