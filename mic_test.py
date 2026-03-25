import sounddevice as sd
import numpy as np

def print_volume(indata, frames, time, status):
    volume = np.sqrt(np.mean(indata**2))
    print(f"Volume: {volume:.5f}", end='\r')

stream = sd.InputStream(callback=print_volume)
with stream:
    input("Speak now... Press Enter to stop.")