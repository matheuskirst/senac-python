from dataclasses import dataclass

@dataclass
class Suspeito:
    id: int
    caso_id: int
    nome: str
    idade: int
    quantidade_evidencias: int

    class Campo:
        id = 'id'
        caso_id = 'caso_id'
        nome = 'nome'
        idade = 'idade'
        quantidade_evidencias = 'quantidade_evidencias'
