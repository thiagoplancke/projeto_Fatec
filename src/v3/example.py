from google import genai
from google.genai import types

client = genai.Client(api_key="<GEMINI_API_KEY>")

instrucoes = "Você é o Assistente Virtual da Whirlpool."

config = types.GenerateContentConfig(
  system_instruction=instrucoes
)

prompt = input("> ")

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=prompt,
  config=config
)

print('Resposta: ')
print(response.text)
