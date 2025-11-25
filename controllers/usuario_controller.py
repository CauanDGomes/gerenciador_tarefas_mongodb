from database.database import Database

class UsuarioController:
    def __init__(self, db: Database):
        self.db = db
        self.col = db.get_collection("usuarios")

    def create(self, nome: str, email: str, senha: str) -> dict:
        novo_id = self.db.next_id("usuarios")
        doc = {"id": novo_id, "nome": nome, "email": email, "senha": senha}
        self.col.insert_one(doc)
        return doc

    def list_all(self) -> list:
        return list(self.col.find({}, {"_id": 0}))

    def find(self, id_usuario: int) -> dict | None:
        return self.col.find_one({"id": id_usuario}, {"_id": 0})

    def update(self, id_usuario: int, dados: dict) -> dict | None:
        self.col.update_one({"id": id_usuario}, {"$set": dados})
        return self.find(id_usuario)

    def delete(self, id_usuario: int) -> int:
        res = self.col.delete_one({"id": id_usuario})
        return res.deleted_count

    def count_all(self) -> int:
        return int(self.col.count_documents({}))
