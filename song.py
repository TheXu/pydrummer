import itertools
import time

SECONDS_PER_MIN = 60.0
MIN_STEP_TIME = 0.01 # TODO: Figure out a way to not have to cut off notes at the 
                     # beginning of the next step. This is will make it so we don't 
                     # hit this minimum so often, which will give us a less choppy
                     # sound.
class Song():
    """A Song is a container for Clips that knows how fast to play them.

    A Song knows how to calculate how much time each step should take during 
    playback in order to play at a speed of the specified beats per minute.
    """
    def __init__(self, bpm=60, time_signature=(4,4)):
        self.beats_per_measure = time_signature[0]
        self.beat_unit = time_signature[1]
        self.bpm = bpm
        self.clips = []

    # TODO: Improve accuracy of calculatation for when to play the next beat
    # Maybe try realigning every bar - use absolute time? 
    def play(self, clip, loops=-1):
        """Play a note for every step in the clip

        Repeat for the specified number of loops. If loop is -1 then play continuously.
        """
        time_per_bar = (SECONDS_PER_MIN / self.bpm) * self.beats_per_measure
        time_per_step = time_per_bar / clip.steps
        bars = 0
        for i in itertools.cycle(range(clip.steps)):
            now = time.time()
            clip.mix.sounds[i].play()
            elapsed = time.time() - now
            time.sleep(max(MIN_STEP_TIME, time_per_step - elapsed)) # sleep for the remaining amount of time
            if i == clip.steps-1:
                bars += 1
                print('')

            if bars == loops:
                return