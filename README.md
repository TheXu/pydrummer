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
pip install -r requirements.txt

Test
---
```
python3 test.py
```
**output:**
```
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] (congalo)
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] (congamid)
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] (congahi)
- congalo - congamid - congahi - - - congahi - congamid - congalo - -
[0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1] (clave)
- congalo clave mixed clave congahi clave clave - congahi clave mixed clave congalo clave clave
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] (hhclosed)
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] (kick)
kick mixed clave mixed mixed mixed clave mixed kick mixed clave mixed mixed mixed clave mixed
```
Usage
---
1. Create a Song to hold our clips.
```python
from song import Song
song = Song(bpm=120, time_signature=(4,4))
```

2. Create a Clip to hold our sequences.

A Clip creates a Sequence for every specified instrument. Each Sequence has one bar with the specified number of steps and one instrument to be used during playback.

```python
from clip import Clip
import config
clip = Clip(instruments=config.SM808, steps_per_bar=16)
```

You can create new drumkits and add instruments in 'config.py'. In this example we used the SM808 drumkit.
```config
SM808 = {
    'clap': 'samples/808/clap.wav',
    'clave': 'samples/808/clave.wav',
    'congahi': 'samples/808/congahi.wav',
    ...
}
```

3. Add clip to our sound.
```python
song.add_clip(clip)
```

4. Update our sequences with patterns.

Here we're going to create a four-on-the-floor drum pattern. First we need to get the clip that we just added to our song.
```python
four_to_floor = song.clips[0]
```
Now we can update our sequences with different patterns to be used during playback. First let's create our kick drum sound.

A four-on-the-floor pattern has a kick on every beat. Since there are 16 steps and 4 beats a measure, our pattern should look like: `kick = [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]`. That's one kick every 4 steps. To make life easier, you can specify a pattern of any length and it will be looped and copied into our sequence until it fills the entire length of the sequence.

Here we will provide a four-step pattern that will be looped and copied into our 'kick' sequence 4 times. 'kick' is the name of the instrument that we provided when we created our clip. The name of the instrument indicates which sequence you are working on and must exactly match what was specified when creating the clip.
```python
four_to_floor.add_pattern(name='kick', pattern=[1,0,0,0])
```

5. Play your clip.
```python
sound.play(four_to_floor, loops=1)
```
**output:**
```
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] (kick)
kick - - - kick - - - kick - - - kick - - -
```
Here we play our clip for one loop. If loops is unspecified the program will cycle until you ctrl-C. A '-' string is printed out to represent silence.

We can add different instruments to our beat by continuing to update sequences with different patterns.
```
four_to_floor.add_pattern('hhclosed', [0,1])
four_to_floor.add_pattern('clave', [0,0,1,1,1,0,1,1])
song.play(four_to_floor, loops=1)
```
**output:**
```
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] (kick)
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] (hhclosed)
[0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1] (clave)
kick hhclosed clave mixed mixed hhclosed clave mixed kick hhclosed clave mixed mixed hhclosed clave mixed
```
A 'mixed' string is printed out when one or more sounds had to be mixed so they could be played back at the same time.

And that's about it. Just add a little conga drums and you have yourself a pretty sick beat.

```
four_to_floor.add_pattern('congalo', [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
four_to_floor.add_pattern('congamid', [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0])
four_to_floor.add_pattern('congahi', [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0])
song.play(four_to_floor)
```
