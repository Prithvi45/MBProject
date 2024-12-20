#from edyoda.celery import app
#from celery.task import task
#from celery import shared_task
from time import sleep 




#@shared_task
def send_notification():
    sleep(2)
    print("sending notification")
    return "Notification Sent"
