import pyaudio
import numpy as np

RATE = 16000
CHUNK = 1024

def record(seconds):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1,
                    rate=RATE, input=True, frames_per_buffer=CHUNK)
    print(f"Recording for {seconds} seconds...")
    frames = []
    for _ in range(int(RATE / CHUNK * seconds)):
        frames.append(stream.read(CHUNK))

    stream.stop_stream()
    stream.close()
    p.terminate()
    return b''.join(frames)

def analyze(data):
    samples = np.frombuffer(data, dtype=np.int16)
    duration = len(samples) / RATE
    avg = np.mean(np.abs(samples))
    return duration, avg

def compare(d1, v1, d2, v2):
    print("\n--- Comparision ---")

    if d1 > d2:
        print(f"Recording-1 is longer by {(d1-d2):.2f}s")
    else:
        print(f"Recording-2 is longer by {(d2-d1):.2f}s")
    
    if v1 > v2:
        print("Recording-1 is louder")
    else:
        print("Recording-2 is louder")

audio1 = record(5)
d1, v1 = analyze(audio1)

audio2 = record(5)
d2, v2 = analyze(audio2)

compare(d1, v1, d2, v2)