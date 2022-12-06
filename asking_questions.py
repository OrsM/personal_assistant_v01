import os
import openai
import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')
ORGANIZATION=os.getenv('ORGANIZATION')

openai.organization = ORGANIZATION
openai.api_key = API_KEY

sample_input = open('examples/input_02.txt', 'r', encoding="utf-8").read()
basic_prompt = "Can you summarize the following text into the key points and next steps?\n"
full_prompt = "%s %s"%(basic_prompt,sample_input)

output = openai.Completion.create(
    model="text-davinci-003",
    prompt=full_prompt,
    max_tokens=250,
    temperature=1
)

filename = "%s%s%s%s"%('examples/',datetime.datetime.now().strftime("%Y%m%d-%H%M"),'_output','.txt')

result = open(filename,'w')
result.write(output['choices'][0]['text'])
result.close()
