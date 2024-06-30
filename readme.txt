client = OpenAI(base_url="http://192.168.0.34:1234/v1", api_key="lm-studio")




# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]

while True:
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
    
    # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": input("> ")})








    ---------------------------------------------------------


    docker run -d --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=mongo_user \
  -e MONGO_INITDB_ROOT_PASSWORD=mongo_password \
  -v $(pwd)/data:/data/db \
  mongo:latest





----------------------------------------------------------


from pymongo import MongoClient
from openai import OpenAI
import requests

# Configurações do MongoDB
mongo_client = MongoClient('mongodb://mongo_user:mongo_password@localhost:27017/')
db = mongo_client['sua_base_de_dados']  # Substitua pelo nome da sua base de dados
collection = db['registros']  # Substitua pelo nome da sua coleção

# Configurações do OpenAI Studio local
client = OpenAI(base_url="http://192.168.0.34:1234/v1", api_key="lm-studio")

# Função para carregar os registros do MongoDB
def carregar_registros():
    try:
        documentos = list(collection.find())
        dados_para_ai = "\n".join([f"{doc['_id']}: {doc['descricao']}" for doc in documentos])
        return dados_para_ai
    except Exception as e:
        print(f"Ocorreu um erro ao carregar registros do MongoDB: {str(e)}")
        return ""

# Função para consultar registros no MongoDB e gerar resposta da AI
def consultar_registros(prompt):
    try:
        # Carrega os registros do MongoDB
        dados_para_ai = carregar_registros()

        # Monta o prompt completo
        prompt_completo = f"{prompt}\n{dados_para_ai}"

        # Chama a API do OpenAI Studio local
        response = client.chat.completions.create(
            model="lm-studio",
            messages=[{"role": "user", "content": prompt_completo}],
            temperature=0.7,
            stream=True,  # Use stream para lidar com resposta de streaming
        )

        # Processa a resposta do streaming
        for chunk in response:
            if chunk.object == 'text':
                try:
                    message = chunk.choices[0].message['content']
                    return message
                except (IndexError, KeyError) as e:
                    print(f"Resposta inválida da API: {e}")
                    return "Desculpe, ocorreu um erro ao consultar. Por favor, tente novamente."

    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar a API do OpenAI Studio: {e}")
        return "Desculpe, ocorreu um erro ao consultar. Por favor, tente novamente."
    except Exception as e:
        print(f"Ocorreu um erro ao consultar: {str(e)}")
        return "Desculpe, ocorreu um erro ao consultar. Por favor, tente novamente."
    finally:
        if 'response' in locals() and hasattr(response, 'close'):
            response.close()  # Fecha o stream de resposta, se existir

# Loop de interação
while True:
    try:
        # Exibe o histórico e aguarda entrada do usuário
        user_input = input("> ")
        resposta = consultar_registros(user_input)
        if resposta:
            print(f"Assistente: {resposta}")
        else:
            print("Resposta do assistente não recebida.")

    except KeyboardInterrupt:
        print("\nPrograma encerrado.")
        break
    except Exception as e:
        print(f"Erro durante a interação: {e}")
        break

# Fechamento da conexão com MongoDB
mongo_client.close()
