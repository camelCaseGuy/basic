import pygame
import time
import math

# Settings:
note_length = 0.3  # Duration of each note in seconds



# Initialize mixer
# pygame.mixer.init(frequency=44100, size=-16, channels=1)
pygame.mixer.init(frequency=44100, size=8, channels=1)

def play_tone(frequency, duration):
    # sample_rate = 22050
    # sample_rate = 44100
    sample_rate = 96000
    # sample_rate = 144100
    n_samples = int(sample_rate * duration)
    buf = bytearray()

    for i in range(n_samples):
        t = i / sample_rate
        # value = int(32767.0 * math.sin(2.0 * math.pi * frequency * t))
        value = 32767 if math.sin(2.0 * math.pi * frequency * t) > 0 else -32768
        buf += value.to_bytes(2, byteorder='little', signed=True)

    sound = pygame.mixer.Sound(buffer=buf)
    sound.fadeout(100)  # fade out over 100 ms
    sound.play()
    time.sleep(duration)
    sound.stop()

notes = [
    131,165,175,185,175,220,233,247,
    262,233,220,196,175,165,147,131,
    175,220,233,247,262,233,220,196,
    131,165,175,185,196,220,233,247,
    196,247,262,294,175,220,262,220,
    131,233,156,277,147,262,139,247
]

while True:
    for note in notes:
        play_tone(note, note_length)
