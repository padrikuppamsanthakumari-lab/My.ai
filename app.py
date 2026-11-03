Python

import os
from openai import OpenAI

# Your AI assistant
client = OpenAI()

AI_NAME = "My AI"

instructions = """
You are My AI, a friendly and helpful AI assistant.
You answer questions clearly and simply.
You help with education, science, mathematics,
technology, and programming.
Always be polite and helpful.
"""

print("================================")
print("       WELCOME TO MY AI")
print("================================")
print("Type 'exit' to stop chatting.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("My AI: Goodbye!")
        break

    try:
        response = client.responses.create(
            model="gpt-6-astra",
            instructions=instructions,
            input=question
        )

        print(f"\n{AI_NAME}: {response.output_text}")

    except Exception as error:
        print("Something went wrong. Please try again.")
        print(error)
      
