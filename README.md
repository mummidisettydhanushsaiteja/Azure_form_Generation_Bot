Azure Form JSON Generator Chatbot 🤖✨

Overview 🚀
The Azure Form JSON Generator Chatbot is an interactive chatbot that generates JSON structures for forms based on user input. It leverages Azure OpenAI to create structured JSON outputs dynamically, making form generation simple and efficient. 📝

Features 🌟
- ✅ Generates dynamic form JSON based on user descriptions.
- ✅ Powered by Azure OpenAI for intelligent form structuring.
- ✅ Secure API key handling using `.env`.
- ✅ User-friendly chatbot interface for easy interaction.

Technologies Used 🛠️
- Python 🐍
- Azure OpenAI 🌍
- OpenAI API 🤖
- Flask (Optional for Web UI) 🌐
- Dotenv for Environment Variables 🔒

Setup Instructions 🏗️
1. Clone the Repository 📂

git clone https://github.com/your-username/azure-form-chatbot.git
cd azure-form-chatbot


2. Create a Virtual Environment 🌱

python -m venv venv
source venv/bin/activate   On Windows use: venv\Scripts\activate

3. Install Dependencies 📦
pip install openai python-dotenv


4. Set Up Environment Variables 🔐
Create a `.env` file and add:
ini
AZURE_OPENAI_API_KEY=your_new_api_key
AZURE_OPENAI_ENDPOINT=https://ai-genpod378939727809.openai.azure.com
AZURE_DEPLOYMENT_NAME=your_deployment_name

5. Run the Chatbot 🏃‍♂️
python form_chatbot.py


 Usage 💬
1. The chatbot will prompt: `Please describe the form you want to create (or type 'exit' to quit):`
2. Enter a description like: `A registration form with name, email, and password fields.`
3. The chatbot will generate and display the corresponding JSON structure.

 Example Output 📄
json
{
  "form": {
    "title": "Registration Form",
    "fields": [
      {"name": "Name", "type": "text", "required": true},
      {"name": "Email", "type": "email", "required": true},
      {"name": "Password", "type": "password", "required": true}
    ]
  }
}


 Security Considerations 🔒
- Never hardcode API keys in the script; always use environment variables.
- Add `.env` to `.gitignore` to prevent accidental commits.

echo ".env" >> .gitignore

Contributing 🤝
Feel free to fork this repository, submit issues, or make pull requests 🚀

License 📜
This project is licensed under the MIT License.


