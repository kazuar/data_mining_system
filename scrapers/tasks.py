
from datetime import datetime

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from scrapers.scrapers_apis import example_scraper


logger = get_task_logger(__name__)

# A periodic task that will run every minute
@periodic_task(run_every = (crontab(hour = "*", minute = "*", day_of_week = "*")))
def task_example():
    logger.info("Start task")
    now = datetime.now()
    result = example_scraper.scraper_example(now.day, now.minute)
    logger.info("Task finished: result = {}".format(result))
