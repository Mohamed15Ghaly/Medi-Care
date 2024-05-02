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
    
    MDVP_fo_HZ :  float
    MDVP_Fhi_HZ :  float
    MDVP_Flo_HZ :  float
    MDVP_Jitter_percentage :  float
    MDVP_Jitter_Abs :  float
    MDVP_RAP :  float
    MDVP_PPQ :  float
    Jitter_DDP :  float
    MDVP_Shimmer :  float
    MDVP_Shimmer_dB :  float
    Shimmer_APQ3 :  float
    Shimmer_APQ5 :  float
    MDVP_APQ :  float
    Shimmer_DDA :  float
    NHR :  float
    HNR :  float
    RPDE :  float
    DFA :  float
    spread1 :  float
    spread2 :  float
    D2 :  float
    PPE :  float
    

# loading the saved model
parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))


@app.post('/parkinson_prediction')
def parkinsons_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    mDVP_fo_HZ = input_dictionary['MDVP_fo_HZ']
    mDVP_Fhi_HZ = input_dictionary['MDVP_Fhi_HZ']
    mDVP_Flo_HZ = input_dictionary['MDVP_Flo_HZ']
    mDVP_Jitter_percentage = input_dictionary['MDVP_Jitter_percentage']
    mDVP_Jitter_Abs = input_dictionary['MDVP_Jitter_Abs']
    mDVP_RAP = input_dictionary['MDVP_RAP']
    mDVP_PPQ = input_dictionary['MDVP_PPQ']
    jitter_DDP = input_dictionary['Jitter_DDP']
    mDVP_Shimmer = input_dictionary['MDVP_Shimmer']
    mDVP_Shimmer_dB = input_dictionary['MDVP_Shimmer_dB']
    shimmer_APQ3 = input_dictionary['Shimmer_APQ3']
    shimmer_APQ5 = input_dictionary['Shimmer_APQ5']
    mDVP_APQ = input_dictionary['MDVP_APQ']
    shimmer_DDA = input_dictionary['Shimmer_DDA']
    nHR = input_dictionary['NHR']
    nNR = input_dictionary['HNR']
    rPDE = input_dictionary['RPDE']
    dFA = input_dictionary['DFA']
    spread1 = input_dictionary['spread1']
    spread2 = input_dictionary['spread2']
    d2 = input_dictionary['D2']
    pPE = input_dictionary['PPE']


    input_list = [mDVP_fo_HZ, mDVP_Fhi_HZ, mDVP_Flo_HZ, mDVP_Jitter_percentage, mDVP_Jitter_Abs, mDVP_RAP, mDVP_PPQ, jitter_DDP,
                   mDVP_Shimmer, mDVP_Shimmer_dB, shimmer_APQ3, shimmer_APQ5, mDVP_APQ, shimmer_DDA, nHR, nNR, rPDE, dFA,
                     spread1,spread2, d2, pPE]
    
    prediction = parkinsons_model.predict([input_list])
    
    if prediction[0] == 0:
        return "We are sorry , You have been diagnosed with parkinson."
    
    else:
        return 'Congratulations , You have been not diagnosed with parkinson.'


