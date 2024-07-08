import requests
import json
import subprocess
import time

user_input = "Who won the 2004 World Series? "
#user_input = "Please create a recipe for chocolate chip cookies "
#user_input = "What's the airspeed velocity of an unladen swallow?"
#user_input = "Is it ever morally acceptable to lie? "
#user_input = "Can a set of all sets that do not contain themselves contain itself?"

# URL for a local server to host llama
url = "http://localhost:11434/api/chat"

# Function to run "ollama run llama3"
def start_ollama():
    process = subprocess.Popen(["ollama", "run", "llama3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)  # Wait a few seconds to give the server time to start
    return process

# Function that takes a prompt as input and sends the prompt to llama
def llama3(prompt):
    data = {
        "model": "llama3",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["message"]["content"]

# Start the ollama server
process = start_ollama()

try:
    # Get a response from the LLaMA model
    response = llama3(user_input)
    print(response)
finally:
    # Terminate the ollama process
    process.terminate()
    process.wait()