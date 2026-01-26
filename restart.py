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
    import subprocess, sys, os
    try:
        # Use Popen to avoid shell/quoting issues on Windows when paths contain spaces.
        subprocess.Popen([sys.executable] + sys.argv)
    except Exception:
        # Fallback to exec if Popen fails
        try:
            os.execl(sys.executable, sys.executable, *sys.argv)
        except Exception:
            pass
    # Ensure current process exits
    try:
        os._exit(0)
    except Exception:
        pass
