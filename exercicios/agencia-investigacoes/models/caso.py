from dataclasses import dataclass

@dataclass
class Caso:
    id: int
    titulo: str
    local: str
    suspeitos_ids: list[int] | None
    is_resolvido: bool
    data_criacao: str
    data_resolucao: str | None

    class Campo:
        id = 'id'
        titulo = 'titulo'
        local = 'local'
        suspeitos_ids = 'suspeitos_ids'
        is_resolvido = 'is_resolvido'
        data_criacao = 'data_criacao'
        data_resolucao = 'data_resolucao'
