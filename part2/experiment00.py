# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
# SPDX-License-Identifier: MIT

# copy to the CIRCUITPY drive as "code.py"
# also copy midi_player.py there
"""Part 2 Experiment 00 -- Send some MIDI notes"""
import time

from midi_player import MidiPlayer


player = MidiPlayer()
while True:
    player.play(time.monotonic())
    time.sleep(0.01)
