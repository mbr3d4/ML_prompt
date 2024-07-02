from pymongo import MongoClient
from datetime import datetime

# Dados estruturados conforme exemplo anterior
registros = [
    {
        "chave": "CHG0337468",
        "descricao": "ajuste na configuração do serviço de e-mail para melhorar a entrega de notificações.",
        "status": "concluido",
        "validado_por": "maria dos santos",
        "turno": "manhã",
        "líder": "ana paula souza",
        "técnico": "fernando almeida",
        "ocorrência": "chg0337468",
        "incidente": "inc766546",
        "data": "2024-06-29",  # Corrigido
        "horário de início": "09:00:00",
        "impacto": "médio",
        "causa raiz": "configuração incorreta",
        "ações": [
            "09:00:00 - início da mudança",
            "09:45:00 - ajuste na configuração",
            "10:30:00 - testes realizados"
        ],
        "envolvidos": [
            "maria dos santos",
            "ana paula souza"
        ],
        "horário de fim": "10:30:00"
    },
    {
        "chave": "CHG0337469",
        "descricao": "atualização de segurança nos servidores web para mitigação de vulnerabilidades.",
        "status": "em andamento",
        "validado_por": "pedro oliveira",
        "turno": "manhã",
        "líder": "joão pereira",
        "técnico": "ricardo fonseca",
        "ocorrência": "chg0337469",
        "incidente": "inc766547",
        "data": "2024-06-29",  # Corrigido
        "horário de início": "10:00:00",
        "impacto": "alto",
        "causa raiz": "vulnerabilidade detectada",
        "ações": [
            "10:00:00 - início da atualização",
            "11:00:00 - aplicação dos patches",
            "12:00:00 - reinício dos servidores"
        ],
        "envolvidos": [
            "pedro oliveira",
            "joão pereira"
        ]
    },
    {
        "chave": "CHG0337470",
        "descricao": "correção de bug no sistema de login para resolver problemas de autenticação.",
        "status": "falha",
        "validado_por": "carla moreira",
        "turno": "manhã",
        "líder": "maria ferreira",
        "técnico": "lucas rodrigues",
        "ocorrência": "chg0337470",
        "incidente": "inc766548",
        "data": "2024-06-29",  # Corrigido
        "horário de início": "08:00:00",
        "impacto": "baixo",
        "causa raiz": "erro de código",
        "ações": [
            "08:00:00 - início da correção",
            "08:45:00 - revisão do código",
            "09:30:00 - testes falharam"
        ],
        "envolvidos": [
            "carla moreira",
            "maria ferreira"
        ]
    },
    {
        "chave": "CHG0337471",
        "descricao": "melhoria no desempenho do banco de dados para reduzir o tempo de resposta.",
        "status": "concluido",
        "validado_por": "jorge silva",
        "turno": "tarde",
        "líder": "ana santos",
        "técnico": "paulo henrique",
        "ocorrência": "chg0337471",
        "incidente": "inc766549",
        "data": "2024-06-29",  # Corrigido
        "horário de início": "14:00:00",
        "impacto": "médio",
        "causa raiz": "alta latência",
        "ações": [
            "14:00:00 - início da otimização",
            "14:45:00 - ajuste nos índices",
            "15:30:00 - verificação do desempenho"
        ],
        "envolvidos": [
            "jorge silva",
            "ana santos"
        ],
        "horário de fim": "15:30:00"
    },
    {
        "chave": "CHG0337472",
        "descricao": "migração do sistema de gerenciamento de conteúdo para nova plataforma.",
        "status": "em andamento",
        "validado_por": "lucas mendes",
        "turno": "tarde",
        "líder": "juliana alves",
        "técnico": "roberto souza",
        "ocorrência": "chg0337472",
        "incidente": "inc766550",
        "data": "2024-06-29",  # Corrigido
        "horário de início": "13:00:00",
        "impacto": "alto",
        "causa raiz": "plataforma obsoleta",
        "ações": [
            "13:00:00 - início da migração",
            "14:30:00 - transferência de dados",
            "16:00:00 - configuração da nova plataforma"
        ],
        "envolvidos": [
            "lucas mendes",
            "juliana alves"
        ]
    },
    {
        "chave": "CHG0337473",
        "descricao": "configuração de novo servidor de backup para aumentar a segurança dos dados.",
        "status": "falha",
        "validado_por": "renato barros",
        "turno": "tarde",
        "líder": "marcos oliveira",
        "técnico": "andré lopes",
        "ocorrência": "chg0337473",
        "incidente": "inc766551",
        "data": "2024-06-29",  # Corrigido
        "horário de início": "15:00:00",
        "impacto": "médio",
        "causa raiz": "erro de configuração",
        "ações": [
            "15:00:00 - início da configuração",
            "15:45:00 - testes iniciais",
            "16:30:00 - falha na validação"
        ],
        "envolvidos": [
            "renato barros",
            "marcos oliveira"
        ]
    },
    {
        "chave": "CHG0337474",
        "descricao": "implementação de nova política de firewall para aumentar a segurança da rede.",
        "status": "concluido",
        "validado_por": "antonio carlos",
        "turno": "noite",
        "líder": "sandra lima",
        "técnico": "leandro costa",
        "ocorrência": "chg0337474",
        "incidente": "inc766552",
        "data": "2024-06-29",  # Corrigido
        "horário de início": "20:00:00",
        "impacto": "alto",
        "causa raiz": "necessidade de segurança",
        "ações": [
            "20:00:00 - início da implementação",
            "21:00:00 - configuração do firewall",
            "22:00:00 - testes de segurança"
        ],
        "envolvidos": [
            "antonio carlos",
            "sandra lima"
        ],
        "horário de fim": "22:00:00"
    },
    {
        "chave": "CHG0337475",
        "descricao": "atualização do software de monitoramento para a versão mais recente.",
        "status": "em andamento",
        "validado_por": "bruno martins",
        "turno": "noite",
        "líder": "claudia nogueira",
        "técnico": "maria aparecida",
        "ocorrência": "chg0337475",
        "incidente": "inc766553",
        "data": "2024-06-29",  # Corrigido
        "horário de início": "21:00:00",
        "impacto": "baixo",
        "causa raiz": "versão desatualizada",
        "ações": [
            "21:00:00 - início da atualização",
            "22:00:00 - instalação da nova versão",
            "23:00:00 - reinício do sistema"
        ],
        "envolvidos": [
            "bruno martins",
            "claudia nogueira"
        ]
    }
]

# Configurações do cliente MongoDB
client = MongoClient('mongodb://mongo_user:mongo_password@localhost:27017/')
db = client['sua_base_de_dados']  # Substitua pelo nome da sua base de dados
collection = db['registros']  # Substitua pelo nome da sua coleção

# Inserção dos registros na coleção
result = collection.insert_many(registros)

# Imprime os IDs dos documentos inseridos
print(f"Inseridos IDs: {result.inserted_ids}")

# Fecha a conexão com o MongoDB
client.close()
