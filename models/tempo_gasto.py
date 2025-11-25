from dataclasses import dataclass

@dataclass
class TempoGasto:
    id: int
    tarefa_id: int
    horas: float
    data_registro: str | None = None
