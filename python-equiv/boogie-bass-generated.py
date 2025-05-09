import pygame
import time
import math

# === CONFIG ===
WAVEFORM = "triangle"   # Options: "sine", "square", "triangle", "sawtooth"
VOLUME = 0.5          # 0.0 to 1.0
SAMPLE_RATE = 128000   # 44100
NOTE_DURATION = 0.30  # seconds per note

# === Notes from BOOGIE BASS ===
notes = [
    131,165,175,185,175,220,233,247,
    262,233,220,196,175,165,147,131,
    175,220,233,247,262,233,220,196,
    131,165,175,185,196,220,233,247,
    196,247,262,294,175,220,262,220,
    131,233,156,277,147,262,139,247
]

pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1)

def generate_wave(frequency, duration, waveform="sine"):
    n_samples = int(SAMPLE_RATE * duration)
    buf = bytearray()
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        angle = 2.0 * math.pi * frequency * t

        if waveform == "sine":
            sample = math.sin(angle)
        elif waveform == "square":
            sample = 1.0 if math.sin(angle) >= 0 else -1.0
        elif waveform == "triangle":
            sample = 2.0 * abs(2.0 * (t * frequency - math.floor(t * frequency + 0.5))) - 1.0
        elif waveform == "sawtooth":
            sample = 2.0 * (t * frequency - math.floor(t * frequency + 0.5))
        else:
            sample = 0

        value = int(VOLUME * 32767 * sample)
        buf += value.to_bytes(2, byteorder='little', signed=True)

    return pygame.mixer.Sound(buffer=buf)

def play_tone(frequency, duration, waveform="sine"):
    sound = generate_wave(frequency, duration, waveform)
    sound.play()
    time.sleep(duration)
    sound.stop()

# === Main loop ===
print(f"Boogie Bass using {WAVEFORM} waveform...")
while True:
    for note in notes:
        play_tone(note, NOTE_DURATION, waveform=WAVEFORM)
