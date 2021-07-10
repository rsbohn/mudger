# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
# SPDX-License-Identifier: MIT
"""a book of songs"""


class Song:
    """a song with a title and a list of notes"""

    def __init__(self, title, notes):
        self.title = title
        self.notes = _flatten(notes)

    def transpose(self, semitones):
        """transpose up or down by semitones

        :param int semitones: number of semitones to raise or lower the notes
        :return list: the notes transposed"""
        return [note + semitones for note in self.notes]


def _flatten(that):
    return [item for sublist in that for item in sublist]


twinkle_twinkle = Song(
    title="Twinkle Twinkle Little Star",
    notes=[
        [60, 60, 67, 67, 69, 69, 67, 0],
        [65, 65, 64, 64, 62, 62, 60, 0],
        [67, 67, 65, 65, 64, 64, 62, 0],
        [67, 67, 65, 65, 64, 64, 62, 0],
        [60, 60, 67, 67, 69, 69, 67, 0],
        [65, 65, 64, 64, 62, 62, 60, 0],
    ],
)
