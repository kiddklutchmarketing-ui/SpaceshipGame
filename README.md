# Spaceship Game — Run & Development

Quick start (PowerShell):

1. Activate the project's venv (optional but recommended):

```powershell
& 'C:/Users/robin/PycharmProjects/.venv/Scripts/Activate.ps1'
```

2. Install dependencies into the venv (if not already installed):

```powershell
& 'C:/Users/robin/PycharmProjects/.venv/Scripts/python.exe' -m pip install -r C:/Users/robin/PycharmProjects/requirements.txt
```

3. Run the game:

```powershell
& 'C:/Users/robin/PycharmProjects/.venv/Scripts/python.exe' 'C:/Users/robin/PycharmProjects/PythonProject/Spaceship Game Project 2.py'
```

Controls (in-game):
- Left / Right or A / D — move
- Space — shoot (plays `shoot.wav`)
- ESC — quit
- M — mute/unmute sounds
- + / - — increase / decrease master volume
- B — toggle background music
- [ / ] — decrease / increase music volume

Where to put assets:
- Put your WAV files into the `assets/` folder. The game expects:
  - `assets/shoot.wav`
  - `assets/explosion.wav`
  - `assets/music_loop.wav` (optional background music)

Notes:
- Audio uses `pygame.mixer` when available. On Windows there is a fallback to `winsound` for simple playback but volume control and music require `pygame`.
- If you prefer to generate placeholder assets, there are small generator scripts in the repo (`generate_music_wav.py`, `generate_explosion_wav.py`, `generate_shoot_wav.py`).
- Use the project's venv interpreter in your editor (VS Code: "Python: Select Interpreter") to avoid unresolved-import issues.

If you want, I can help add packaging, an installer, or export a single-file build for distribution.
# Project run instructions

Use the project's virtual environment to run scripts. From PowerShell or a terminal, run:

```powershell
C:/Users/robin/PycharmProjects/.venv/Scripts/python.exe path\to\your_script.py
```

To install dependencies into the venv (already installed `pygame`):

```powershell
C:/Users/robin/PycharmProjects/.venv/Scripts/python.exe -m pip install -r requirements.txt
```

If VS Code still shows unresolved imports, select the interpreter `C:/Users/robin/PycharmProjects/.venv/Scripts/python.exe` via the Command Palette: "Python: Select Interpreter".
