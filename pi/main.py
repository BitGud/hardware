from gpiozero import Buzzer, OutputDevice
import websockets, asyncio

BUZZER_PIN = 5
RELAY_PIN= 3

buzzer = Buzzer(BUZZER_PIN)
relay = OutputDevice(RELAY_PIN, active_high=True, initial_value=False)

async def listen():
    url = ''

    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            if (msg == 'on'):
                buzzer.on()
                relay.on()
                buzzer.off()
                relay.off()

asyncio.get_event_loop().run_forever(listen())
