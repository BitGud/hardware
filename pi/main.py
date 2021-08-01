from gpiozero import Buzzer, OutputDevice
import websockets, asyncio
from time import sleep
import socketio

BUZZER_PIN = 5
RELAY_PIN= 3

UID="6105e7c6396ab2ee56cf3c67"
SOCKETIO="wss://bitgud-backend.herokuapp.com"

buzzer = Buzzer(BUZZER_PIN)
relay = OutputDevice(RELAY_PIN, active_high=True, initial_value=False)

sio = socketio.Client()
sio.connect(SOCKETIO,auth={token: UID})

@sio.on('shock')
def shock():
    # handle the message
    relay.on()
    sleep(1)
    relay.off()
        
