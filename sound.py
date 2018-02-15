import numpy as np
import sounddevice
import soundfile

class Sound(object):
    """A Sound is pre-recorded sound data that can be heard when it reaches our ears.

    A Sound can also be mixed with other Sounds to create a new Sound. This is how we
    create the effect of hearing two notes playing back at the same time. 

    We read in the sound file to get its data and sample rate to be used during playback.
    When another sound is mixed in we continue to use the original sample_rate. 
    """
    def __init__(self, name='-', fpath=''):
        self.name = name
        self.file_path = fpath
        try:
            self.data, self.sample_rate = soundfile.read(fpath, frames=100000, fill_value=0)
        except:
            self.data = []
            self.sample_rate = 44100 # TODO: Figure out good default for instrument wave files
        self.data_array = np.array(self.data)

    def play(self):
        print('{}'.format(self.name), end=' ', flush=True)
        sounddevice.play(self.data_array, self.sample_rate)

    def mix(self, sound):
        # TODO: Figure out how to mix soundfiles of different shapes
        # TODO: Fix sounddevice.PortAudioError: Error opening OutputStream:
        # Invalid number of channels [PaErrorCode -9998] - Hard to repro, try
        # playing clips with many different sequences with overlapping sounds
        # and try different wave files
        # TODO: Actually research how to mix sound data together to make this sound better
        self.data_array = np.column_stack([self.data, sound.data])
