from api import app, tasks
from flask_apscheduler import APScheduler


scheduler = APScheduler()


def scheduled_tasks():
    tasks.scrapper.add_countries()


if __name__ == '__main__':
    scheduler.add_job(id='Scheduled task', func=scheduled_tasks, trigger='interval', seconds=300)
    scheduler.start()

    app.run()