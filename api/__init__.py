from flask import Flask, jsonify, Response, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from api import models, urls, tasks

