"""
Script para popular o banco com dados de exemplo para vídeo demonstrativo
"""

from pymongo import MongoClient

def popular_banco_exemplo():
    # Conectar ao MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["sistema_tarefas"]
    
    print("=" * 60)
    print("POPULANDO BANCO COM DADOS DE EXEMPLO")
    print("=" * 60)
    
    # Limpar dados existentes
    for colecao in db.list_collection_names():
        db[colecao].delete_many({})
    
    # === USUÁRIOS ===
    usuarios_col = db["usuarios"]
    usuarios = [
        {"id": 1, "nome": "João Silva", "email": "joao@email.com", "senha": "123456"},
        {"id": 2, "nome": "Maria Santos", "email": "maria@email.com", "senha": "abc123"},
        {"id": 3, "nome": "Pedro Oliveira", "email": "pedro@email.com", "senha": "senha123"},
    ]
    usuarios_col.insert_many(usuarios)
    print(f"✓ {len(usuarios)} usuário(s) criado(s)")
    
    # === CATEGORIAS ===
    categorias_col = db["categorias"]
    categorias = [
        {"id": 1, "nome": "Trabalho", "descricao": "Tarefas relacionadas ao trabalho"},
        {"id": 2, "nome": "Estudos", "descricao": "Tarefas de estudo e pesquisa"},
        {"id": 3, "nome": "Pessoal", "descricao": "Tarefas pessoais e lazer"},
        {"id": 4, "nome": "Projeto", "descricao": "Tarefas do projeto C3"},
    ]
    categorias_col.insert_many(categorias)
    print(f"✓ {len(categorias)} categoria(s) criada(s)")
    
    # === TAREFAS ===
    tarefas_col = db["tarefas"]
    tarefas = [
        {
            "id": 1,
            "titulo": "Implementar API REST",
            "descricao": "Criar endpoints para gerenciar tarefas",
            "data_inicio": "2025-11-20",
            "data_fim": "2025-11-25",
            "status": "em_andamento",
            "tempo_gasto": 15.5,
            "id_usuario": 1,
            "categoria_id": 4
        },
        {
            "id": 2,
            "titulo": "Estudar MongoDB",
            "descricao": "Aprender agregação e lookup em MongoDB",
            "data_inicio": "2025-11-15",
            "data_fim": "2025-11-30",
            "status": "pendente",
            "tempo_gasto": 8.0,
            "id_usuario": 2,
            "categoria_id": 2
        },
        {
            "id": 3,
            "titulo": "Fazer apresentação",
            "descricao": "Preparar slides do projeto C3",
            "data_inicio": "2025-11-22",
            "data_fim": "2025-11-28",
            "status": "concluida",
            "tempo_gasto": 5.0,
            "id_usuario": 1,
            "categoria_id": 4
        },
        {
            "id": 4,
            "titulo": "Reunião com cliente",
            "descricao": "Discutir requisitos do novo projeto",
            "data_inicio": "2025-11-25",
            "data_fim": "2025-11-25",
            "status": "pendente",
            "tempo_gasto": 0.0,
            "id_usuario": 3,
            "categoria_id": 1
        },
    ]
    tarefas_col.insert_many(tarefas)
    print(f"✓ {len(tarefas)} tarefa(s) criada(s)")
    
    # === COMENTÁRIOS ===
    comentarios_col = db["comentarios"]
    comentarios = [
        {
            "id": 1,
            "tarefa_id": 1,
            "usuario_id": 1,
            "texto": "Iniciamos o desenvolvimento da API",
            "data_comentario": "2025-11-20"
        },
        {
            "id": 2,
            "tarefa_id": 1,
            "usuario_id": 2,
            "texto": "Já temos 50% implementado",
            "data_comentario": "2025-11-23"
        },
        {
            "id": 3,
            "tarefa_id": 2,
            "usuario_id": 2,
            "texto": "Finalizei a leitura do capítulo 3",
            "data_comentario": "2025-11-24"
        },
    ]
    comentarios_col.insert_many(comentarios)
    print(f"✓ {len(comentarios)} comentário(s) criado(s)")
    
    # === ANEXOS ===
    anexos_col = db["anexos"]
    anexos = [
        {
            "id": 1,
            "tarefa_id": 1,
            "nome_arquivo": "requisitos_api.pdf",
            "tipo_arquivo": ".pdf",
            "caminho": "/documentos/requisitos_api.pdf"
        },
        {
            "id": 2,
            "tarefa_id": 3,
            "nome_arquivo": "slides_c3.pptx",
            "tipo_arquivo": ".pptx",
            "caminho": "/documentos/slides_c3.pptx"
        },
    ]
    anexos_col.insert_many(anexos)
    print(f"✓ {len(anexos)} anexo(s) criado(s)")
    
    # === TEMPOS GASTOS ===
    tempos_col = db["tempos_gastos"]
    tempos = [
        {
            "id": 1,
            "tarefa_id": 1,
            "horas": 5.0,
            "data_registro": "2025-11-20"
        },
        {
            "id": 2,
            "tarefa_id": 1,
            "horas": 5.5,
            "data_registro": "2025-11-21"
        },
        {
            "id": 3,
            "tarefa_id": 1,
            "horas": 5.0,
            "data_registro": "2025-11-23"
        },
        {
            "id": 4,
            "tarefa_id": 2,
            "horas": 8.0,
            "data_registro": "2025-11-24"
        },
        {
            "id": 5,
            "tarefa_id": 3,
            "horas": 5.0,
            "data_registro": "2025-11-22"
        },
    ]
    tempos_col.insert_many(tempos)
    print(f"✓ {len(tempos)} registro(s) de tempo gasto criado(s)")
    
    # === COUNTERS ===
    counters_col = db["counters"]
    counters = [
        {"_id": "usuarios", "seq": 3},
        {"_id": "categorias", "seq": 4},
        {"_id": "tarefas", "seq": 4},
        {"_id": "comentarios", "seq": 3},
        {"_id": "anexos", "seq": 2},
        {"_id": "tempos_gastos", "seq": 5},
    ]
    counters_col.insert_many(counters)
    print(f"✓ Contadores inicializados")
    
    print("=" * 60)
    print("✅ Banco populado com sucesso!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        popular_banco_exemplo()
    except Exception as e:
        print(f"❌ Erro ao popular banco: {e}")
        print("Certifique-se de que MongoDB está rodando na porta 27017")
