from typing import Optional

from fastapi import FastAPI
from joblib import load
import pandas as pd
import json

from DataModel import DataModel
from DataModel import JsonInput
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
      results = proccess(petition_dict)
      return {"result": results}

@app.post("/newData")
def make_predictions(dataModel: JsonInput):
      print("inicio")
      petition_dict = dataModel
      print(petition_dict)
      dictRest = proccess2(petition_dict)
      return dictRest

def proccess(petition_dict):
   results = []
   for petition in petition_dict:
      for pet in petition[1]:
         print(pet)
         petition = pet
         df = pd.DataFrame(petition, index=[0])
         print(df)
         #df.columns = dataModel.columns()
         model = load("assets/modelo.joblib")
         print("llego 1")
         result = model.predict(df)
         print("llego 2")
         print(result[0])
         results.append(result[0])
   print(results)
   return results

def proccess2(petition_dict):
   frames = []
   model = load("assets/modelo.joblib")
   for petition in petition_dict:
      for pet in petition[1]:
         petition = pet
         df = pd.DataFrame(petition, index=[0])
         frames.append(df.copy())
   df = pd.concat(frames)
   print(df)
   x = df.drop('Admission Points', axis = 1)
   y = df['Admission Points']
   pipe = model.fit(x,y)
   r2 = pipe.score(x,y)
   y_predicted = pipe.predict(x)
   rmse = (mse(y, y_predicted))**(1/2)
   return {"RMSE": rmse, "R^2": r2}