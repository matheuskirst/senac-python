from dataclasses import dataclass

@dataclass(frozen=True)
class RegistrarEvidencia:
    caso_id: int
    suspeito_id: int
    descricao: str
