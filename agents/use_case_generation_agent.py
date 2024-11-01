import google.generativeai as genai

genai.configure(api_key='AIzaSyAXyynS94oAsXvplaDJGFHjsIS74Mi6Fh4')

def generate_use_cases(insights):
    # Initialize the Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Create a prompt based on the industry insights
    prompt = "Based on the following industry insights, generate relevant AI use cases (minimum 10-15):\n"
    for insight in insights:
        prompt += f"- {insight['content']}\n"
    
    # Generate content using Gemini
    response = model.generate_content(prompt)
    
    # Split the response into individual use cases
    return response.text.strip().split("\n")
