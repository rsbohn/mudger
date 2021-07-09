# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
# SPDX-License-Identifier: MIT

# copy to the CIRCUITPY drive as "code.py"
"""Part 2 Experiment 02 -- other modes"""
import time
import board

from neopixel import NeoPixel
from midi_player import MidiPlayer

# thanks https://github.com/adafruit/Adafruit_Learning_System_Guides
# /blob/f44f5f961ceb9dccb785c5843c22b12bcc1f7b5b/MIDI_Modal_Keyboard/code.py
major = (0, 2, 4, 5, 7, 9, 11, 12)
minor = (0, 2, 3, 5, 7, 8, 10, 12)
dorian = (0, 2, 3, 5, 7, 9, 10, 12)
phrygian = (0, 1, 3, 5, 7, 8, 10, 12)
lydian = (0, 2, 4, 6, 7, 9, 11, 12)
mixolydian = (0, 2, 4, 5, 7, 9, 10, 12)
locrian = (0, 1, 3, 5, 6, 8, 10, 12)

player = MidiPlayer()
player.riff = [60 + m for m in dorian]
pixel = NeoPixel(board.NEOPIXEL, 1, brightness=0.3)
lightshow = [0xFF0000, 0xCC0000, 0x990000, 0x660000, 0x330000, 0x000000]
while True:
    step = player.play(time.monotonic())
    pixel[0] = lightshow[step % len(lightshow)]
    time.sleep(0.01)
