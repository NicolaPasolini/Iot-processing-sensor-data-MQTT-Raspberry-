import paho.mqtt.client as mqtt
import json
from gpiozero import LED
import time

broker = 'broker.hivemq.com'
topic = "supertoy/model/tecnobot/serial/pasolini/incarico"

led1 = LED(7)
led2 = LED(22)
led3 = LED(18)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to {broker} Broker!")
    else:
        print(f"Failed to connect, return code {rc}")
    client.subscribe(topic)


def on_message(client, userdata, msg):
    messaggio = msg.payload.decode()
    print("Messaggio ricevuto: " + messaggio)
    #gestione Json
    payload = json.loads(msg.payload)
    n = payload ["num_azioni"]
    print(n)
    if(n==1):
        led1.on()
        time.sleep(5)
    elif(n==2):
        led2.on()
        time.sleep(5)
    elif(n==3):
        led3.on()
        time.sleep(5)
    else:
        print("numero azioni non valido")



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
# Rimani in ascolto dei messaggi sul topic
client.loop_forever()




