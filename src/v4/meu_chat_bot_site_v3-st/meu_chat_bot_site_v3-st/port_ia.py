# aqui eu só usei para testar mesmo.
# port_ia.py
def responder_ia(texto):
    texto = texto.lower()

    if "oi" in texto or "olá" in texto:
        return "Olá! Sou Whiribot :D"
    elif "ajuda" in texto:
        return "Claro! Me diga com o que você precisa."
    elif "tchau" in texto:
        return "Até mais! 👋"
    else:
        return "Interessante... me conte mais sobre isso!"