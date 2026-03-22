from ai_model import AI_DATA
from ai_train import ai_md,risk

import numpy as np

def filter1(reg,subj):
    
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
    try:
        while(s<len(h)):
            temp=str(cont[s])
            temp=str(temp)
            print(temp)
            st=[]
            hd=AI_DATA.query.filter_by(admission_number=temp,subject_id=subj).all()
            s+=1
            if(ai_md):
                for k in hd:
                    
                    st.append(k.marks_obtained)
                print(risk(st))
                
            else:
                return f"couldnt load"
            
    except Exception as e:
        return f"the error is {str(e)}"
    
     
        

    
        
    