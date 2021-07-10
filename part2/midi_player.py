# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
# SPDX-License-Identifier: MIT

# copy to the CIRCUITPY drive as "midi_player.py"
"""MidiPlayer -- play MIDI notes"""
import usb_midi

# use `circup install adafruit_midi`
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff


class MidiPlayer:
    """send riff notes in a timely manner"""

    def __init__(self):
        self.midi = adafruit_midi.MIDI(
            midi_in=usb_midi.ports[0],
            midi_out=usb_midi.ports[1],
            in_channel=1,
            out_channel=1,
        )
        self.bpm = 20
        self.tick_time = 60 / self.bpm * 1 / 4
        self.velocity = 120
        self.last_tick = 0
        self.step = 0
        self.playing = False
        self.current_note = None
        # do re mi...
        self.riff = [60, 62, 64, 65, 67, 69, 71, 72]

    def start(self):
        """Start from step zero."""
        self.playing = True
        self.step = 0
        self.last_tick = 0
        return self

    def stop(self):
        """Stop playing."""
        self.playing = False
        return self

    def resume(self):
        """Continue at the next step."""
        self.playing = True
        self.last_tick = 0
        return self

    def play(self, now):
        """Play the next note after self.tick_time has elapsed."""
        if self.playing and self.tick_time <= now - self.last_tick:
            self.last_tick = now
            self.current_note = self.riff[self.step % len(self.riff)]
            self.step += 1
            if self.current_note > 19:
                self.midi.send(NoteOn(self.current_note, self.velocity))
        if not self.playing and self.current_note is not None:
            self.midi.send(NoteOff(self.current_note, 0))
            self.current_note = None
        return self.step
