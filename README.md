# [Chatbot Whirlpool](https://hub.docker.com/r/tarsislimafatec/chatbot_fatec_whirlpool)

Assistente Virtual Inteligente

## Visão Geral do Projeto

Este projeto visa desenvolver um chatbot inteligente para auxiliar os clientes da Whirlpool com dúvidas sobre produtos (por exemplo, máquinas de lavar, fogões). O chatbot utiliza Processamento de Linguagem Natural (PLN) para interpretar perguntas e fornecer respostas relevantes, simulando a interação humana. O projeto integra modelos avançados de IA (Gemini) para uma comunicação aprimorada com o usuário.

## Tecnologias Utilizadas

- Python
- Flask
- HTML
- CSS
- API do Google Gemini (para integração avançada de IA)

## Contribuidores

- [Luiz Henrique Crepaldi](https://github.com/LuizHenrique529) (Product Owner)
- [Matheus Armelindo](#) (Scrum Master)
- [Tarsis Lima](https://github.com/tarsislimadev) (Back-end)
- [Thiago Plancke](https://github.com/thiagoplancke) (Back-end)
- [Mateus Linardi](#) (Back-end)
- [Kevin Walker](#) (Front-end)
- [Emannuel Paulo](https://github.com/emannuelp-boldrin) (Designer)

## Como rodar o projeto

Certifique-se de ter [Docker](https://docs.docker.com/engine/install/) instalado.

Para puxar a imagem Docker mais recente do Docker Hub, use o seguinte comando:

```bash
docker pull tarsislimafatec/chatbot_fatec_whirlpool
```

Certifique-se de ter sua chave de [API do Google Gemini](https://aistudio.google.com/api-keys) pronta.

Substitua `"SUA_CHAVE_API_GEMINI"` pela sua chave de API real do Google Gemini. 

```bash
docker run -p 5000:5000 -e GOOGLE_API_KEY="SUA_CHAVE_API_GEMINI" tarsislimafatec/chatbot_fatec_whirlpool
```

O chatbot estará acessível em `http://localhost:5000`.
