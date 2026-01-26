import os
import wave
import struct
import random

def make_noise_wav(path, duration=0.6, rate=22050):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    nframes = int(duration * rate)
    with wave.open(path, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        frames = bytearray()
        for i in range(nframes):
            # white noise with exponential decay
            t = i / rate
            decay = max(0.0, 1.0 - t / duration)
            sample = int((random.uniform(-1, 1) * decay) * 32767 * 0.6)
            frames += struct.pack('<h', sample)
        wf.writeframes(frames)

if __name__ == '__main__':
    ws_path = os.path.join(os.path.dirname(__file__), 'assets', 'explosion.wav')
    make_noise_wav(ws_path)
    print('Wrote', ws_path)
