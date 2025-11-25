from database.database import Database

class TempoGastoController:
    def __init__(self, db: Database):
        self.db = db
        self.col = db.get_collection("tempos_gastos")

    def create(self, tarefa_id: int, horas: float, data_registro: str | None = None) -> dict:
        novo_id = self.db.next_id("tempos_gastos")
        doc = {"id": novo_id, "tarefa_id": tarefa_id, "horas": horas, "data_registro": data_registro}
        self.col.insert_one(doc)
        return doc

    def list_by_tarefa(self, tarefa_id: int) -> list:
        return list(self.col.find({"tarefa_id": tarefa_id}, {"_id": 0}))

    def delete_by_tarefa(self, tarefa_id: int) -> int:
        res = self.col.delete_many({"tarefa_id": tarefa_id})
        return res.deleted_count

    def count_all(self) -> int:
        return int(self.col.count_documents({}))
