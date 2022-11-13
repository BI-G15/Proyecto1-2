from pydantic import BaseModel
from typing import List

class DataModel2(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.

    text: str
    

class JsonInput (BaseModel):
    list_of_inputs: List[dict]
    
#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["text"]
