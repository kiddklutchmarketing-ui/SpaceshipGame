import os
import zlib
import struct

# Minimal PNG writer for solid-color RGB images (no external deps).
# Writes non-interlaced 8-bit RGB PNG.

def write_png(path, w, h, r, g, b):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)

    # PNG signature
    png = b'\x89PNG\r\n\x1a\n'
    # IHDR
    ihdr = struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)  # color type 2 = truecolor RGB
    png += chunk(b'IHDR', ihdr)

    # IDAT: build raw scanlines
    scanlines = bytearray()
    for y in range(h):
        # filter type 0
        scanlines.append(0)
        for x in range(w):
            scanlines += bytes((r, g, b))
    compressed = zlib.compress(bytes(scanlines), level=9)
    png += chunk(b'IDAT', compressed)
    png += chunk(b'IEND', b'')

    with open(path, 'wb') as f:
        f.write(png)


if __name__ == '__main__':
    write_png(os.path.join('assets', 'player.png'), 32, 32, 80, 200, 250)
    write_png(os.path.join('assets', 'enemy.png'), 28, 28, 240, 80, 100)
    write_png(os.path.join('assets', 'bullet.png'), 6, 12, 255, 220, 120)
    print('Wrote assets/player.png, assets/enemy.png, assets/bullet.png')
