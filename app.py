from flask import Flask,jsonify
from extensions import db, migrate
from dotenv import load_dotenv
import os
from flask import request
from results import general
from results import filter1



load_dotenv()
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('neon')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,  # Checks if connection is alive before every query
    "pool_recycle": 280,    # Closes connection before Neon's 300s timeout
    "connect_args": {
        "sslmode": "require",
        "connect_timeout": 10
    }
}
db.init_app(app)
migrate.init_app(app,db)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data:
        
        return jsonify({"error": "No JSON data provided"}), 400
    
    if not reg or subj is None:
        return jsonify({"error": "admissionNumber and subjectId are required"}), 400

    reg = data.get('admissionNumber') or data.get('register')
    subj = data.get('subjectId') or data.get('subject')
    
    result = filter1(reg, subj)
    
    if isinstance(result, str):
        return jsonify({"error": result}), 400
    else:
        value,x=result
        return jsonify({
            "risk": value,
            "trend": x
        })
    

from ai_model import AI,AI_DATA
from ai_train import ai_md
ai_md()

    
if __name__ == "__main__":
    with app.app_context():
        result=filter1('1007', 1)
        
        if isinstance(result,str):
            print(f"{str(result)}")
        else:
            value,x=result
        # Test single record
            print(f"Single Test: {value} and the trend is {x}")
        
        # Test batch
        s = ['1001', '1002', '1003', '1004']
        general(s, 1)
        
    
    # Run the server
    app.run(debug=True)
    









