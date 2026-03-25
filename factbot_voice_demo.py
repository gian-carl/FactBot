import sounddevice as sd
import numpy as np
import speech_recognition as sr
import queue
import threading

def record_audio(duration=3, samplerate=16000):
    """Record audio for a given duration (seconds) and return raw bytes."""
    audio_queue = queue.Queue()
    recording = True

    def callback(indata, frames, time, status):
        audio_queue.put(indata.copy())

    with sd.InputStream(samplerate=samplerate, channels=1, callback=callback):
        # Collect chunks for the specified duration
        chunks = []
        for _ in range(int(duration * samplerate / 512)):  # 512 is typical block size
            try:
                chunk = audio_queue.get(timeout=0.5)
                chunks.append(chunk)
            except queue.Empty:
                break
        recording = False
        # Combine chunks
        audio_data = np.concatenate(chunks, axis=0)
        # Convert to 16‑bit integer bytes
        audio_bytes = (audio_data * 32767).astype(np.int16).tobytes()
        return audio_bytes

def main():
    recognizer = sr.Recognizer()
    print("Voice‑to‑Text Accuracy Test")
    print("===========================")
    print("Speak a phrase after pressing Enter.")
    print("Type 'stop' to exit.\n")

    while True:
        input("Press Enter when ready to speak...")
        print("Listening...", end='', flush=True)

        # Record 3 seconds of audio
        audio_bytes = record_audio(duration=3)

        # Create AudioData object for speech_recognition
        audio = sr.AudioData(audio_bytes, 16000, 2)

        try:
            text = recognizer.recognize_google(audio)
            print(f"\rYou said: {text}")
        except sr.UnknownValueError:
            print("\rSorry, I could not understand that.")
        except sr.RequestError as e:
            print(f"\rSpeech recognition service error: {e}")

        # Check if user wants to stop
        if text.lower() in ["stop", "exit", "quit"]:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()