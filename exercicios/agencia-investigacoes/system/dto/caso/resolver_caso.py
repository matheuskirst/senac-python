from dataclasses import dataclass

@dataclass(frozen=True)
class ResolverCaso:
    caso_id: int
    suspeito_id: int
