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

- Notes:
- Development Python version: 3.11.9
- Audio uses `pygame.mixer` when available. On Windows there is a fallback to `winsound` for simple playback but volume control and music require `pygame`.
- If you prefer to generate placeholder assets, there are small generator scripts in the repo (`generate_music_wav.py`, `generate_explosion_wav.py`, `generate_shoot_wav.py`).
- Use the project's venv interpreter in your editor (VS Code: "Python: Select Interpreter") to avoid unresolved-import issues.

If you want, I can help add packaging, an installer, or export a single-file build for distribution.
# Extras added by maintainer:
- Meteor sprites: `assets/meteor.png` (auto-generated with `generate_sprites_png.py`).
- Launchers: `launch_game.py` (Python launcher), `run_game_venv.ps1` (PowerShell), and a Desktop shortcut created on your Desktop.
- Build helper: `build_exe.ps1` to create a one-file EXE using PyInstaller.
- CI: `.github/workflows/ci.yml` (Windows runner using Python 3.11.9).
- Tests: basic smoke test `tests/test_imports.py`.
# Sandbox & Docker

The repo includes a minimal sandbox runner and middleware supporting JWT/JWKS and optional Docker-based execution. To run tests with the Docker-enabled sandbox locally, enable the env var and run tests:

PowerShell:

```powershell
$env:SANDBOX_USE_DOCKER = '1'
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
```

To verify JWTs against a JWKS endpoint, set `SANDBOX_JWKS_URL`:

```powershell
$env:SANDBOX_JWKS_URL = 'https://example.com/.well-known/jwks.json'
```

An optional seccomp profile placeholder is included at `tools/seccomp.json`. Replace with a tested profile before enabling it in production.
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

To run the game via the repo venv (recommended):

```powershell
& '.\.venv\Scripts\python.exe' launch_game.py
```

To build a single-file executable (Windows PowerShell):

```powershell
.\build_exe.ps1
```

## Download

Download the latest packaged release (Windows exe + assets) from the GitHub release:

- Spaceship Game v1.0.0: https://github.com/kiddklutchmarketing-ui/SpaceshipGame/releases/tag/v1.0.0

Quick run (Windows):

1. Download and extract `SpaceshipGame_release.zip`.
2. Make sure the `SpaceshipGame.exe` and the `assets/` folder are in the same directory.
3. Double-click `SpaceshipGame.exe` or run from PowerShell:

```powershell
cd <path-to-extracted-folder>
.\SpaceshipGame.exe
```

If you'd like, I can add a small badge or link to the repo homepage pointing to the release.
