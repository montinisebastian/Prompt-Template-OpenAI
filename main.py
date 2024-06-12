from openai import OpenAI
# Setup environment and logging
import os
import logging
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def chat_with_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}],
            temperature=0  # This sets the creativity to 0
        )
        # Correct way to access the message content
        if response.choices:
            logging.info(f"Response: {response.choices[0].message.content}")
            logging.info(f"Tokens used: {response.usage.total_tokens}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    user_prompt = "Please explain the basics of Python data types."
    chat_with_openai(user_prompt)
