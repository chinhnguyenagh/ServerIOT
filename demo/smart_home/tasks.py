from __future__ import absolute_import, unicode_literals
from celery import shared_task
from paho.mqtt import client as mqtt_client
from decouple import config
@shared_task
def pub(host:str, port:int, topic:str, msg:str):
    try:
        client = mqtt_client.Client()    
        client.username_pw_set(config('USERNAME_MQTT'), config('PASSWORD_MQTT'))
        client.connect(host, port)
        client.publish(topic, msg)
    except:
        pass
