from celery.schedules import crontab
from celery.task import PeriodicTask


__all__ = ['ExampleTask']


class ExampleTask(PeriodicTask):
    run_every = crontab(minute=0, hour=0)

    def run(self, *args, **kwargs):
        print('test')
