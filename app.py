from api import app, tasks
from flask_apscheduler import APScheduler


scheduler = APScheduler()


def scheduled_tasks():
    data_scrapper = tasks.Scrapper()
    data_scrapper.job()


if __name__ == '__main__':
    scheduler.add_job(id='Scheduled task', func=scheduled_tasks, trigger='interval', seconds=1200)
    scheduler.start()
    app.run(debug=True)