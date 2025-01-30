import os
from openai import AzureOpenAI

# Replace with your actual API key and endpoint
api_key = "your_new_api_key"  
endpoint = "your_new_endpoint"  
deployment_name = "your_deployment_name"  # Replace with your deployment name from Azure

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=endpoint,
    api_version="2023-12-01-preview"  # Latest API version
)

# Function to generate form JSON with the desired structure
def generate_form_json(form_description):
    form_json = [
        {
            "checked": True,
            "description": "Your date of birth is used to calculate your age.",
            "disabled": False,
            "label": "Date of birth",
            "name": "name_8251071862",
            "placeholder": "Placeholder",
            "required": True,
            "rowIndex": 0,
            "type": "",
            "value": "",
            "variant": "Date Picker"
        },
        {
            "checked": True,
            "description": "Add the date of submission with detailly.",
            "disabled": False,
            "label": "Submission Date",
            "name": "name_9692581527",
            "placeholder": "Placeholder",
            "required": True,
            "rowIndex": 0,
            "type": "",
            "value": "",
            "variant": "Datetime Picker"
        },
        {
            "checked": True,
            "description": "Select a file to upload.",
            "disabled": False,
            "label": "Select File",
            "name": "name_8537132264",
            "placeholder": "Placeholder",
            "required": True,
            "rowIndex": 0,
            "type": "",
            "value": "",
            "variant": "File Input"
        },
        {
            "checked": True,
            "description": "This is your public display name.",
            "disabled": False,
            "label": "Username",
            "name": "name_3284148037",
            "placeholder": "shadcn",
            "required": True,
            "rowIndex": 0,
            "type": "",
            "value": "",
            "variant": "Input"
        },
        {
            "checked": True,
            "description": "Please enter the one-time password sent to your phone.",
            "disabled": False,
            "label": "One-Time Password",
            "name": "name_5019323857",
            "placeholder": "Placeholder",
            "required": True,
            "rowIndex": 0,
            "type": "",
            "value": "",
            "variant": "Input OTP"
        },
        {
            "checked": True,
            "description": "Select multiple options.",
            "disabled": False,
            "label": "Select your framework",
            "name": "name_4237324743",
            "placeholder": "Placeholder",
            "required": True,
            "rowIndex": 0,
            "type": "",
            "value": "",
            "variant": "Multi Select"
        },
        {
            "checked": True,
            "description": "Enter your password.",
            "disabled": False,
            "label": "Password",
            "name": "name_5780312975",
            "placeholder": "Placeholder",
            "required": True,
            "rowIndex": 0,
            "type": "",
            "value": "",
            "variant": "Password"
        },
        {
            "checked": True,
            "description": "You can manage your mobile notifications in the mobile settings page.",
            "disabled": False,
            "label": "Use different settings for my mobile devices",
            "name": "name_3992127805",
            "placeholder": "Placeholder",
            "required": True,
            "rowIndex": 0,
            "type": "",
            "value": "",
            "variant": "Checkbox"
        },
        {
            "checked": True,
            "description": "You can manage email addresses in your email settings.",
            "disabled": False,
            "label": "Email",
            "name": "name_9766947504",
            "placeholder": "Select a verified email to display",
            "required": True,
            "rowIndex": 0,
            "type": "",
            "value": "",
            "variant": "Select"
        }
    ]
    return form_json

# Chatbot interface
def chatbot():
    print("Welcome to the Form JSON Generator Chatbot!")
    while True:
        form_description = input("Please describe the form you want to create (or type 'exit' to quit): ")
        if form_description.lower() == 'exit':
            break
        form_json = generate_form_json(form_description)
        print("\nGenerated Form JSON:\n")
        print(form_json)
        print("\n")

if __name__ == "__main__":
    chatbot()
