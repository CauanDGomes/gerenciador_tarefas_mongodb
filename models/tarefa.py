from dataclasses import dataclass

@dataclass
class Tarefa:
    id: int
    titulo: str
    descricao: str | None
    data_inicio: str | None = None
    data_fim: str | None = None
    status: str = "pendente"
    tempo_gasto: float = 0.0
    id_usuario: int | None = None
    categoria_id: int | None = None
