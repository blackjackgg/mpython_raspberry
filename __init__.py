import sys
from math import pow

try:
    import time
except ImportError:
    pass

try:
    import re
except ImportError:
    import ure as re

try:
   from midi import MidiFile
except ImportError:
    MidiFile = None

try:
   from rtttl import RTTTL
except ImportError:
    RTTTL = None

SAMPLING_RATE = 1000

names = ("c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b")

A4 = 440
C0 = A4 * pow(2, -4.75)

def note_freq(note):
    n, o = note[:-1], int(note[-1])
    index = names.index(n)
    return int(round(pow(2, (float(o * 12 + index) / 12.0)) * C0, 2))

def isplit(iterable, sep=None):
    r = ''
    for c in iterable:
        r += c
        if sep is None:
            if not c.strip():
                r = r[:-1]
                if r:
                    yield r
                    r = ''                    
        elif r.endswith(sep):
            r=r[:-len(sep)]
            yield r
            r = ''
    if r:
        yield r

class BuzzerPlayer(object):

    def __init__(self, pin="X8", timer_id=1, channel_id=1, callback=None, platform=None):

        if not platform:
            platform = sys.platform
            
        self.platform = platform
        
        if "esp" in platform:
            from machine import PWM, Pin
            self.buzzer_pin = PWM(Pin(pin, Pin.OUT), freq=1000)

        elif platform == "pyboard":
            import pyb
            from pyb import Pin, Timer
            self.pyb = pyb
            self.sound_pin = Pin(pin)
            self.timer = Timer(timer_id, freq=10000)
            self.channel = self.timer.channel(1, Timer.PWM, pin=self.sound_pin, pulse_width=0)
                  
        self.callback = callback

    def from_file(self, filename, chunksize=5):
        with open(filename, "rb") as f:
            while True:
                chunk = f.read(chunksize)
                if chunk:
                    for b in chunk:
                        yield chr(b)
                else:
                    break
    
    def play_nokia_tone(self, song, tempo=None, transpose=6, name="unkown"):
        
        pattern = "([0-9]*)(.*)([0-9]?)"
        def tune(): 
            for item in isplit(song):
                if item.startswith('t'):
                    _, tempo = item.split('=')
                    yield tempo
                    continue
                match = re.match(pattern, item)
                duration = match.group(1)
                pitch = match.group(2)
                octave = match.group(3)

                if pitch == "-":
                    pitch = "r"
                if pitch.startswith("#"):
                    pitch = pitch[1] + "#" + pitch[2:]
                dotted = pitch.startswith(".")
                duration = -int(duration) if dotted else int(duration)
                yield (pitch + octave, int(duration))

        t = tune()
        if not tempo:
            tempo = next(t)
        print("tempo",tempo)    
        #self.play_tune(tempo, t, transpose=transpose, name=name)

    def tone(self, freq, duration=0, duty=30):
        self.buzzer_pin.freq(int(freq))
        self.buzzer_pin.duty(duty)
        time.sleep_us( int(duration * 0.9 * 1000) )
        self.buzzer_pin.duty(0)
        time.sleep_us(int(duration * 0.1 * 1000))


        if callable(self.callback):
            self.callback(freq)
            
#     def play_tune(self, tempo, tune, transpose=0, name="unknown"):
#         print("\n== playing '%s' ==:" % name)
#         print(tempo)
#         full_notes_per_second = float(tempo) / 60 / 4
#         full_note_in_samples = SAMPLING_RATE / full_notes_per_second
#         for note_pitch, note_duration in tune:
#             print(note_pitch, note_duration)
#             duration = int(full_note_in_samples / note_duration)
#             if note_pitch == "r":
#                 self.tone(0, duration, 0)
#             else:
#                 freq = note_freq(note_pitch)
#                 if transpose: freq *= 2 ** transpose
#                 print("%s " % note_pitch, end="")
#                 self.tone(freq, duration, 30)
#                 
#         self.tone(0, 0, 0)

#     if MidiFile:
#         def play_midi(self, filename, track=1,  transpose=6):
#             midi = MidiFile(filename)
#             tune = midi.read_track(track)
#             self.play_tune(midi.tempo, tune, transpose=transpose, name=filename)
# 
#     if RTTTL:
#         def play_rtttl(self, input):
#             tune = RTTTL(input)    
#             for freq, msec in tune.notes():
#                 self.tone(freq, msec)

