from database.database import Database

class TarefaController:
    def __init__(self, db: Database):
        self.db = db
        self.col = db.get_collection("tarefas")
        self.coment_col = db.get_collection("comentarios")
        self.anexo_col = db.get_collection("anexos")
        self.tempo_col = db.get_collection("tempos_gastos")

    def create(self, titulo: str, descricao: str | None, id_usuario: int, categoria_id: int, data_inicio: str | None = None, data_fim: str | None = None) -> dict:
        novo_id = self.db.next_id("tarefas")
        doc = {
            "id": novo_id,
            "titulo": titulo,
            "descricao": descricao,
            "data_inicio": data_inicio,
            "data_fim": data_fim,
            "status": "pendente",
            "tempo_gasto": 0.0,
            "id_usuario": id_usuario,
            "categoria_id": categoria_id
        }
        self.col.insert_one(doc)
        return doc

    def list_all(self) -> list:
        return list(self.col.find({}, {"_id": 0}))

    def find(self, id_tarefa: int) -> dict | None:
        return self.col.find_one({"id": id_tarefa}, {"_id": 0})

    def update(self, id_tarefa: int, dados: dict) -> dict | None:
        self.col.update_one({"id": id_tarefa}, {"$set": dados})
        return self.find(id_tarefa)

    def delete(self, id_tarefa: int, cascade: bool = False) -> int:
        if cascade:
            self.coment_col.delete_many({"tarefa_id": id_tarefa})
            self.anexo_col.delete_many({"tarefa_id": id_tarefa})
            self.tempo_col.delete_many({"tarefa_id": id_tarefa})
        res = self.col.delete_one({"id": id_tarefa})
        return res.deleted_count

    def count_by_usuario(self, id_usuario: int) -> int:
        return int(self.col.count_documents({"id_usuario": id_usuario}))

    def count_by_categoria(self, categoria_id: int) -> int:
        return int(self.col.count_documents({"categoria_id": categoria_id}))

    def count_all(self) -> int:
        return int(self.col.count_documents({}))
