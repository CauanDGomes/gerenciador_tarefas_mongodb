"""
Script para limpar o banco de dados MongoDB
Execute este arquivo para remover todos os dados
"""

from pymongo import MongoClient

def limpar_banco():
    # Conectar ao MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["sistema_tarefas"]
    
    # Listar todas as coleções
    colecoes = db.list_collection_names()
    
    print("=" * 60)
    print("LIMPANDO BANCO DE DADOS: sistema_tarefas")
    print("=" * 60)
    
    for colecao in colecoes:
        quantidade = db[colecao].count_documents({})
        if quantidade > 0:
            db[colecao].delete_many({})
            print(f"✓ Coleção '{colecao}': {quantidade} documento(s) removido(s)")
        else:
            print(f"✓ Coleção '{colecao}': vazia")
    
    # Limpar contador
    db["counters"].delete_many({})
    print(f"✓ Coleção 'counters': resetada")
    
    print("=" * 60)
    print("✅ Banco de dados limpo com sucesso!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        limpar_banco()
    except Exception as e:
        print(f"❌ Erro ao limpar banco: {e}")
        print("Certifique-se de que MongoDB está rodando na porta 27017")
