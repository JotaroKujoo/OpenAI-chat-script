#IMPORTING LIBRARIES

#Importing the requests library to make HTTP/S requests
import requests

#Importing the os library to interact with the operating system
import os

#Importing the load_dotenv function from the dotenv library to load environment variables from a .env file
from dotenv import load_dotenv

#Loading environment variables from the .env file
load_dotenv()

#Retrieving the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#Making a POST request to the AIML API to get a response from the GPT-4o-mini model
response = requests.post(
    "https://api.aimlapi.com/v1/responses",
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer" + OPENAI_API_KEY,
    },
    json={
      "model": "gpt-4o-mini",
      "input": "Cuentame un chiste"
    }
)

data = response.json()
print(data["output_text"])