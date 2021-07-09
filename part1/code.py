# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
# SPDX-License-Identifier: MIT
"""part1: blinking lights and making noise"""
import time
import board
from neopixel import NeoPixel

pixel = NeoPixel(board.NEOPIXEL, 1, brightness=0.3)
lightshow = [0xFF0000, 0xFFFF00, 0x00FF00, 0x000000]
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

    time.sleep(0.01)
