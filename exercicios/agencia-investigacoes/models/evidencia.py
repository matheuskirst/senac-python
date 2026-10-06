from dataclasses import dataclass

@dataclass
class Evidencia:
    id: int
    caso_id: int
    suspeito_id: int
    descricao: str

    class Campo:
        id = 'id'
        caso_id = 'caso_id'
        suspeito_id = 'suspeito_id'
        descricao = 'descricao'
