from api import app, tasks
from flask_apscheduler import APScheduler


scheduler = APScheduler()

def scheduled_tasks():
    tasks.job()

if __name__ == '__main__':
    scheduler.add_job(id='Scheduled task', func=scheduled_tasks, trigger='interval', seconds=500)
    scheduler.start()
    app.run()