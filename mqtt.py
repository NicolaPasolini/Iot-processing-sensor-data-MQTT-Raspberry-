import paho.mqtt.client as mqtt
import json
from gpiozero import LED
import time

broker = 'broker.hivemq.com'

topic = "scatolacompleta"
topic2 = "spedizionecompleta"

#pin_led = 17
#led = LED(pin_led)
#uso led.on() o off() dove mi serve con eventualmente sleep(5) e led.value() per sapere se acceso o spento

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to {broker} Broker!")
    else:
        print(f"Failed to connect, return code {rc}")
    client.subscribe(topic)
    client.subscribe(topic2)

def on_message(client, userdata, msg):
    messaggio = msg.payload.decode()
    print("Messaggio ricevuto: " + messaggio)
    #gestione json
    payload = json.loads(msg.payload)
    status1 = payload ["stato_transito"]
    if(status1==1):
        print("in transito")
    elif(status1==0):
        print("consegnato")


def pubblica_messaggio(client, messaggio):
    client.publish(topic, messaggio)

def createMessage():
    json_payload={"id_cella": 0, "id_shuttle": 0, "elementi": {"id": 0,"essenza": "a","forma": "b","formato": 0	},"peso": 2, "cod_ordine":0,"stato_transito": 1,"stato_consegnato": 0,"tipo_cella": "c" }
    return json.dumps(json_payload)




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
pubblica_messaggio(client, createMessage())
# Rimani in ascolto dei messaggi sul topic
client.loop_forever()


def gestisciMsg(msg):
    payload = json.loads(msg.payload)
    status1 = payload ["stato_transito"]
    if(status1==1):
        print("in transito")
