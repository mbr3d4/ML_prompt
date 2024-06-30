from pymongo import MongoClient
from datetime import datetime

# Dados estruturados conforme exemplo anterior
registros = [
 {
      "chave": "CHG0337467",
      "data_hora": "2024-06-29T10:00:00Z",
      "descricao": "ROGERIO DE PAULA FERNANDES - CHG0337467 - [NEXT] - ALTERAÇÃO NO SERVIÇO NEXT-PROFILE PARA AJUSTE NO TRATAMENTO DE CAMPOS QUE GERAM NPE NO PROCESSO DE REONBOARDING E CORREÇÃO DO CÓDIGO EM PRODUÇÃO DA ROTA PARA ENCERRAMENTO DE CONTRATOS DE FGTS",
      "status": "Sucesso",
      "validado_por": "DS CASSIO LUIZ SALGADO",
      "Turno": "Manhã",
      "Líder Técnico": "",
      "Técnico responsável": "ROGERIO DE PAULA FERNANDES",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-29T10:00:00Z",
      "Horário de fim": "2024-06-29T11:30:00Z",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": [
        "DS CASSIO LUIZ SALGADO"
      ]
    },
    {
      "chave": "CHG0340621",
      "data_hora": "2024-06-29T14:00:00Z",
      "descricao": "IVANILDO DE OLIVEIRA JOAQUIM - CHG0340621 - VILA CRM: DEPLOY DE METADADOS SALESFORCE NÃO TRANSACIONAIS.",
      "status": "Sucesso",
      "validado_por": "DS CAROLINA MOREIRA CAPITANI",
      "Turno": "Tarde",
      "Líder Técnico": "",
      "Técnico responsável": "IVANILDO DE OLIVEIRA JOAQUIM",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-29T14:00:00Z",
      "Horário de fim": "",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": [
        "DS CAROLINA MOREIRA CAPITANI"
      ]
    },
    {
      "chave": "CHG0341064",
      "data_hora": "2024-06-30T08:30:00Z",
      "descricao": "WILSON ROBERTO DE SOUZA FILHO - CHG0341064 - PDM-2510: Implantação da versão 1.30.2.",
      "status": "Sucesso",
      "validado_por": "DS FABIO DONIZETE ALVES",
      "Turno": "Manhã",
      "Líder Técnico": "",
      "Técnico responsável": "WILSON ROBERTO DE SOUZA FILHO",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-30T08:30:00Z",
      "Horário de fim": "",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": [
        "DS FABIO DONIZETE ALVES"
      ]
    },
    {
      "chave": "CHG0341003",
      "data_hora": "2024-06-29T20:30:00Z",
      "descricao": "JOSE GERALDO MOREIRA FERREIRA - CHG0341003 - BRACE-6454: Implantar mudanças no BFF do produto de Consignado INSS.",
      "status": "Sucesso",
      "validado_por": "DS JOSE GERALDO MOREIRA FERREIRA",
      "Turno": "Noite/Madrugada",
      "Líder Técnico": "",
      "Técnico responsável": "JOSE GERALDO MOREIRA FERREIRA",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-29T20:30:00Z",
      "Horário de fim": "",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": [
        "DS JOSE GERALDO MOREIRA FERREIRA"
      ]
    },
    {
      "chave": "CHG0341243",
      "data_hora": "2024-06-29T22:00:00Z",
      "descricao": "LILIANE CRISTINA RODRIGUES - CHG0341243 - BRACE-6256: Disponibilizar a funcionalidade de enviar o comprovante por e-mail para os Corbans.",
      "status": "Falha no deploy",
      "validado_por": "",
      "Turno": "Noite/Madrugada",
      "Líder Técnico": "",
      "Técnico responsável": "LILIANE CRISTINA RODRIGUES",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-29T22:00:00Z",
      "Horário de fim": "",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": []
    },
    {
      "chave": "CHG0337618",
      "data_hora": "2024-06-30T09:00:00Z",
      "descricao": "CRISTIANE DE FREITAS - CHG0337618 - OF][Regulatório] - Atendimento da IN 463 - Tratamento da ausência do campo 'resource' nas respostas do serviço /products no fluxo de consentimento.",
      "status": "Sucesso",
      "validado_por": "DS Cristiane de Freitas",
      "Turno": "Manhã",
      "Líder Técnico": "",
      "Técnico responsável": "CRISTIANE DE FREITAS",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-30T09:00:00Z",
      "Horário de fim": "",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": [
        "DS Cristiane de Freitas"
      ]
    },
    {
      "chave": "CHG0335208",
      "data_hora": "2024-06-29T15:00:00Z",
      "descricao": "ROODNEY MORAES DE SOUZA - CHG0335208-PPJSUPJ-7057: Implantar funcionalidade consultar e persistir id da conta",
      "status": "Sucesso",
      "validado_por": "DS ROODNEY MORAES DE SOUZA",
      "Turno": "Tarde",
      "Líder Técnico": "",
      "Técnico responsável": "ROODNEY MORAES DE SOUZA",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-29T15:00:00Z",
      "Horário de fim": "",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": [
        "DS ROODNEY MORAES DE SOUZA"
      ]
    },
    {
      "chave": "CHG0340067",
      "data_hora": "2024-06-30T10:00:00Z",
      "descricao": "PAULO GEOVANNI SCORSI DOS SANTOS - CHG0340067-Openfinance - Pagamentos - Funcionalidade de cancelamento de Transações / Push Notification",
      "status": "Em fase de validação",
      "validado_por": "",
      "Turno": "Manhã",
      "Líder Técnico": "",
      "Técnico responsável": "PAULO GEOVANNI SCORSI DOS SANTOS",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-30T10:00:00Z",
      "Horário de fim": "",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": []
    },
    {
      "chave": "CHG0339456",
      "data_hora": "2024-06-29T16:00:00Z",
      "descricao": "ALEXANDRE MACHADO HOEPNER - CHG0339456 - PIER-1459 - Servico Tokenizacao",
      "status": "Sucesso",
      "validado_por": "DS ALEXANDRE MACHADO HOEPNER",
      "Turno": "Tarde",
      "Líder Técnico": "",
      "Técnico responsável": "ALEXANDRE MACHADO HOEPNER",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-29T16:00:00Z",
      "Horário de fim": "",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": [
        "DS ALEXANDRE MACHADO HOEPNER"
      ]
    },
    {
      "chave": "CHG0340571",
      "data_hora": "2024-06-30T11:00:00Z",
      "descricao": "FELIPE ANTONIO DE SOUZA - CHG0340571 - [BIA] Atendimento à Resolução BCB nº 215 de 03/08/2022 - Procedimentos - Elaboração de procedimento interno contendo o processo de recebimento de pedidos de informações.",
      "status": "Sucesso",
      "validado_por": "DS LUIS FERNANDO GUGLIELMO",
      "Turno": "Manhã",
      "Líder Técnico": "",
      "Técnico responsável": "FELIPE ANTONIO DE SOUZA",
      "Ocorrência": "",
      "Registro Incidente": "",
      "Horário de início": "2024-06-30T11:00:00Z",
      "Horário de fim": "",
      "Impacto": "",
      "Causa Raiz": "",
      "Ações": [
        "",
        "",
        ""
      ],
      "Mudança relacionada": "",
      "Envolvidos": [
        "DS LUIS FERNANDO GUGLIELMO"
      ]
    },
    # Adicione mais registros conforme necessário
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
