from api import app, tasks
from flask_apscheduler import APScheduler

from apscheduler.schedulers.background import BackgroundScheduler


def scheduled_tasks():
    tasks.job()

sched = BackgroundScheduler(daemon=False)
sched.add_job(scheduled_tasks, 'interval', minutes=5)
sched.start()


if __name__ == '__main__':
    app.run()