from mix import Mix
from sequence import Sequence

class Clip(object):
    """A Clip maintains Sequences and the output Mix sequence.

    A Clip manages the Sequences used during the construction of a rhythm and 
    maintains the Mix, the output rhythm created by merging all the Sequences 
    together. 

    A Sequence is created for every instrument in the instruments dictionary. 
    Both the Mix and the Sequences have the same number of steps calculated by 
    bars * steps_per_bar.
    """
    def __init__(self, instruments, bars=1, steps_per_bar=4):
        self.steps = bars * steps_per_bar
        self.sequences = {}
        for name, fpath in instruments.items():
            self.sequences[name] = Sequence(name, fpath, self.steps)
        self.mix = Mix(self.steps)

    def add_pattern(self, name, pattern):
        """Add a pattern to the Sequence with the given name.

        Each time a Sequence is updated, we merge it with our Mix sequence so 
        that it's ready to be played back at any time.
        """
        self.sequences[name].set_pattern(pattern)
        print('{pattern} ({name})'.format(name=name, pattern=self.sequences[name].pattern))
        self.mix.merge(self.sequences[name])