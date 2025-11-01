# [Chatbot Whirlpool - Assistente Virtual Inteligente](https://hub.docker.com/r/tarsislimafatec/chatbot_fatec_whirlpool)

## Puxar a Imagem Docker

Para puxar a imagem Docker mais recente do Docker Hub, use o seguinte comando:

```bash
docker pull tarsislimafatec/chatbot_fatec_whirlpool
```

## Executar a Imagem Docker

Depois de puxar a imagem, você pode executar o chatbot usando [Docker](). Certifique-se de ter sua chave de [API do Google Gemini](https://aistudio.google.com/api-keys) pronta.

```bash
docker run -p 5000:5000 -e GOOGLE_API_KEY="SUA_CHAVE_API_GEMINI" tarsislimafatec/chatbot_fatec_whirlpool
```

Substitua `"SUA_CHAVE_API_GEMINI"` pela sua chave de API real do Google Gemini. O chatbot estará acessível em `http://localhost:5000`.
