"""
test_stt.py – Voice‑to‑Text Accuracy Test

This script records 3 seconds of audio after you press Enter,
sends it to Google's speech recognition, and prints the result.
"""

import sounddevice as sd
import numpy as np
import speech_recognition as sr
import queue
import time

def record_audio(duration=3, samplerate=16000):
    """
    Record audio for a fixed duration (seconds) using sounddevice.
    Returns the audio as bytes in 16‑bit PCM format (suitable for speech_recognition).
    """
    audio_queue = queue.Queue()

    def callback(indata, frames, time, status):
        """Called for each audio block; put it into the queue."""
        audio_queue.put(indata.copy())

    # Start the input stream
    with sd.InputStream(samplerate=samplerate, channels=1, callback=callback):
        # Calculate number of blocks to collect for the given duration
        # 512 is a typical block size, but we can compute dynamically:
        blocks_per_second = samplerate / 512
        total_blocks = int(duration * blocks_per_second)

        chunks = []
        for _ in range(total_blocks):
            try:
                # Wait up to 0.5 seconds for a block (should be plenty)
                chunk = audio_queue.get(timeout=0.5)
                chunks.append(chunk)
            except queue.Empty:
                # If we run out of data, stop early
                break

        # Concatenate all chunks into one array
        audio_data = np.concatenate(chunks, axis=0)

        # Convert float64 samples (-1..1) to 16‑bit integer bytes
        audio_bytes = (audio_data * 32767).astype(np.int16).tobytes()

        return audio_bytes

def main():
    recognizer = sr.Recognizer()
    print("🎤 Voice‑to‑Text Accuracy Test")
    print("==============================")
    print("Speak a phrase after pressing Enter.")
    print("Type 'stop' to exit.\n")

    while True:
        input("⏎  Press Enter when ready to speak...")
        print("🎙️  Listening (3 seconds)...", end='', flush=True)

        # Record audio
        try:
            audio_bytes = record_audio(duration=3)
        except Exception as e:
            print(f"\n⚠️  Recording error: {e}")
            continue

        # Create an AudioData object for speech_recognition
        audio = sr.AudioData(audio_bytes, 16000, 2)

        # Send to Google
        try:
            text = recognizer.recognize_google(audio)
            print(f"\r📝 You said: {text}")
        except sr.UnknownValueError:
            print("\r😕 Sorry, I could not understand that.")
        except sr.RequestError as e:
            print(f"\r🌐 Speech recognition service error: {e}")

        # Stop condition
        if text.lower() in ["stop", "exit", "quit"]:
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()