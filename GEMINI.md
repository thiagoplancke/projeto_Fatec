# GEMINI.md

## Project Overview

This project is a Python-based chatbot for Whirlpool customer support. It is designed to answer frequently asked questions about Whirlpool products.

The chatbot is built with Python and utilizes the Google Generative AI (Gemini) API for Natural Language Processing. Specifically, it uses embedding models to understand user questions and find the most relevant answers from a predefined list of FAQs.

The project is structured as a simple Python application and includes a `Dockerfile`, suggesting that it is intended to be deployed as a containerized service. The `README.md` also mentions the use of Flask, although it is not currently listed in the `requirements.txt`.

## Key Files

- `src/chatbot/chatbot.py`: The main application logic, including the FAQ data, Gemini API integration, and a command-line interface for interacting with the chatbot.
- `src/chatbot/requirements.txt`: Lists the project's Python dependencies, which currently only includes `google-generativeai`.
- `src/chatbot/Dockerfile`: A configuration file for building a Docker container for the application. It is currently incomplete.
- `README.md`: Provides a high-level overview of the project, its purpose, and the development team.

## Building and Running

### Prerequisites

- Python 3
- An API key for the Google Gemini API.

### Running Locally

1.  **Install dependencies:**

    ```bash
    pip install -r src/chatbot/requirements.txt
    ```

2.  **Set the API Key:**

    The application requires a Google Gemini API key. The key is currently hardcoded in `src/chatbot/chatbot.py`. It is highly recommended to remove the hardcoded key and set it as an environment variable for security reasons.

    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY"
    ```

    Then, in `src/chatbot/chatbot.py`, you should use the following line to configure the API key:

    ```python
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    ```

3.  **Run the chatbot:**

    ```bash
    python src/chatbot/chatbot.py
    ```

    This will start the chatbot in a command-line interface.

### Docker

The `Dockerfile` is currently incomplete. To build and run this application with Docker, the `Dockerfile` would need to be updated to copy the source code and install the dependencies. A more complete `Dockerfile` would look something like this:

```dockerfile
FROM python:alpine

WORKDIR /app

COPY src/chatbot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/chatbot/ .

CMD ["python", "chatbot.py"]
```

## Development Conventions

- **API Keys:** The Google Gemini API key is currently hardcoded in `src/chatbot/chatbot.py`. This is a security risk. The recommended practice is to use environment variables to manage sensitive information like API keys.
- **FAQ Data:** The FAQ data is hardcoded as a list of dictionaries in `src/chatbot/chatbot.py`. For a more scalable solution, this data could be moved to a separate file (e.g., a JSON or CSV file) or a database.
- **Containerization:** The presence of a `Dockerfile` indicates an intention to containerize the application. The `Dockerfile` should be completed to enable building and running the application in a Docker container.
