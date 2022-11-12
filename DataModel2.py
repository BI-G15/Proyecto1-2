from pydantic import BaseModel
from typing import List

class DataModel2(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.

    serial_no: float
    gre_score: float
    toefl_score: float
    university_rating: float
    sop: float
    lor: float 
    cgpa: float
    research: float
    Admission_Points: float

class JsonInput2 (BaseModel):
    list_of_inputs: List[dict]
    
#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["Serial No.","GRE Score","TOEFL Score","University Rating","SOP","LOR" ,"CGPA","Research","Admission Points"]
