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
def jsn():
    data = request.get_json()
    if not data:
        
        return jsonify({"error": "No JSON data provided"}), 400
    
    reg = data.get('register')
    subj = data.get('subject')
    
    result = filter1(reg, subj)
    if isinstance(result, str):
        return jsonify({"error": result}), 400
    return jsonify({
        "risk": getattr(result, 'value', "N/A"),
        "trend": getattr(result, 'x1', "N/A")
    })

from ai_model import AI,AI_DATA
from ai_train import ai_md
ai_md()



# with app.app_context():
#     print(f"{filter1('1001',1)}")
    
# s=['1001','1002','1003','1004']


# with app.app_context():
#     print(f"{general(s,1)}")
    
    
if __name__ == "__main__":
    with app.app_context():
        
        # Test single record
        print(f"Single Test: {filter1('1001', 1)}")
        
        # Test batch
        s = ['1001', '1002', '1003', '1004']
        print(f"Batch Test: {general(s, 1)}")
    
    # Run the server
    app.run(debug=True)
    









