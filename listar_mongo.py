from pymongo import MongoClient

# Configurações do cliente MongoDB
client = MongoClient('mongodb://mongo_user:mongo_password@localhost:27017/')
db = client['sua_base_de_dados']  # Substitua pelo nome da sua base de dados
collection = db['registros']  # Substitua pelo nome da sua coleção

# Consulta para listar todos os documentos na coleção
documentos = collection.find()

# Imprime os documentos encontrados
for documento in documentos:
    print(documento)

# Fecha a conexão com o MongoDB
client.close()
