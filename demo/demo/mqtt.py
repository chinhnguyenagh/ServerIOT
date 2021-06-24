from paho.mqtt import client as mqtt_client
import requests
import psycopg2
import json
try:
    connection = psycopg2.connect(
        user = 'postgres',
        password = 'root',
        host = '127.0.0.1',
        port = '5432',
        database = 'smarthome'
    )
    cursor  = connection.cursor()
except(Exception, psycopg2.Error) as error:
    print("connect errot ", error)

topic = 'home/status'
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    home = eval(msg.payload.decode())
    sql_select_query = """update smart_home_home set temperature = %s, humid =  %s, distance_door = %s, distance_private_room = %s where id = %s """

    cursor.execute(sql_select_query, (home['temperature'],home['humid'],home['distance_door'],home['distance_private_room'],home['id']))
    connection.commit()






client = mqtt_client.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1',1883)

