from flask import Flask
from flask_session import Session


app = Flask(__name__)
TEMPLATES_AUTO_RELOAD=True
app.config['SECRET_KEY'] = 'DESOFTsecretKEY123'
app.config['SESSION_TYPE']='filesystem'

app.config['DEBUG']=True
methods = ['POST', 'GET']
session=Session(app)


from app import routes