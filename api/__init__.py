from flask import Flask, jsonify, Response, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from celery import Celery
from datetime import timedelta
import celeryconfig

def make_celery(app):
    celery = Celery(app.import_name,backend=app.config['CELERY_RESULT_BACKEND'],broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return  self.run( *args, **kwargs)
    celery.Task = ContextTask
    return celery

app = Flask(__name__)


app.config.from_object(Config)
app.config.update(CELERY_BROKER_URL='redis://localhost:6379',CELERY_RESULT_BACKEND='redis://localhost:6379')
celery = make_celery(app)
celery.config_from_object(celeryconfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.config['CELERYBEAT_SCHEDULE'] = {
    # Executes every minute
    'periodic_task-every-minute': {
        'task': 'api.urls.taskscrapper',
        'schedule': timedelta(seconds=30)
    }
}


from api import models, urls, tasks

