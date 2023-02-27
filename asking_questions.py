import os
import openai
import datetime
# the below requires  pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')
ORGANIZATION=os.getenv('ORGANIZATION')

openai.organization = ORGANIZATION
openai.api_key = API_KEY


def summarize_notes(input_filename = "input_01.txt"):
    """Provide a summary with key points & next steps for an input of raw text"""
    input_file = open("%s%s"%('examples/', input_filename), 'r', encoding="utf-8").read()
    basic_prompt = "Can you summarize the following text into the key points and next steps?\n"
    full_prompt = "%s %s"%(basic_prompt,input_file)

    output = openai.Completion.create(
        model="text-davinci-003",
        prompt=full_prompt,
        max_tokens=250,
        temperature=1
    )

    output_filename = "%s%s%s%s"%('examples/',datetime.datetime.now().strftime("%Y%m%d-%H%M"),'_output','.txt')

    output_file = open(output_filename,'w')
    output_file.write(output['choices'][0]['text'])
    output_file.close()

# summarize_notes()

def ask_ai(question = "how are you doing today?"):
    """ask Open AI a question, get an answer"""
    output = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=250,
        temperature=1
    )
    return output['choices'][0]['text']
