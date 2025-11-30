# IMPORTING LIQBRARIES

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Chat loop
while True:
    user = input("You: ")

    if user.lower() in ["exit", "quit", "salir"]:
        print("Exiting chat. Goodbye!")
        break

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

        data = response.json()

        print("AI:", data["output_text"])

    except KeyError as e:
        print("❌ KeyError: Missing key in response →", e)

    except requests.exceptions.RequestException as e:
        print("❌ Request error:", e)

    except Exception as e:
        print("❌ Unexpected error:", e)