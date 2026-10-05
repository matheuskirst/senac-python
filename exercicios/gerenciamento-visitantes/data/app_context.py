import os
from dotenv import load_dotenv

from libraries import JsonContext
from models import Visitante

class AppContext(JsonContext):
    def __init__(self) -> None:
        super().__init__()

        load_dotenv()
        visitantes_json = os.getenv("VISITANTES_JSON")

        self.visitantes = self.JsonSet(model_class=Visitante, json_path=visitantes_json)
