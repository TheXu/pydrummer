from sound import Sound

class Sequence(object):
    """A Sequence is a series of notes defined by a pattern and a Sound.

    A pattern is an array of zeros and ones and has a length equal to the
    number of steps in our playback window.
    """
    def __init__(self, name, fpath, steps):
        self.name = name
        self.sound = Sound(name, fpath)
        self.steps = steps
        self.pattern = [0] * steps

    def set_pattern(self, pattern):
        """Set the pattern.

        If the length of given pattern is smaller than the length of the pattern
        in our Sequence, loop throught it again an continue setting elements
        until you reach the end.
        """
        for i in range(self.steps):
            self.pattern[i] = pattern[i%len(pattern)]
            if self.pattern[i] == 1: self.active = True

    def play_step(self, i):
        self.sound.play()