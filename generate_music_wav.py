import os
import wave
import struct
import math

def make_loop(path, freq=110, duration=6.0, rate=22050, volume=0.2):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    nframes = int(duration * rate)
    amplitude = int(32767 * volume)
    with wave.open(path, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        frames = bytearray()
        for i in range(nframes):
            t = i / rate
            # two sine layers for a warm pad
            s = 0.5 * math.sin(2 * math.pi * freq * t) + 0.5 * math.sin(2 * math.pi * (freq * 1.5) * t)
            # slow amplitude modulation
            s *= (0.6 + 0.4 * math.sin(2 * math.pi * 0.2 * t))
            sample = int(amplitude * s)
            frames += struct.pack('<h', sample)
        wf.writeframes(frames)

if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), 'assets', 'music_loop.wav')
    make_loop(out)
    print('Wrote', out)
