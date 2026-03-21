import joblib
import os
model=None
def ai_md():
    global model
    dir=os.path.dirname(os.path.abspath(__file__))
    md_path=os.path.join(dir,'elimubase_ai.pkl')

    try:
            model=joblib.load(md_path)
            print (f"load was a success")
            return True
        

    except Exception as e:
       print(f"failed to load {str(e)}")
       return False
   
import pandas as pd
def risk(marks):
    global model
    feature_names = ['cat_1', 'cat_2', 'cat_3', 'exam_1', 'exam_2']
    input_1=pd.DataFrame([marks],columns=feature_names)
    input_1['trend']=input_1.apply(scope,axis=1)*5
    prd=model.predict(input_1)
    x1=int(input_1['trend'].values[0])
    if(x1>0):
        return f"risk is at {prd[0]} and student is in a trend of {x1}"
    elif(x1<0):
        return f"risk is at {prd[0]} but student is in a trend of {x1}"
    else:
        return f"risk is at {prd[0]} but student is in a stable trend of {x1}"
        
    
from sklearn.linear_model import LinearRegression
import numpy as np
def scope(row):
    vl=['cat_1','cat_2','cat_3','exam_1','exam_2']
    st=row[vl].dropna().values
    try:
        if len(st)<2:
            return 0.0
        x=np.arange(len(st)).reshape(-1,1)
        linear=LinearRegression()
        linear.fit(x,st)
        return linear.coef_[0]
    except Exception as e:
        return f"error occured {str(e)}"


        
    