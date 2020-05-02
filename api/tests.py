from api import db,celery
from api.tasks import Scrapper



@celery.task
def taskscrapper():
    obj = Scrapper()
    print("Dropping the tables")
    db.drop_all()
    print("Creating the tables")
    db.create_all()
    obj.add_countries()


