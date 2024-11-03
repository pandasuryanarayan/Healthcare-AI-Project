# Healthcare AI Project

## Overview
This project implements a Multi-Agent system to generate AI use cases for the healthcare industry. It performs industry research, generates relevant use cases, and collects datasets from `Huggingface`.

## Project Structure
- `agents/`: Contains the individual agent implementations.
- `data/`: Stores the output use cases and resource links.
- `main.py`: Main script to execute the agents.
- `requirements.txt`: Dependencies for the project.

## Setup
1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the root of your  project and add your API keys:

   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   TAVILYCLIENT_API_KEY=your_tavilyclient_api_key_here
   HUGGINGFACE_TOKEN=your_huggingface_token_here
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
## Output
The use cases and resource links and all other results will be stored in the `data/` directory after generated.
