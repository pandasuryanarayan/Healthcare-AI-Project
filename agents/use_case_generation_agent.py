import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

def generate_use_cases(insights):
    # Initialize the Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Create a prompt based on the industry insights
    prompt = "Based on the following industry insights, List relevant AI use cases (15-20):\n"
    for insight in insights:
        prompt += f"- {insight['content']}\n"
    
    # Generate content using Gemini
    response = model.generate_content(prompt)
    
    # Split the response into individual use cases
    return response.text.strip().split("\n")
