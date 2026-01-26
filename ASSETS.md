# Assets and formats

Required audio assets (place in `assets/`):
- `shoot.wav` — bullet sound (WAV)
- `explosion.wav` — enemy destroyed (WAV)
- `music_loop.wav` — background music (WAV, optional)

Recommended image assets (place in `assets/`):
- `player.png`  (preferred) — player sprite (PNG)
- `enemy.png`   (preferred) — enemy sprite (PNG)
- `bullet.png`  (preferred) — bullet sprite (PNG)

Notes:
- The game will prefer PNG files and fall back to BMP (`.bmp`) if PNGs are not present.
- If no sprite files exist the game will draw simple rectangles.
