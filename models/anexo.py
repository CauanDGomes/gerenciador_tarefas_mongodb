from dataclasses import dataclass

@dataclass
class Anexo:
    id: int
    tarefa_id: int
    nome_arquivo: str
    tipo_arquivo: str | None
    caminho: str
