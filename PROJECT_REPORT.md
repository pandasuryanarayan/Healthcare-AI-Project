# Project Report: Market Research & Use Case Generation Agent for Generative AI

## 1. Introduction
This project, **Market Research & Use Case Generation Agent for Generative AI**, aims to generate AI use cases specifically for the healthcare industry. Utilizing a multi-agent architecture, this system focuses on creating relevant AI datasets and insights for healthcare institutions.

### Objectives
- Conduct market research for targeted insights.
- Generate specific AI use cases based on industry trends.
- Identify suitable datasets from Hugging Face for each use case.

## 2. Methodology
### System Architecture
The architecture consists of five agents, each with distinct roles. Below is an overview of each agent:

- **Industry Research Agent**: Uses Tavily API to fetch healthcare trends.
- **Use Case Generation Agent**: Generates healthcare-specific AI use cases using Google Gemini based on insights.
- **Dataset Generation Agent**: Generates dataset keywords from use cases.
- **MD to Text Module**: Converts datasets from Markdown to plain text for easy integration.
- **Resource Collection Agent**: Searches and matches datasets from Hugging Face using fuzzy matching.

### Data Flow
1. **main.py** coordinates agent activities.
2. **Industry Research Agent** gathers insights, stored in `insights.md`.
3. **Use Case Generation Agent** produces relevant AI use cases, saved in `use_cases.md`.
4. **Dataset Generation Agent** creates keywords, saved to `datasets.md`.
5. **MD to Text Module** extracts datasets to text in `datasets_md_text.txt`.
6. **Resource Collection Agent** matches datasets on Hugging Face and saves results to `huggingface_datasets.txt`.

## 3. Results
### Industry Insights

### Generated AI Use Cases

### Dataset Matching and Collection
The fuzzy matching retrieved relevant datasets. For instance:
- **Dataset Match**: "healthcare-ai-diagnosis" (score: 85%) on Hugging Face.

## 4. Conclusion
The multi-agent architecture successfully generated industry-specific AI use cases and identified relevant datasets. However, fuzzy matching occasionally yielded non-relevant datasets due to low keyword overlap. Future work includes improving dataset matching criteria.

### Limitations
- **Dataset Accuracy**: Matching scores varied, affecting relevance.
- **Industry Scope**: Insights may be general and not fully healthcare-specific.