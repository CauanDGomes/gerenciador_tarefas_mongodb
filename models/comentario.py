from dataclasses import dataclass

@dataclass
class Comentario:
    id: int
    tarefa_id: int
    usuario_id: int
    texto: str
    data_comentario: str | None = None
