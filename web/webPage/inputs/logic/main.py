from typing import Optional

from fastapi import FastAPI
from joblib import load
import pandas as pd
import json

from DataModel2 import DataModel2
from DataModel2 import JsonInput
from sklearn.metrics import mean_squared_error as mse

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: JsonInput):
      print("inicio")
      petition_dict = dataModel
      print("1")
      print(petition_dict)
      #results = proccess(petition_dict)
      results = proccess(petition_dict)
      return {"result": results}


def proccess(petition_dict):
   results = []
   model = load("../../modelo2.joblib")
   for petition in petition_dict:
      for pet in petition[1]:
         #print(pet)
         
         df = pd.DataFrame(pet, index=[1])
         
         print(df.dtypes)
         #df.columns = dataModel.columns()
         
         #print("llego 1")
         result = model.predict(df['text'])
         
         #print("llego 2")
         #print(result[0])
         results.append(result[0])
   print(results)
   return results




