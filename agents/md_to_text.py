import re

def extract_datasets_from_md(md_file_path, output_file):

    # Read the content from the Markdown file
    with open(md_file_path, 'r') as file:
        md_content = file.read()

    # Use a regex pattern to find all dataset lists
    pattern = r'\[(.*?)\]'
    datasets = []

    # Find all matches in the Markdown content
    matches = re.findall(pattern, md_content, re.DOTALL)

    for match in matches:
        # Split the datasets by commas and strip whitespace
        datasets.extend([dataset.strip().strip('"') for dataset in match.split(',')])

    # Write the datasets to the output file
    with open(output_file, 'w') as f:
        for dataset in datasets:
            f.write(f"{dataset}\n")

    # Read the datasets back from the file to remove duplicates
    with open(output_file, 'r') as f:
        unique_datasets = set(f.read().splitlines())

    # Write the unique datasets back to the output file
    with open(output_file, 'w') as f:
        for dataset in sorted(unique_datasets):  # Sort if needed
            f.write(f"{dataset}\n")

    print("Extracted Datasets from MD to TEXT.")
    print("Datasets are saved to datasets_md_text.txt")