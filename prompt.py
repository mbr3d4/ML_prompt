from openai import OpenAI
from pymongo import MongoClient
import sys

# Configurações do MongoDB
mongo_client = MongoClient('mongodb://mongo_user:mongo_password@localhost:27017/')
db = mongo_client['sua_base_de_dados']  # Substitua pelo nome da sua base de dados
collection = db['registros']  # Substitua pelo nome da sua coleção

# Point to the local server
client = OpenAI(base_url="http://192.168.0.34:1234/v1", api_key="lm-studio")

history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]

def save_to_mongo(conversation_history):
    try:
        collection.insert_one({"history": conversation_history})
    except Exception as e:
        print(f"An error occurred while saving to MongoDB: {e}")

def fetch_knowledge_from_mongo():
    try:
        knowledge = collection.find({}, {'_id': 0})  # Exclude MongoDB's default _id field
        return list(knowledge)
    except Exception as e:
        print(f"An error occurred while fetching from MongoDB: {e}")
        return []

def read_instructions_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred while reading the instructions file: {e}")
        return ""

while True:
    try:
        # Fetch knowledge base from MongoDB
        knowledge_base = fetch_knowledge_from_mongo()

        # Convert the knowledge base to a format the model can understand
        knowledge_base_str = "\n".join([str(record) for record in knowledge_base])

        # Read additional instructions from the file
        instructions = read_instructions_from_file('instrucoes.txt')

        # Add knowledge base and instructions to the initial system prompt
        initial_prompt = ("Você é um assistente inteligente. Você sempre fornece respostas bem fundamentadas, corretas e úteis "
                          "Aqui estão alguns conhecimentos adicionais para ajudá-lo:\n" + knowledge_base_str + "\n\n" +
                          "Aqui estão algumas instruções adicionais:\n" + instructions)
        history[0] = {"role": "system", "content": initial_prompt}

        completion = client.chat.completions.create(
            model="microsoft/Phi-3-mini-4k-instruct-gguf",
            messages=history,
            temperature=0.7,
            stream=True,
        )

        new_message = {"role": "assistant", "content": ""}
        
        for chunk in completion:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
                new_message["content"] += chunk.choices[0].delta.content

        history.append(new_message)
        
        print()
        user_input = input("> ")
        
        if user_input.lower() == "exit":
            print("Exiting chat.")
            save_to_mongo(history)
            break

        history.append({"role": "user", "content": user_input})

    except Exception as e:
        print(f"An error occurred: {e}")
        save_to_mongo(history)
        break
