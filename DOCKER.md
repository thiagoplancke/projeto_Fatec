
# Whirlpool Customer Support Chatbot

This is a Python-based chatbot for Whirlpool customer support. It is designed to answer frequently asked questions about Whirlpool products.

The chatbot is built with Python and utilizes the Google Generative AI (Gemini) API for Natural Language Processing.

## How to Use This Image

### Prerequisites

You must have an API key for the Google Gemini API.

### Running the Chatbot

1.  **Pull the image from Docker Hub:**

    ```bash
    docker pull tarsislimafatec/chatbot_fatec_whirlpool:latest
    ```

2.  **Run the container with your API key:**

    Replace `"YOUR_API_KEY"` with your actual Google Gemini API key.

    ```bash
    docker run -it -e GOOGLE_API_KEY="YOUR_API_KEY" tarsislimafatec/chatbot_fatec_whirlpool:latest
    ```

The chatbot will start in an interactive command-line interface.

## Configuration

### Environment Variables

-   `GOOGLE_API_KEY`: **(Required)** Your API key for the Google Gemini API.

## Example Interaction

```
Welcome to the Whirlpool Chatbot!
Ask a question or type "quit" to exit.
You: What is the warranty on my refrigerator?
Chatbot: The standard warranty for Whirlpool refrigerators is one year for parts and labor.
```
