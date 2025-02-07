import os
import json
from openai import AzureOpenAI

# Replace with your actual API key and endpoint
api_key = "your_new_api_key"
endpoint = "your_end_point"
deployment_name = "your_deployment_name"

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=endpoint,
    api_version="2023-12-01-preview"
)

# Function to generate JSON in the strict format
def generate_form_json(form_description):
    prompt = f"""
    Generate a JSON array containing form fields with the following structure:
    
    [
      {{
        "checked": true,
        "description": "This is your public display name.",
        "disabled": false,
        "label": "Username",
        "name": "name_0819770465",
        "placeholder": "shadcn",
        "required": true,
        "rowIndex": 0,
        "type": "",
        "value": "",
        "variant": "Input"
      }}
    ]
    
    The form should contain fields: {form_description}. Ensure the JSON is properly formatted.
    """

    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are an assistant that generates structured JSON output."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    json_output = response.choices[0].message.content.strip()
    
    # Validate JSON output
    try:
        parsed_json = json.loads(json_output)
        return json.dumps(parsed_json, indent=2)  # Return formatted JSON
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON format received. \n{json_output}"

# Chatbot interface
def chatbot():
    print("Welcome to the Form JSON Generator Chatbot!")
    while True:
        form_description = input("Enter form fields (or type 'exit' to quit): ")
        if form_description.lower() == 'exit':
            break
        try:
            form_json = generate_form_json(form_description)
            print("\nGenerated Form JSON:\n")
            print(form_json)
            print("\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chatbot()
