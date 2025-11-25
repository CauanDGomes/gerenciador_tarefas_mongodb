from database.database import Database

class AnexoController:
    def __init__(self, db: Database):
        self.db = db
        self.col = db.get_collection("anexos")

    def create(self, tarefa_id: int, nome_arquivo: str, tipo_arquivo: str | None, caminho: str) -> dict:
        novo_id = self.db.next_id("anexos")
        doc = {"id": novo_id, "tarefa_id": tarefa_id, "nome_arquivo": nome_arquivo, "tipo_arquivo": tipo_arquivo, "caminho": caminho}
        self.col.insert_one(doc)
        return doc

    def list_by_tarefa(self, tarefa_id: int) -> list:
        return list(self.col.find({"tarefa_id": tarefa_id}, {"_id": 0}))

    def delete_by_tarefa(self, tarefa_id: int) -> int:
        res = self.col.delete_many({"tarefa_id": tarefa_id})
        return res.deleted_count

    def count_all(self) -> int:
        return int(self.col.count_documents({}))
