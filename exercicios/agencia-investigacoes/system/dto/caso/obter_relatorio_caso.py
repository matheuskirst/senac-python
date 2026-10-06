from dataclasses import dataclass
from dto import ObterDescricaoSuspeito

@dataclass(frozen=True)
class ObterRelatorioCaso:
    titulo: str
    local: str
    suspeitos: list[ObterDescricaoSuspeito] | None
