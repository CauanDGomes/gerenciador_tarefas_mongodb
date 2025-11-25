from database.database import Database

class CategoriaController:
    def __init__(self, db: Database):
        self.db = db
        self.col = db.get_collection("categorias")

    def create(self, nome: str, descricao: str | None = None) -> dict:
        novo_id = self.db.next_id("categorias")
        doc = {"id": novo_id, "nome": nome, "descricao": descricao}
        self.col.insert_one(doc)
        return doc

    def list_all(self) -> list:
        return list(self.col.find({}, {"_id": 0}))

    def find(self, id_cat: int) -> dict | None:
        return self.col.find_one({"id": id_cat}, {"_id": 0})

    def update(self, id_cat: int, dados: dict) -> dict | None:
        self.col.update_one({"id": id_cat}, {"$set": dados})
        return self.find(id_cat)

    def delete(self, id_cat: int) -> int:
        res = self.col.delete_one({"id": id_cat})
        return res.deleted_count

    def count_all(self) -> int:
        return int(self.col.count_documents({}))
