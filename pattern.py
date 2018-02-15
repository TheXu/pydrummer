from sound import Sound

import config

class Pattern(object):
	def __init__(self, symbol_pattern, measure_delimiter=None):
		self.sound_map = {
			' ' : ' ',
			'_' : Sound('kick', config.PATHS['samples']+config.SAMPLES['kick']),
			'^' : Sound('rim', config.PATHS['samples']+config.SAMPLES['rim']),
			'.' : Sound('tamb', config.PATHS['samples']+config.SAMPLES['tamb']),
			'*' : Sound('clap', config.PATHS['samples']+config.SAMPLES['clap']),
		}
		self.symbol_pattern = symbol_pattern
		self.measure_delimiter = measure_delimiter

	def get_sound_pattern(self):
		sound_pattern = []
		for symbol in self.symbol_pattern:
			if symbol != self.measure_delimiter:			
				sound = self.sound_map[symbol]
				sound_pattern.append(sound)
		return sound_pattern