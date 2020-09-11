import os
import urllib.parse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from gensim.models import KeyedVectors
from app import utils

app = Flask(__name__)

db_string = os.environ['dbstring']
params = urllib.parse.quote_plus(db_string)

app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
# 	'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)
model = KeyedVectors.load('./app/model/ft_we.model')
stopwords = utils.get_stopwords('./app/model/stopwords.txt')
const_store = {
	'topics': ["Artificial Intelligence", "Computer Science and Game Theory", "Multiagent Systems", "Computer Vision and Pattern Recognition", "Data Structures and Algorithms", "Distributed, Parallel, and Cluster Computing", "Human-Computer Interaction", "Information Retrieval", "Machine Learning", "Robotics", "Social and Information Networks", "Sound" ]
}
temp_store = []

from app.views import mod
app.register_blueprint(mod)

from app.cli import *