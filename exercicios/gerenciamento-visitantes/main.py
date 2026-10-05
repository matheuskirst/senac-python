import os
from dotenv import load_dotenv

from data import AppContext
from services import VisitantesService
from view import SistemaView
from models import Visitante
from libraries import DataclassInstance

def main():
    app_context = AppContext()
    visitantes_service = VisitantesService(contexto=app_context)

    sistema_view = SistemaView(visitantes_service=visitantes_service)

    sistema_view.run()

if __name__ == "__main__":
    main()
