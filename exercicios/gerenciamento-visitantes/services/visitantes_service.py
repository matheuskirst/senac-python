import uuid
from typing import Any
from datetime import datetime

from data import AppContext
from enums import IngressoTipo, Ordenar
from models import Visitante
from utils import resolver_idade, resolver_ingresso_tipo

class VisitantesService:
    def __init__(self, contexto: AppContext):
        self.contexto = contexto

    def cadastrar_visitante(self, dados: dict):
        nome = dados["nome"]
        data_nascimento = datetime.strftime(dados["data_nascimento"], "%d/%m/%Y")
        idade = resolver_idade(dados["data_nascimento"])
        cpf = dados["cpf"]
        ingresso_tipo = dados["ingresso_tipo"]
        data_visita = datetime.strftime(dados["data_visita"], "%d/%m/%Y")

        cpfExiste = self.contexto.visitantes.where(lambda v: v.cpf == cpf).first()

        if cpfExiste:
            return {"Erro": "Já existe um visitante cadastrado com esse CPF.\n\nO cadastro não foi realizado."}

        numero_ingresso = str(uuid.uuid4())
        
        visitante = Visitante(
            nome = nome,
            data_nascimento = data_nascimento,
            idade = idade,
            cpf = cpf,
            ingresso_tipo = ingresso_tipo,
            data_visita = data_visita,
            numero_ingresso = numero_ingresso
        )

        self.contexto.visitantes.add(visitante)
        self.contexto.visitantes.save_changes()

        return {"Sucesso": "Visitante cadastrado com sucesso!"}

    def remover_visitante_por_cpf(self, cpf: str):
        try:
            visitante = self.contexto.visitantes.where(lambda v: v.cpf == cpf).first()

            if visitante == None:
                return {"Erro": "Visitante não encontrado"}

            self.contexto.visitantes.where(lambda v: v.cpf == cpf).delete()
            self.contexto.visitantes.save_changes()

            return {"Sucesso": f"Visitante: {visitante.nome}, CPF: '{visitante.cpf}' removido com sucesso!"}
        except:
            return {"Erro": "Ocorreu um erro interno."}

    def listar_todos(self):
        visitantes = self.contexto.visitantes.to_list()

        if not visitantes:
            return [{"Erro": "Não ha visitantes cadastrados."}]

        lista_visitantes_dados: list[dict[str, Any]] = []

        for visitante in visitantes:
            visitante_dados = {
                "Nome": visitante.nome,
                "Idade": f"{visitante.idade} anos",
                "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
            }
            lista_visitantes_dados.append(visitante_dados)

        return lista_visitantes_dados


    def listar_por_ingresso(self, ingresso:IngressoTipo):
        visitantes = self.contexto.visitantes.where(lambda v: v.ingresso_tipo == ingresso).to_list()

        if not visitantes:
            return [{"Erro": "Não ha visitantes cadastrados."}]

        lista_visitantes_dados = []

        for visitante in visitantes:
            visitante_dados = {
                "Nome": visitante.nome,
                "Idade": f"{visitante.idade} anos"
            }
            lista_visitantes_dados.append(visitante_dados)

        return lista_visitantes_dados

    def listar_por_ordem(self, ordem:Ordenar):
        visitantes = []
        match ordem:
            case Ordenar.Nome:
                visitantes = self.contexto.visitantes.order_by(Visitante.Campo.nome).to_list()
            case Ordenar.Idade:
                visitantes = self.contexto.visitantes.order_by(Visitante.Campo.idade).to_list()

        if not visitantes:
            return [{"Erro": "Não ha visitantes cadastrados."}]

        lista_visitantes_dados = []

        for visitante in visitantes:
            visitante_dados = {
                "Nome": visitante.nome,
                "Idade": f"{visitante.idade} anos",
                "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
            }
            lista_visitantes_dados.append(visitante_dados)

        return lista_visitantes_dados

    def consultar_por_cpf(self, cpf: str):
        try:
            visitante = self.contexto.visitantes.where(lambda v: v.cpf == cpf).first()

            if visitante == None:
                return {"Erro": "Visitante não encontrado"}

            visitante_dados = {
                "Nome": visitante.nome,
                "Idade": f"{visitante.idade} anos",
                "CPF": visitante.cpf,
                "Data de Nascimento": visitante.data_nascimento,
                "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
                "Data da visita": visitante.data_visita,
                "Número do ingresso": visitante.numero_ingresso
            }
            return visitante_dados

        except:
            return {"Erro": "Ocorreu um erro interno."}

    def consultar_por_data(self, data: str):
        visitantes = self.contexto.visitantes.where(lambda v: v.data_visita == data).to_list()

        if not visitantes:
            return [{"Erro": "Nenhum Visitante encontrado"}]

        visitantes_dados = []

        for visitante in visitantes:
            dados = {
                "Nome": visitante.nome,
                "Idade": f"{visitante.idade} anos",
                "CPF": visitante.cpf,
                "Data de Nascimento": visitante.data_nascimento,
                "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
                "Data da visita": visitante.data_visita,
                "Número do ingresso": visitante.numero_ingresso
            }
            visitantes_dados.append(dados)

        return visitantes_dados

    def obter_estatisticas(self):
        quantidade = self.contexto.visitantes.count()

        if quantidade == None or quantidade == 0:
            return {"Erro": "Não existem visitantes cadastrados para gerar estatísticas"}


        ingressos_normal = self.contexto.visitantes.where(lambda v: v.ingresso_tipo == IngressoTipo.Normal).count()
        ingressos_vip = self.contexto.visitantes.where(lambda v: v.ingresso_tipo == IngressoTipo.Vip).count()
        ingressos_premium = self.contexto.visitantes.where(lambda v: v.ingresso_tipo == IngressoTipo.Premium).count()

        idades: list[int] = self.contexto.visitantes.select(Visitante.Campo.idade)

        idade_media = sum(idades) / len(idades)

        estatisticas = {
            "Total de visitantes": quantidade,
            "Ingressos Normal": ingressos_normal,
            "Ingressos VIP": ingressos_vip,
            "Ingressos Premium": ingressos_premium,
            "Média de idade": round(idade_media, 2)
        }
        
        return estatisticas
