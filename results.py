from ai_model import AI_DATA
from ai_train import ai_md,risk
def filter1(reg):
    reg_=reg
    state=AI_DATA.query.filter_by(reg=reg_).first()
    try:
        if(state):
            hold=[
                state.cat_1,
                state.cat_2,
                state.cat_3,
                state.exam_1,
                state.exam_2
            ]
            if(ai_md):
                print(hold)
                return risk(hold)
            else:
                return f"the ai couldnt initialize"
        else:
            return f"the registration doesnt exist"
            
    except Exception as e:
        return f"error is {str(e)}"        
            
                
        
        
    