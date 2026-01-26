import os
import wave
import struct
import math

def make_wav(path, freq=660, duration=0.4, volume=0.5, rate=44100):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    nframes = int(duration * rate)
    amplitude = int(32767 * volume)
    with wave.open(path, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        frames = bytearray()
        for i in range(nframes):
            sample = int(amplitude * math.sin(2 * math.pi * freq * i / rate))
            frames += struct.pack('<h', sample)
        wf.writeframes(frames)

if __name__ == '__main__':
    # workspace assets path
    ws_path = os.path.join(os.path.dirname(__file__), 'assets', 'shoot.wav')
    make_wav(ws_path)
    # root path expected by the legacy module
    root_path = r'C:\Users\robin\assets\shoot.wav'
    try:
        make_wav(root_path)
    except Exception:
        pass
    print('WAV files written:')
    print(' -', ws_path)
    print(' -', root_path)
