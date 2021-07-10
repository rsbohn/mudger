# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
# SPDX-License-Identifier: MIT

# copy to the CIRCUITPY drive as "code.py"
# also copy midi_player.py there
"""Part 2 Experiment 01 -- bring back the light show"""
import time
import board

from neopixel import NeoPixel
from midi_player import MidiPlayer

player = MidiPlayer()
player.start()
pixel = NeoPixel(board.NEOPIXEL, 1, brightness=0.3)
lightshow = [0xFF0000, 0xCC0000, 0x990000, 0x660000, 0x330000, 0x000000]
while True:
    step = player.play(time.monotonic())
    pixel[0] = lightshow[step % len(lightshow)]
    time.sleep(0.01)
