from datetime import datetime
import os
from dotenv import load_dotenv
from factory import TTSFactory

load_dotenv(override=True)
tts = TTSFactory().get_tts('gtts')

REQ_TOPIC = os.getenv("REQ_TOPIC")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[{datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}] {client._client_id.decode()} connected to broker sucessfully")
        client.subscribe(REQ_TOPIC)
        client.subscribe('/tts/stop')
        
    else:
        print(f"Connection failed with code {rc}")
        
def on_subscribe(client, userdata, mid, granted_qos):
    print(f"[{datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}] {client._client_id.decode()} subscribed to topic with mid {mid} and QOS {granted_qos} on {REQ_TOPIC}")

def on_message(client, userdata, message):
    print(f"[{datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}] Received a message on topic {message.topic}")
    
    if message.topic == '/tts/stop':
        tts.stop()
    elif message.topic == '/tts':
        tts.speak(message.payload.decode())