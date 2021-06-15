from paho.mqtt import client as mqtt_client
topic = 'home/status'
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    pass


# for obj in Home.objects.all():
#     try:
#         client_obj = mqtt_client.Client()
#         client_obj.on_connect = on_connect
#         client_obj.subscribe(obj.topic)
#         client_obj.on_message = on_message
#         client_obj.connect(obj.host_mqtt, obj.port_mqtt)
#         list_client.append(client_obj)
#     except:
#         pass

client = mqtt_client.Client()
client.on_connect = on_connect
client.subscribe(topic)
client.on_message = on_message
client.connect('127.0.0.1',1883)

