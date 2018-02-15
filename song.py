import itertools
import threading
import time

class Song(threading.Thread):
	def __init__(self, bpm = 60, time_sig = (4,4)):
		super(Song, self).__init__()
		self.beats_per_measure = time_sig[0]
		self.note_that_gets_one_beat = time_sig[1]
		self.bpm = bpm
		self.start()

	def play(self, pattern):
		sleep = 60.0 / self.bpm / self.beats_per_measure
		count = 1
		for sound in itertools.cycle(pattern):
			self.worker(sound)
			time.sleep(sleep)
			count+=1

	def worker(self, sound):
		if sound:
			sound.play()