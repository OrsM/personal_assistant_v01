import os
import openai

# the below requires  pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')
ORGANIZATION=os.getenv('ORGANIZATION')

openai.organization = ORGANIZATION
openai.api_key = API_KEY

def ask_gpt(question = "how are you doing today?"):
    """ask GPT AI a question, get an answer"""
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": question}
        ]
    )
    return output['choices'][0]['message']['content']