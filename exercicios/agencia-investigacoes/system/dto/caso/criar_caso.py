from dataclasses import dataclass

@dataclass(frozen=True)
class CriarCaso:
    titulo: str
    local: str
