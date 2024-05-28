from flask import Flask, request

from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from dotenv import load_dotenv

from langchain_community.llms import Ollama
# Load environment variables from .env file (e.g., API keys)
load_dotenv()

# Initialize the ElevenLabs client (for text-to-speech conversion, commented out)
client = ElevenLabs()

# Initialize the Ollama language model interface
cached_llm = Ollama(model="llama3", base_url="http://localhost:11434")

# Create a Flask app instance
app = Flask(__name__)

import os

def get_file_content(selected_dino):
    """
        Reads the content of a text file corresponding to the selected dinosaur from the 'database' directory.
    """
    directory = os.path.join(os.getcwd(), "database")
    file_path = os.path.join(directory, f"{selected_dino}.txt")
    with open(file_path, "r") as file:
        content = file.read()
    return content

def llmPost(query, selected_dino, content):
    """
    Sends a query to the LLM (Ollama) with the relevant dinosaur content as context.
    Formats the prompt to request a summary in a 'tourist guide' style.
    """
    llm_query = f"Based on the provided content, please provide a brief summary in a 'tourist guide' style to answer the query: {query}\n\n{content}"
    print("llm_query : " + llm_query)
    response = cached_llm.invoke(llm_query)
    return response

@app.route("/llm", methods=["POST"])
def handle_llm():
    """
    Handles POST requests to the /llm endpoint.
    Extracts query and selected dinosaur from the JSON payload.
    Fetches relevant content from the database.
    Calls the LLM to get a response.
    (Optionally, generates audio using ElevenLabs, commented out)
    Returns the LLM response as JSON.
    """
    json_content = request.json
    query = json_content.get("query")
    selected_dino = json_content.get("selected_dino")
    # Retrieve dinosaur information from the database
    content = get_file_content(selected_dino)
    # Get a response from the LLM
    response = llmPost(query, selected_dino, content)

    print(response)

    #audio_stream = client.generate(text="You asked: " + query, stream=True)
    #stream(audio_stream)

    #audio_stream = client.generate(text=response, stream=True)
    #stream(audio_stream)

    response_answer = {"answer": response}

    return response_answer

# Start the app
def start_app():
    # Start the Flask server on port 8080, accessible to all network interfaces.
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    start_app()
