#!/usr/bin/python3

import config

from clip import Clip
from song import Song

if __name__ == '__main__':
    song = Song(bpm=120, time_signature=(4,4))

    song.clips.append(Clip(config.SM808, steps_per_bar=8))
    four_to_floor = song.clips[0]

    four_to_floor.add_pattern('kick3', [1,0])

    song.play(four_to_floor, loops=2)

    four_to_floor.add_pattern('hhclosed', [0,1,0,1,0,0,0,1])

    song.play(four_to_floor, loops=2)

    four_to_floor.add_pattern('congalo', [0,1,0,0])
    four_to_floor.add_pattern('congamid', [0,0,1,0])
    four_to_floor.add_pattern('congahi', [0,0,0,1])

    song.play(four_to_floor, loops=2)

    four_to_floor.add_pattern('clave', [0,0,1,1,0,0,1,1])

    song.play(four_to_floor, loops=1)

    four_to_floor.add_pattern('hhclosed', [0,1])
    four_to_floor.add_pattern('kick3', [1,0])

    song.play(four_to_floor, loops=2)

    four_to_floor.add_pattern('kickrr3', [0,0,0,1])

    song.play(four_to_floor, loops=1)