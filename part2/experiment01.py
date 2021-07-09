# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
# SPDX-License-Identifier: MIT

# copy to the CIRCUITPY drive as "code.py"
"""Part 2 Experiment 01 -- bring back the light show"""
import time
import board
import usb_midi

# use `circup install adafruit_midi`
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from neopixel import NeoPixel


class MidiPlayer:
    """send riff notes in a timely manner"""

    def __init__(self):
        self.midi = adafruit_midi.MIDI(
            midi_in=usb_midi.ports[0],
            midi_out=usb_midi.ports[1],
            in_channel=1,
            out_channel=1,
        )
        self.bpm = 10
        self.tick_time = 60 / self.bpm * 1 / 4
        self.velocity = 120
        self.last_tick = 0
        self.step = 0
        # do re mi...
        self.riff = [60, 62, 64, 65, 67, 69, 71, 72]

    def play(self, now):
        """Play the next note after self.tick_time has elapsed."""
        if self.tick_time <= now - self.last_tick:
            self.last_tick = now
            note = self.riff[self.step % len(self.riff)]
            self.midi.send(NoteOn(note, self.velocity))
            self.step += 1
        return self.step


player = MidiPlayer()
pixel = NeoPixel(board.NEOPIXEL, 1, brightness=0.3)
lightshow = [0xFF0000, 0xCC0000, 0x990000, 0x660000, 0x330000, 0x000000]
while True:
    step = player.play(time.monotonic())
    pixel[0] = lightshow[step % len(lightshow)]
    time.sleep(0.01)
