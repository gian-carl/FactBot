"""
wake_word_demo.py – Continuous voice interaction with wake word "hey"
Fixed to ensure TTS works repeatedly.
"""

import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import queue
import time

# ----------------------------------------------------------------------
# Audio recording function
# ----------------------------------------------------------------------
def record_audio(duration=3, samplerate=16000):
    """Record audio for a fixed duration and return bytes."""
    audio_queue = queue.Queue()

    def callback(indata, frames, time, status):
        audio_queue.put(indata.copy())

    with sd.InputStream(samplerate=samplerate, channels=1, callback=callback):
        blocks_per_second = samplerate / 512
        total_blocks = int(duration * blocks_per_second)

        chunks = []
        for _ in range(total_blocks):
            try:
                chunk = audio_queue.get(timeout=0.5)
                chunks.append(chunk)
            except queue.Empty:
                break

        if not chunks:
            return None
        audio_data = np.concatenate(chunks, axis=0)
        audio_bytes = (audio_data * 32767).astype(np.int16).tobytes()
        return audio_bytes

# ----------------------------------------------------------------------
# Speech recognition helper
# ----------------------------------------------------------------------
def listen_for_phrase(recognizer, duration=3):
    """Record audio, transcribe, return text or None."""
    audio_bytes = record_audio(duration)
    if audio_bytes is None:
        return None
    audio = sr.AudioData(audio_bytes, 16000, 2)
    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None

# ----------------------------------------------------------------------
# Text‑to‑speech with a fresh engine each time (ensures it works)
# ----------------------------------------------------------------------
def speak(text):
    """Speak the given text using a new pyttsx3 engine."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    # Optional small delay to let the engine clean up
    time.sleep(0.1)

# ----------------------------------------------------------------------
# Main loop
# ----------------------------------------------------------------------
def main():
    recognizer = sr.Recognizer()

    speak("Wake word demo started. Say 'hey' to activate.")
    print("Bot: Wake word demo started. Say 'hey' to activate.\n")

    while True:
        print("Listening for wake word 'hey'...")
        phrase = listen_for_phrase(recognizer, duration=3)

        if phrase is None:
            continue

        print(f"User: {phrase}")

        # Check for exit command (can be said anytime)
        if "stop" in phrase or "exit" in phrase:
            speak("Goodbye!")
            print("Bot: Goodbye!")
            break

        # Check for wake word
        if "hey" in phrase:
            speak("Yes?")
            print("Bot: Yes?")

            # Now listen for the actual command
            print("Listening for command...")
            command = listen_for_phrase(recognizer, duration=4)
            if command is None:
                speak("Sorry, I didn't catch that.")
                print("Bot: Sorry, I didn't catch that.")
                continue

            print(f"User: {command}")

            # Speak back what the user said (for testing)
            response = f"You said: {command}"
            speak(response)
            print(f"Bot: {response}")

        else:
            print("(Not a wake word, continuing...)")

if __name__ == "__main__":
    main()