import time
import board
from neopixel import NeoPixel

pixel = NeoPixel(board.NEOPIXEL, 1, brightness=0.3)
lightshow = [0xFF0000, 0xFFFF00, 0x00FF00, 0x000000]


bpm = 120
tick = 60/bpm * 1/4
last_tick = 0
step = 0

while True:
    now = time.monotonic()
    if tick <= now - last_tick:
        last_tick = now
        pixel[0] = lightshow[step % len(lightshow)]
        step += 1

    time.sleep(0.01)
