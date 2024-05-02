# -*- coding: utf-8 -*-
'''

@authot:B_Menisy

'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Age : int
    Sex : int
    Cp : int
    Trestbps : int
    Chol : int
    Fbs : int
    Restecg : int
    Thalach : int
    Exang : int
    Oldpeak : float
    Slope : int
    Ca : int
    Thal : int
    
    

# loading the saved model
heart_disease_model = pickle.load(open(r'heart_disease_model.sav','rb'))


@app.post('/heart_disease_prediction')
def heart_disease_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    age = input_dictionary['Age']
    sex = input_dictionary['Sex']
    cp = input_dictionary['Cp']
    trestbps = input_dictionary['Trestbps']
    Chol = input_dictionary['Chol']
    Fbs = input_dictionary['Fbs']
    Restecg = input_dictionary['Restecg']
    Thalach = input_dictionary['Thalach']
    Exang = input_dictionary['Exang']
    Oldpeak = input_dictionary['Oldpeak']
    Slope = input_dictionary['Slope']
    Ca = input_dictionary['Ca']
    Thal = input_dictionary['Thal']
    


    input_list = [age, sex, cp, trestbps, Chol, Fbs, Restecg,Thalach, Exang, Oldpeak, Slope, Ca, Thal]
    
    prediction = heart_disease_model.predict([input_list])
    
    if prediction[0] == 0:
        return "We are sorry , You have been diagnosed with heart attack."
    
    else:
        return 'Congratulations , You have been not diagnosed with heart attack.'


