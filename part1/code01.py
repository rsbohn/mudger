# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
# SPDX-License-Identifier: MIT
"""part1: blinking lights and making noise"""
import time
import board
from neopixel import NeoPixel
from pwmio import PWMOut

pixel = NeoPixel(board.NEOPIXEL, 1, brightness=0.3)
lightshow = [0xFF0000, 0xFFFF00, 0x00FF00, 0x000000]

speaker = PWMOut(board.D7, duty_cycle=0x4000, frequency=440, variable_frequency=True)
freqs = [220, 440, 880]

BPM = 120
TICK = 60 / BPM * 1 / 4
LAST_TICK = 0
STEP = 0

while True:
    now = time.monotonic()
    if TICK <= now - LAST_TICK:
        LAST_TICK = now
        pixel[0] = lightshow[STEP % len(lightshow)]
        STEP += 1
        speaker.frequency = freqs[STEP % len(freqs)]

    time.sleep(0.01)
