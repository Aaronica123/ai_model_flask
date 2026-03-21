from flask import Flask
from extensions import db, migrate
from dotenv import load_dotenv
import os

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


from ai_model import AI,AI_DATA
from ai_train import ai_md
ai_md()

from results import filter1

with app.app_context():
    print(f"{filter1('1001',1)}")
    
s=[1,2,3,4,5]
from results import general

with app.app_context():
    general(s,1)
    









