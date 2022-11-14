from typing import Optional

from fastapi import FastAPI
from joblib import load

from .DataModel import DataModel
from .DataModel import JsonInput

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: JsonInput):
      petition_dict = dataModel
      results = proccess(petition_dict)
      return {"result": results}

def proccess(petition):
    print(petition)
    model = load("modelo2.joblib")
    result = model.predict([petition])
    print(result[0])
    return result[0]
