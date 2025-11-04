from google import genai
from google.genai import types
import os

model="gemini-2.5-flash"
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

system_instruction = """
Você é o Assistente Virtual da Whirlpool. 
Você pode responder, em texto curtos, sobre produtos Whirlpool.
"""

config = types.GenerateContentConfig(system_instruction=system_instruction)

def responder_ia(contents):
    response = client.models.generate_content(model=model,contents=contents,config=config)
    return response.text
