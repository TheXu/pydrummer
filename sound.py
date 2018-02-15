import sounddevice
import soundfile
import wave
from os import system

class Sound(object):
	def __init__(self, name, fpath):
		self.name = name
		self.file_path = fpath
		self.data, self.framerate = soundfile.read(fpath)

	def play(self):
		print('{}'.format(self.name), end=' ', flush=True)
		sounddevice.play(self.data, self.framerate)

	def open_file(self):
		return wave.open(self.file_path)