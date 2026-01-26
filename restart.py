import pygame

def restart_game():
    """Restart the current Python process.

    Call this from your game code when you want to immediately restart the
    program (exits pygame cleanly then re-execs the Python interpreter).
    """
    try:
        pygame.quit()
    except Exception:
        pass
    import os, sys
    os.execl(sys.executable, sys.executable, *sys.argv)
