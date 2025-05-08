import os

from dotenv import load_dotenv, find_dotenv
from openai import AzureOpenAI

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

print(os.getcwd())
print(os.listdir())

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# Test the connection by sending a simple message to the model
response = client.chat.completions.create(
    model="GPT-4.1",  # Aus dem Azure-Portal holen
    messages=[{"role": "user", "content": "Hallo!"}],
)
print(response.choices[0].message.content)
