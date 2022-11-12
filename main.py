from typing import Optional

from fastapi import FastAPI
from joblib import load, dump
import pandas as pd
import json

from DataModel import DataModel
from DataModel import JsonInput
from DataModel2 import DataModel2
from DataModel2 import JsonInput2
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
      petition_dict = dataModel
      results = proccess(petition_dict)
      return {"result": results}

import string
punctuation = set(string.punctuation)
def tokenize(sentence):
    tokens = []
    for token in sentence.split():
        new_token = []
        for character in token:
            if character not in punctuation:
                new_token.append(character.lower())
        if new_token:
            tokens.append("".join(new_token))
    return tokens

def proccess(petition_dict):
   results = []
   for petition in petition_dict:
      for pet in petition[1]:
         petition = pet
         df = pd.DataFrame(petition, index=[0])
         model = load("modelo.joblib")
         result = model.predict(df)
         results.append(result[0])
   return results

@app.post("/newData")
def make_predictions(dataModel: JsonInput2):
      petition_dict = dataModel
      dictRest = proccess2(petition_dict)
      return dictRest

def proccess2(petition_dict):
   frames = []
   model = load("modelo.joblib")
   for petition in petition_dict:
      for pet in petition[1]:
         petition = pet
         df = pd.DataFrame(petition, index=[0])
         frames.append(df.copy())
   df = pd.concat(frames)
   x = df.drop('Admission Points', axis = 1)
   y = df['Admission Points']
   pipe = model.fit(x,y)
   r2 = pipe.score(x,y)
   y_predicted = pipe.predict(x)
   rmse = (mse(y, y_predicted))**(1/2)
   dump(pipe, "modelo.joblib")
   return {"RMSE": rmse, "R^2": r2}