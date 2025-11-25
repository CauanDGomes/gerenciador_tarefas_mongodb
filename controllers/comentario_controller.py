from database.database import Database

class ComentarioController:
    def __init__(self, db: Database):
        self.db = db
        self.col = db.get_collection("comentarios")

    def create(self, tarefa_id: int, usuario_id: int, texto: str, data_comentario: str | None = None) -> dict:
        novo_id = self.db.next_id("comentarios")
        doc = {"id": novo_id, "tarefa_id": tarefa_id, "usuario_id": usuario_id, "texto": texto, "data_comentario": data_comentario}
        self.col.insert_one(doc)
        return doc

    def list_by_tarefa(self, tarefa_id: int) -> list:
        return list(self.col.find({"tarefa_id": tarefa_id}, {"_id": 0}))

    def delete_by_tarefa(self, tarefa_id: int) -> int:
        res = self.col.delete_many({"tarefa_id": tarefa_id})
        return res.deleted_count

    def count_all(self) -> int:
        return int(self.col.count_documents({}))
