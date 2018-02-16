#!/usr/bin/python3

import pydrummer.config

from pydrummer.models.song import Song
from pydrummer.models.sound import Sound
from pydrummer.player import Player

if __name__ == '__main__':
    # 1. Create player that we'll use to play sounds.
    player = Player()

    # 2. Create song.
    song = Song()

    # 3. Add clip.
    song.add_clip(pydrummer.config.SM808, steps=8)

    # 4. Add pattern.
    print('\nListen to some sounds to pick which ones you like...')
    player.play(sound=Sound(name="kick", fpath=pydrummer.config.SM808["kick"]))
    player.play(sound=Sound(name="kick2", fpath=pydrummer.config.SM808["kick2"]))
    player.play(sound=Sound(name="kick3", fpath=pydrummer.config.SM808["kick3"]))
    print('\nAdd pattern with the sound you like best...')
    clip = song.clips[0]
    clip.add_pattern('kick3', [1,0])

    # 5. Play clip.
    print('\nPlay the clip to see if you like the way it sounds...')
    player.play(clip=clip, loops=1)

    # 6. Continue to add patterns and play clip until you finish your beat.
    print('\nAdd more patterns and play the clip along the way...')
    clip.add_pattern('hhclosed', [1,1,0,1,1,0,0,1])
    player.play(clip=clip, loops=1)
    # Adding drums back in to make them louder (hacky)
    print('\nMake kick louder...')
    clip.add_pattern('kick3', [1,0])
    player.play(clip=clip, loops=1)
    print('\nLouder...')
    clip.add_pattern('kick3', [1,0])
    player.play(clip=clip, loops=1)
    print('\nListen to a single instrument pattern...')
    player.play(sequence=clip.sequences["hhclosed"], loops=1)

    # 7. Play song.
    print('\nListen to the final output...')
    player.play(song=song, loops=3)
    print('\nListen with a different tempo...')
    player.settings.bpm = 60
    player.play(clip=clip, loops=1)
