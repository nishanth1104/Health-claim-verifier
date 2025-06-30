import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

model = whisper.load_model("base")

def record_and_transcribe():
    duration = 5  # seconds
    fs = 44100

    print("🎤 Speak now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write("output.wav", fs, recording)

    result = model.transcribe("output.wav", language="en")
    return result['text']
