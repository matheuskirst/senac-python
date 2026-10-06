from dataclasses import dataclass

@dataclass(frozen=True)
class ObterDescricaoSuspeito:
    nome: str
    idade: int
    evidencias: int
