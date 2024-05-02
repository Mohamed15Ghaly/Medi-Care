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
    
    clump_thickness : int
    uniform_cell_size : int
    uniform_cell_shape : int
    marginal_adhesion : int
    single_epithelial_size : int
    bare_nuclei : int
    bland_chromatin : int
    normal_nucleoli : int
    mitoses : int


# loading the saved model
Breast_cancer_model = pickle.load(open(r'Breast_cancer.pkl','rb'))


@app.post('/Breast_cancer_prediction')
def Breast_cancer_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    Clump_thickness = input_dictionary['clump_thickness']
    Uniform_cell_size = input_dictionary['uniform_cell_size']
    Uniform_cell_shape = input_dictionary['uniform_cell_shape']
    Marginal_adhesion = input_dictionary['marginal_adhesion']
    Single_epithelial_size = input_dictionary['single_epithelial_size']
    Bare_nuclei = input_dictionary['bare_nuclei']
    Bland_chromatin = input_dictionary['bland_chromatin']
    Normal_nucleoli = input_dictionary['normal_nucleoli']
    Mitoses = input_dictionary['mitoses']
    

    input_list = [Clump_thickness, Uniform_cell_size, Uniform_cell_shape, Marginal_adhesion, Single_epithelial_size
                  , Bare_nuclei, Bland_chromatin,Normal_nucleoli, Mitoses]
    
    prediction = Breast_cancer_model.predict([input_list])
    
    if prediction[0] == 2:
        return "We are sorry , You have been diagnosed with benign tumor."
    
    else:
        return 'Congratulations , You have been not diagnosed with malignant tumor.'


