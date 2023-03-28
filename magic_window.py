import os
import openai
import tkinter as tk
# the below requires  pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')
ORGANIZATION=os.getenv('ORGANIZATION')

openai.organization = ORGANIZATION
openai.api_key = API_KEY

MODEL="gpt-3.5-turbo"

def generate_response(prompt):
    """ask GPT to do something, get an answer"""
    output = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return output['choices'][0]['message']['content']

def send_message():
    message = input_field.get()
    input_field.delete(0, tk.END)
    response = generate_response(message)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + message + "\n\n")
    chat_log.insert(tk.END, MODEL+": " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

# Crear ventana principal
root = tk.Tk()
root.title(MODEL)
#root.geometry("800x600")

root.geometry("800x600+0+0")

# close_button = tk.Button(root, width = 30, text="Quit", command=root.destroy)
# close_button.pack(side=tk.RIGHT)

# Crear un frame que contiene el chatlog y el scrollbar
chat_frame = tk.Frame(root)
chat_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=12, pady=12)

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

send_button = tk.Button(input_frame, text="Enviar", command=lambda: send_message())
send_button.pack(side=tk.RIGHT, padx=5)

# Hacer que el input field tenga focus al iniciar la aplicación
input_field.focus_set()

# Iniciar la aplicación
root.mainloop()