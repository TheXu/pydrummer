from pattern import Pattern
from song import Song

if __name__ == '__main__':
	song = Song(120)
	pattern = Pattern('_._._***|_^_^_***','|')
	song.play(pattern.get_sound_pattern())