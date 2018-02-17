# ...d[-_-]b...
a minimal drum machine you can use to design drum patterns that can be played back with different instruments at precise time steps.

Dependencies
---
* Numpy
* Sounddevice
* SoundFile

Installation
---
pydrummer supports Python 3.5 and later. It's available on the Python Package Index and can be installed by running:
```
pip install pydrummer
```

Test
---
```
python setup.py pytest
```

Demo
---
```
wget https://raw.githubusercontent.com/allieoop/pydrummer/master/demo.py
python demo.py
```

Usage
---
#### 1. Create a Player that we'll use to play our sounds.
```python
from pydrummer.player import Player
player = Player()
```

#### 2. Create a Song to hold our clips.
```python
from pydrummer.models.song import Song
song = Song()
```

#### 3. Add a Clip.
```python
import pydrummer.config
song.add_clip(pydrummer.config.SAMPLES['tr808'], steps=8)
```

**Note:** You can create new drumkits and add them to 'config.py'. After adding a new drumkit, the wave files become accessible via the 'pydrummer.config.SAMPLES' dictionary. In this example we use the pre-installed 'tr808' drumkit. Below you can see that we use a relative path for its location since it lives in the project directory.

*config.py:*
```python
"""Add your drumkits here.

DRUMKITS maps the name of a drumkit to its samples directory.
"""
DRUMKITS = {
    'tr808': 'samples/808',
}
```

#### 4. Add some drum patterns.

First get the clip that we just added to our song.
```python
clip = song.clips[0]
```
Now we can update our clip with different instrument patterns to be used during playback. 

For this example we're going to create a four-on-the-floor rhythm. Four-on-the-floor has a kick drum on every beat. Since the specified number of steps is 8 and the default time signature is 4/4, which is 4 beats a measure, our pattern should look like: `[1,0,1,0,1,0,1,0]`

That's one kick every 2 steps. To make life easier, you can add a pattern of any length and it will be looped until it reaches the specified number of steps.

```python
clip.add_pattern(name='kick', pattern=[1,0])
```
**Note:** 'kick' is the name of one of the instruments we provided when adding our clip with the 'tr808' drumkit. The name of the instrument indicates which instrument you want to use for your pattern and **must** exactly match what was specified when creating the clip. To see a list of names and their associated sound files: `print(pydrummer.config.SAMPLES['tr808'])` You can also create a Sound object and pass it to 'Player.play' to hear what each wave file sounds like (see demo.py for an example).

Let's just add one more pattern before playing our clip to make it more interesting.
```python
clip.add_pattern(name='hhclosed', pattern=[1,1,0,1,1,0,0,1])
```

#### 5. Play your clip.
```python
player.play(clip=clip, loops=1)
```
*output:*
```
[1, 0, 1, 0, 1, 0, 1, 0] (kick3)
[1, 1, 0, 1, 1, 0, 0, 1] (hhclosed)
mix hhclosed kick3 hhclosed mix - kick3 hhclosed
```
A '-' string is printed out to represent silence and a 'mix' string is printed out when two or more sounds had to be mixed so they could be played back at the same time. If loops is unspecified the program will cycle until you ctrl-C. 

You can also adjust playback tempo in the player settings.
```python
player.settings.bpm = 60
player.play(clip=clip, loops=1)
```

**Note:** You can also play the song that holds the clip. This will be more interesting when we can play multiple clips of different instruments at the same time.
```python
player.play(song=song)
```
