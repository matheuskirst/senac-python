from dataclasses import dataclass

@dataclass(frozen=True)
class AdicionarSuspeito:
    caso_id: int
    nome: str
    idade: int
    evidencias_ids: list[int] | None
