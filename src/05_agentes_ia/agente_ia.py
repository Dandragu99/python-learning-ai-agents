
import os
from dotenv import load_dotenv
from groq import Groq

# Cargar las variables del archivo .env
load_dotenv()

# Crear el cliente para comunicarnos con Groq
cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Enviar una petición al modelo
respuesta = cliente.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "¿Cuánto es 10 más 5?"
        }
    ]
)

# Mostrar la respuesta generada
print(respuesta.choices[0].message.content)
