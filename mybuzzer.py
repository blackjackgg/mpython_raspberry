from buzzer import BuzzerPlayer
from test.nokia_songs import songs


if __name__ == "__main__":
    buzz = BuzzerPlayer(pin=26)

    try:
        while True:
            for song_name, v in songs.items():
                buzz.play_nokia_tone(tempo=v, song=v, name=song_name)
                print("runnnn")
    finally:
        print("fuck")


