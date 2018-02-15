# ...d[-_-]b...
sm808 is a minimal drum machine you can use to design drum patterns that can be played back with different instruments at precise time steps.

Dependencies
---
* cffi==1.11.4
* numpy==1.14.0
* pycparser==2.18
* sounddevice==0.3.10
* SoundFile==0.9.0.post1

Install
---
```
pip install -r requirements.txt
```

Test
---
```
python3 test.py
```

Usage
---
#### 1. Create a Player that we'll use to play our sounds.
```python
from player import Player
player = Player()
```

#### 2. Create a Song to hold our clips.
```python
from models.song import Song
song = Song()
```

#### 3. Add a Clip.
```python
import config
song.add_clip(config.SM808)
```

**Note:** You can create new drumkits and add instruments in 'config.py'. In this example we used the SM808 drumkit.

*config.py:*
```config
SM808 = {
    'clap': 'samples/808/clap.wav',
    'clave': 'samples/808/clave.wav',
    'congahi': 'samples/808/congahi.wav',
    ...
}
```

#### 4. Add some drum patterns.

First get the clip that we just added to our song.
```python
clip = song.clips[0]
```
Now we can update our clip with different instrument patterns to be used during playback. 

For this example we're going to create a four-on-the-floor rhythm. Four-on-the-floor has a kick drum on every beat. Since the default number of steps is 16 and the default time signature is 4/4, which is 4 beats a measure, our pattern should look like: `[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]`

That's one kick every 4 steps. To make life easier, you can add a pattern of any length and it will be looped until it reaches the specified number of steps.

```python
clip.add_pattern(name='kick', pattern=[1,0,0,0])
```
**Note:** 'kick' is the name of the instrument that we provided when we created our clip. The name of the instrument indicates which instrument you want to use for your pattern and **must** exactly match what was specified when creating the clip.

Let's just add one more pattern before playing our clip to make it more interesting.
```python
clip.add_pattern(name='tomlo', pattern=[0,1,0,1,1,0,0,1])
```

#### 5. Play your clip.
```python
player.play(clip=clip, loops=1)
```
*output:*
```
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] (kick)
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1] (tomlo)
kick tomlo - tomlo mix - - tomlo kick tomlo - tomlo mix - - tomlo
```
A '-' string is printed out to represent silence and a 'mix' string is printed out when one or more sounds had to be mixed so they could be played back at the same time. If loops is unspecified the program will cycle until you ctrl-C. 

You can also adjust playback tempo in the player settings.
```python
player.settings.bpm = 60
player.play(clip=clip, loops=1)
```

**Note:** You can also play the song that holds the clip. This will be more interesting when we can play multiple clips of different instruments at the same time.
```python
player.play(song=song)
```
