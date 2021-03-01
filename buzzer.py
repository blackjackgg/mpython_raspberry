import random
import logging
from buzzer import BuzzerPlayer, songs


if __name__ == "__main__":
    buzz = BuzzerPlayer(callback=blink_led)

    try:
        while True:
            for song_name, v in songs.items():
                tempo, song = v
                buzz.play_nokia_tone(tempo=tempo, song=song, name=song_name)
    finally:
        buzz.channel.pulse_width_percent(0)


