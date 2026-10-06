from datetime import datetime

from data import AppContext
from dto import CriarCaso, ResolverCaso, ObterRelatorioCaso, AdicionarSuspeito, ObterDescricaoSuspeito, RegistrarEvidencia
from models import Caso, Suspeito, Evidencia

class CasosService:
    def __init__(self, contexto: AppContext) -> None:
        self.contexto = contexto

    def criar_caso(self, criar_caso_dto: CriarCaso):
        id = self.contexto.suspeitos.count() + 1
        caso = Caso(
            id=id,
            titulo=criar_caso_dto.titulo,
            local=criar_caso_dto.local,
            suspeitos_ids=None,
            is_resolvido=False,
            data_criacao=datetime.strftime(datetime.now(), "%d/%m/%Y"),
            data_resolucao=None
        )

        self.contexto.casos.add(caso)
        self.contexto.casos.save_changes()

    def adicionar_suspeito(self, adicionar_suspeito_dto: AdicionarSuspeito):
        id = self.contexto.suspeitos.count() + 1
        suspeito = Suspeito(
            id=id,
            caso_id=adicionar_suspeito_dto.caso_id,
            nome=adicionar_suspeito_dto.nome,
            idade=adicionar_suspeito_dto.idade,
            quantidade_evidencias=0
        )

        self.contexto.casos.where(lambda c: c.id == adicionar_suspeito_dto.caso_id).update(Caso.Campo.suspeitos_ids, "")

        self.contexto.suspeitos.add(suspeito)
        self.contexto.suspeitos.save_changes()

    def registrar_evidencia(self, registrar_evidencia_dto: RegistrarEvidencia):
        suspeito = self.contexto.suspeitos.where(lambda s: s.id == registrar_evidencia_dto.suspeito_id).first()

        if not suspeito:
            return None

        id = self.contexto.evidencias.count() + 1
        evidencia = Evidencia(
            id=id,
            caso_id=registrar_evidencia_dto.caso_id,
            suspeito_id=suspeito.id,
            descricao=registrar_evidencia_dto.descricao
        )

        self.contexto.suspeitos.where(lambda s: s.id == suspeito.id).update(field=Suspeito.Campo.quantidade_evidencias, value=suspeito.quantidade_evidencias + 1)

        self.contexto.evidencias.add(evidencia)

        self.contexto.evidencias.save_changes()
        self.contexto.suspeitos.save_changes()

    def resolver_caso(self, resolver_caso_dto: ResolverCaso):
        caso_id = resolver_caso_dto.caso_id
        suspeito_id = resolver_caso_dto.suspeito_id

        caso = self.contexto.casos.where(lambda c: c.id == caso_id).first()

        if not caso:
            return None

        suspeito = self.contexto.suspeitos.where(lambda s: s.id == suspeito_id and s.caso_id == caso_id).first()

        if not suspeito:
            return None
        
        maior_suspeito = self.contexto.suspeitos.where(lambda s: s.caso_id == caso_id).order_by_descending(Suspeito.Campo.quantidade_evidencias).first()

        if not maior_suspeito:
            return None

        if suspeito.id != maior_suspeito.id:
            return False

        self.contexto.casos.where(lambda c: c.id == caso.id).update(field=Caso.Campo.is_resolvido, value=True)
        self.contexto.casos.save_changes()

        return True

    def obter_caso_relatorio(self, caso_id: int) -> ObterRelatorioCaso | None:
        caso = self.contexto.casos.where(lambda c: c.id == caso_id).first()

        if not caso:
            return None

        suspeitos = self.contexto.suspeitos.where(lambda s: s.caso_id == caso.id).to_list()

        lista_descricao_suspeito: list[ObterDescricaoSuspeito] = []
        if suspeitos:
            for suspeito in suspeitos:
                suspeito_evidencias = self.contexto.evidencias.where(lambda e: e.caso_id == caso.id and e.suspeito_id == suspeito.id).count()
                descricao_suspeito = ObterDescricaoSuspeito(
                    nome= suspeito.nome,
                    idade=suspeito.idade,
                    evidencias=suspeito_evidencias
                )
                lista_descricao_suspeito.append(descricao_suspeito)

        relatorio = ObterRelatorioCaso(
            titulo=caso.titulo,
            local=caso.local,
            suspeitos=lista_descricao_suspeito
        )

        return relatorio
