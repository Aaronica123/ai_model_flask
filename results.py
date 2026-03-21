from ai_model import AI_DATA
from ai_train import ai_md,risk
from flask import request
import numpy as np
import json
def filter1(reg,subj):
    data=json.loads(request.data)
    
    data=request.get_json()    
    register=data.get('register')
    subject=data.get('subject')
    reg_=reg
    subj_id=subj
    state=AI_DATA.query.filter_by(admission_number=reg_ ,subject_id=subj_id).all()
    
    mk=[]
    try:
        if(state):
            
            for k in state:
               
               mk.append(k.marks_obtained)
            x=5
            print(len(mk))
            y=len(mk)
            print
            while(y<x):
                mk.append(None)
                y=y+1
                
            
            if(ai_md):
                print(mk)
                return risk(mk)
            else:
                return f"the ai couldnt initialize"
        else:
            return f"the registration doesnt exist"
            
    except Exception as e:
        return f"error is {str(e)}"        
            
                
def general(cont,subj):
    h=[]
    h=cont
    s=0
    while(s<len(h)):
        print(h[s])
        s+=1;   
    
        
    