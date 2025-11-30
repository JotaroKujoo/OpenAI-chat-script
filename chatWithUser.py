# IMPORTING LIQBRARIES

#Importing the requests library to make HTTP/S requests
import requests

#Importing the os library to interact with the operating system
import os

# Importing the load_dotenv function from the dotenv library to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieving the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Chat loop
while True:
    user = input("You: ")

    # Exit condition
    if user.lower() in ["exit", "quit", "salir"]:
        print("Exiting chat. Goodbye!")
        break
    
    # Error handling
    try:
        
        # Making request to AIML API
        response = requests.post(
            "https://api.aimlapi.com/v1/responses",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + OPENAI_API_KEY,
            },
            json={
                "model": "gpt-4o-mini",
                "input": user
            }
        )

        # Raises an error if status code is not 200
        response.raise_for_status()

        #Printing the AI response
        data = response.json()
        print("AI:", data["output_text"])

    except KeyError as e:
        print("❌ KeyError: Missing key in response →", e)

    except requests.exceptions.RequestException as e:
        print("❌ Request error:", e)

    except Exception as e:
        print("❌ Unexpected error:", e)