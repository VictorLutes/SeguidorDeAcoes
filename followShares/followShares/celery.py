import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'followShares.settings')

app = Celery('follows')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    

app.conf.beat_schedule = {
    #Scheduler Name
    'update_shares_minute': {
        # Task Name (Name Specified in Decorator)
        'task': 'update_shares',  
        # Schedule      
        'schedule': 60.0,
        # Function Arguments 
        'args': () 
    },
} 