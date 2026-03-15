import joblib
import os
model=None
def ai_md():
    global model
    dir=os.path.dirname(os.path.abspath(__file__))
    md_path=os.path.join(dir,'elimubase_model.pkl')

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
    
    prd=model.predict(input_1)
    
    return f"risk is at {prd[0]}"
       

        
    