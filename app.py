from flask import Flask
from extensions import db, migrate
from dotenv import load_dotenv
import os

load_dotenv()
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('supabase')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)
migrate.init_app(app,db)


from ai_model import AI,AI_DATA
from ai_train import ai_md
ai_md()

from results import filter1

with app.app_context():
    print(f"{filter1(1)}")









