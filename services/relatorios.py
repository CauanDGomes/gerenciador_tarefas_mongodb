from database.database import Database
from controllers.usuario_controller import UsuarioController
from controllers.categoria_controller import CategoriaController
from controllers.tarefa_controller import TarefaController
from controllers.comentario_controller import ComentarioController

class Relatorios:
    def __init__(self, db: Database):
        self.db = db
        self.usuario_ctrl = UsuarioController(db)
        self.categoria_ctrl = CategoriaController(db)
        self.tarefa_ctrl = TarefaController(db)
        self.comentario_ctrl = ComentarioController(db)
        
        self.tarefas_col = db.get_collection("tarefas")
        self.usuarios_col = db.get_collection("usuarios")
        self.categorias_col = db.get_collection("categorias")
        self.comentarios_col = db.get_collection("comentarios")

    def relatorio_tarefas_por_usuario(self):
        """
        Relatório com sumarização: Total de tarefas por usuário
        Utiliza aggregation pipeline com group
        """
        print("\n" + "=" * 70)
        print("RELATÓRIO: TAREFAS POR USUÁRIO")
        print("=" * 70)
        
        pipeline = [
            {
                "$group": {
                    "_id": "$id_usuario",
                    "total_tarefas": {"$sum": 1},
                    "pendentes": {"$sum": {"$cond": [{"$eq": ["$status", "pendente"]}, 1, 0]}},
                    "em_andamento": {"$sum": {"$cond": [{"$eq": ["$status", "em_andamento"]}, 1, 0]}},
                    "concluidas": {"$sum": {"$cond": [{"$eq": ["$status", "concluida"]}, 1, 0]}}
                }
            },
            {
                "$sort": {"total_tarefas": -1}
            }
        ]
        
        resultados = list(self.tarefas_col.aggregate(pipeline))
        
        if not resultados:
            print("\nNenhuma tarefa encontrada.")
        else:
            print(f"\n{'ID Usuário':<15} {'Total Tarefas':<20} {'Pendentes':<15} {'Em Andamento':<20} {'Concluídas':<15}")
            print("-" * 85)
            
            for resultado in resultados:
                usuario_id = resultado.get("_id", "N/A")
                usuario = self.usuario_ctrl.find(usuario_id)
                nome_usuario = usuario.get("nome", "N/A") if usuario else "N/A"
                
                print(f"{nome_usuario:<15} {resultado['total_tarefas']:<20} {resultado['pendentes']:<15} {resultado['em_andamento']:<20} {resultado['concluidas']:<15}")
        
        print("\n" + "=" * 70)

    def relatorio_tarefas_por_categoria(self):
        """
        Relatório com sumarização: Total de tarefas por categoria
        Utiliza aggregation pipeline com group
        """
        print("\n" + "=" * 70)
        print("RELATÓRIO: TAREFAS POR CATEGORIA")
        print("=" * 70)
        
        pipeline = [
            {
                "$group": {
                    "_id": "$categoria_id",
                    "total_tarefas": {"$sum": 1},
                    "pendentes": {"$sum": {"$cond": [{"$eq": ["$status", "pendente"]}, 1, 0]}},
                    "em_andamento": {"$sum": {"$cond": [{"$eq": ["$status", "em_andamento"]}, 1, 0]}},
                    "concluidas": {"$sum": {"$cond": [{"$eq": ["$status", "concluida"]}, 1, 0]}}
                }
            },
            {
                "$sort": {"total_tarefas": -1}
            }
        ]
        
        resultados = list(self.tarefas_col.aggregate(pipeline))
        
        if not resultados:
            print("\nNenhuma tarefa encontrada.")
        else:
            print(f"\n{'Categoria':<20} {'Total Tarefas':<20} {'Pendentes':<15} {'Em Andamento':<20} {'Concluídas':<15}")
            print("-" * 90)
            
            for resultado in resultados:
                cat_id = resultado.get("_id", "N/A")
                categoria = self.categoria_ctrl.find(cat_id)
                nome_categoria = categoria.get("nome", "N/A") if categoria else "N/A"
                
                print(f"{nome_categoria:<20} {resultado['total_tarefas']:<20} {resultado['pendentes']:<15} {resultado['em_andamento']:<20} {resultado['concluidas']:<15}")
        
        print("\n" + "=" * 70)

    def relatorio_tarefas_com_detalhes(self):
        """
        Relatório com junção de coleções: Tarefas com usuário, categoria e comentários
        Utiliza $lookup para juntar dados
        """
        print("\n" + "=" * 70)
        print("RELATÓRIO: TAREFAS COM DETALHES (Usuário, Categoria e Comentários)")
        print("=" * 70)
        
        pipeline = [
            {
                "$lookup": {
                    "from": "usuarios",
                    "localField": "id_usuario",
                    "foreignField": "id",
                    "as": "usuario_info"
                }
            },
            {
                "$lookup": {
                    "from": "categorias",
                    "localField": "categoria_id",
                    "foreignField": "id",
                    "as": "categoria_info"
                }
            },
            {
                "$lookup": {
                    "from": "comentarios",
                    "localField": "id",
                    "foreignField": "tarefa_id",
                    "as": "comentarios"
                }
            },
            {
                "$project": {
                    "id": 1,
                    "titulo": 1,
                    "status": 1,
                    "usuario_nome": {"$arrayElemAt": ["$usuario_info.nome", 0]},
                    "categoria_nome": {"$arrayElemAt": ["$categoria_info.nome", 0]},
                    "total_comentarios": {"$size": "$comentarios"}
                }
            },
            {
                "$sort": {"id": 1}
            }
        ]
        
        resultados = list(self.tarefas_col.aggregate(pipeline))
        
        if not resultados:
            print("\nNenhuma tarefa encontrada.")
        else:
            print(f"\n{'ID':<8} {'Título':<30} {'Status':<15} {'Usuário':<20} {'Categoria':<20} {'Comentários':<15}")
            print("-" * 108)
            
            for resultado in resultados:
                tarefa_id = resultado.get("id", "N/A")
                titulo = resultado.get("titulo", "N/A")[:28]
                status = resultado.get("status", "N/A")
                usuario = resultado.get("usuario_nome", "N/A")[:18]
                categoria = resultado.get("categoria_nome", "N/A")[:18]
                comentarios = resultado.get("total_comentarios", 0)
                
                print(f"{tarefa_id:<8} {titulo:<30} {status:<15} {usuario:<20} {categoria:<20} {comentarios:<15}")
        
        print("\n" + "=" * 70)

    def exibir_menu_relatorios(self):
        """Menu para escolher qual relatório exibir"""
        while True:
            print("\n" + "=" * 70)
            print("RELATÓRIOS")
            print("=" * 70)
            print("\n1. Tarefas por Usuário (Sumarização)")
            print("2. Tarefas por Categoria (Sumarização)")
            print("3. Tarefas com Detalhes (Junção de Coleções)")
            print("4. Voltar ao Menu Principal")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.relatorio_tarefas_por_usuario()
            elif opcao == "2":
                self.relatorio_tarefas_por_categoria()
            elif opcao == "3":
                self.relatorio_tarefas_com_detalhes()
            elif opcao == "4":
                break
            else:
                print("Opção inválida!")
