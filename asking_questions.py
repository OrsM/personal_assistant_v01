import os
import openai
import datetime
import tkinter

# the below requires  pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')
ORGANIZATION=os.getenv('ORGANIZATION')

openai.organization = ORGANIZATION
openai.api_key = API_KEY


def summarize_notes(input_filename = "input_01.txt", max_tokens = 300):
    """Provide a summary with key points & next steps for an input of raw text"""
    input_file = open("%s%s"%('examples/', input_filename), 'r', encoding="utf-8").read()
    basic_prompt = "Can you summarize the following text into the key points and next steps?\n"
    full_prompt = "%s %s"%(basic_prompt,input_file)

    output = openai.Completion.create(
        model="text-davinci-003",
        prompt=full_prompt,
        max_tokens=max_tokens,
        temperature=1
    )

    output_filename = "%s%s%s%s"%('examples/',datetime.datetime.now().strftime("%Y%m%d-%H%M"),'_output','.txt')

    output_file = open(output_filename,'w')
    output_file.write(output['choices'][0]['text'])
    output_file.close()


# summarize_notes("input_01.txt")

def ask_ai(question = "how are you doing today?"):
    """ask Open AI a question, get an answer"""
    output = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=250,
        temperature=1
    )
    return output['choices'][0]['text']


def ask_gpt(question = "how are you doing today?"):
    """ask GPT AI a question, get an answer"""
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": question}
        ]
    )
    return output['choices'][0]['message']['content']



completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "how are you doing today?"}
  ]
)

print(completion.choices[0].message)



def send_message(topic, event=None):
    message = input_field.get()
    input_field.delete(0, tk.END)
    response = generate_response(message, topic)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + message + "\n\n")
    chat_log.insert(tk.END, "GPT-3: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

# Crear ventana principal
root = tk.Tk()
root.title("GPT-3 Chatbot")
root.geometry("800x600")

# Crear un frame que contiene el chatlog y el scrollbar
chat_frame = tk.Frame(root)
chat_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

chat_log = tk.Text(chat_frame, height=20, width=50)
chat_log.config(state=tk.DISABLED)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(chat_frame, command=chat_log.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_log['yscrollcommand'] = scrollbar.set

# Crear un frame que contiene el input field y el botón de enviar
input_frame = tk.Frame(root)
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

input_field = tk.Entry(input_frame, width=50)
input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

send_button = tk.Button(input_frame, text="Enviar", command=lambda: send_message(topic_selector.get()))
send_button.pack(side=tk.RIGHT, padx=5)

# Crear un frame que contiene el selector de temas
topic_frame = tk.Frame(root)
topic_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

topic_label = tk.Label(topic_frame, text="Selecciona un tema:")
topic_label.pack(side=tk.LEFT, padx=5)

topics = ["Trabajo", "Proyecto1", "Ocio", "Reuniones", "Deportes"]
topic_selector = tk.StringVar()
topic_selector.set(topics[0])
topic_dropdown = tk.OptionMenu(topic_frame, topic_selector, *topics)
topic_dropdown.pack(side=tk.LEFT, padx=5)

# Hacer que el input field tenga focus al iniciar la aplicación
input_field.focus_set()

# Iniciar la aplicación
root.mainloop()