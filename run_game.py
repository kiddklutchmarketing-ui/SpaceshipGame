import os
import sys
import subprocess

def main():
    repo_root = os.path.abspath(os.path.dirname(__file__))
    game_path = os.path.join(repo_root, 'PythonProject', 'Spaceship Game Project 2.py')
    if not os.path.exists(game_path):
        print('Game entry not found:', game_path)
        return 2
    # Launch the game using the same interpreter
    try:
        subprocess.run([sys.executable, game_path])
    except Exception as e:
        print('Failed to launch game:', e)
        return 1
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
