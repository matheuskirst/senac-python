import os
from dotenv import load_dotenv
from libraries import JsonContext
from models import Caso, Suspeito, Evidencia

class AppContext(JsonContext):
    def __init__(self) -> None:
        super().__init__()
        load_dotenv()

        casos_json = os.getenv("CASOS_JSON")
        suspeitos_json = os.getenv("SUSPEITOS_JSON")
        evidencias_json = os.getenv("EVIDENCIAS_JSON")

        self.casos = self.JsonSet(model_class=Caso, json_path=casos_json)
        self.suspeitos = self.JsonSet(model_class=Suspeito, json_path=suspeitos_json)
        self.evidencias = self.JsonSet(model_class=Evidencia,  json_path=evidencias_json)
