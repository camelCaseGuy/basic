import winsound
import time

# Define the note frequencies (Hz) from the original DATA lines
notes = [
    131,165,175,185,175,220,233,247,
    262,233,220,196,175,165,147,131,
    175,220,233,247,262,233,220,196,
    131,165,175,185,196,220,233,247,
    196,247,262,294,175,220,262,220,
    131,233,156,277,147,262,139,247
]

# Loop forever, just like the original BASIC code
while True:
    for note in notes:
        winsound.Beep(note, 120)  # 120 ms ~ matches SOUND duration of 6 clock ticks
