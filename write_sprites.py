import os
import struct

# Create small BMP 24-bit images (no compression)
# Simple utility to create a solid-color square BMP

def write_bmp(path, w, h, r, g, b):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    row_padded = (w * 3 + 3) & ~3
    filesize = 14 + 40 + row_padded * h
    with open(path, 'wb') as f:
        # BMP header
        f.write(b'BM')
        f.write(struct.pack('<I', filesize))
        f.write(b'\x00\x00')
        f.write(b'\x00\x00')
        f.write(struct.pack('<I', 14 + 40))
        # DIB header
        f.write(struct.pack('<I', 40))
        f.write(struct.pack('<i', w))
        f.write(struct.pack('<i', h))
        f.write(struct.pack('<H', 1))
        f.write(struct.pack('<H', 24))
        f.write(struct.pack('<I', 0))
        f.write(struct.pack('<I', row_padded * h))
        f.write(struct.pack('<i', 2835))
        f.write(struct.pack('<i', 2835))
        f.write(struct.pack('<I', 0))
        f.write(struct.pack('<I', 0))
        # pixel data (bottom-up)
        for y in range(h):
            row = bytearray()
            for x in range(w):
                # BMP stores as B,G,R
                row += bytes((b, g, r))
            # padding
            while len(row) < row_padded:
                row += b'\x00'
            f.write(row)


if __name__ == '__main__':
    write_bmp(os.path.join('assets', 'player.bmp'), 32, 32, 80, 200, 250)
    write_bmp(os.path.join('assets', 'enemy.bmp'), 28, 28, 240, 80, 100)
    write_bmp(os.path.join('assets', 'bullet.bmp'), 6, 12, 255, 220, 120)
    print('Wrote assets/player.bmp, assets/enemy.bmp, assets/bullet.bmp')
