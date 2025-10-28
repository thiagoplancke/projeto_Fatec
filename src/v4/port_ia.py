from google import genai
from google.genai import types

client = genai.Client(api_key="<GEMINI_API_KEY>")

instrucoes = "Você é o Assistente Virtual da Whirlpool."

config = types.GenerateContentConfig(
  system_instruction=instrucoes
)

# aqui eu só usei para testar mesmo.
# port_ia.py
def responder_ia(texto):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=texto,
        config=config
    )

    return response.text
