"""Simple compatibility wrapper so `import sound` works in the game.
Delegates to `assets_shooter_wav.sound` implementation.
"""
try:
    from assets_shooter_wav import sound as _sound_impl
except Exception:
    # fallback: try to load the bridge file if running from different cwd
    try:
        import runpy
        runpy.run_path(r'C:\Users\robin\assets_shooter_wav.py', run_name='assets_shooter_wav')
        from assets_shooter_wav import sound as _sound_impl
    except Exception:
        class _Dummy:
            def play(self, *a, **k):
                return None
            def set_volume(self, v):
                return None
            def toggle_mute(self):
                return None
            def play_music(self, loop=True):
                return None
            def stop_music(self):
                return None
            def set_music_volume(self, v):
                return None

        _sound_impl = _Dummy()

sound = _sound_impl

__all__ = ['sound']

# Module-level convenience functions so callers can use `sound.play(name)`
def play(name):
    try:
        return _sound_impl.play(name)
    except Exception:
        try:
            return _sound_impl.sound.play(name)
        except Exception:
            return None

def set_volume(v):
    try:
        return _sound_impl.set_volume(v)
    except Exception:
        try:
            return _sound_impl.sound.set_volume(v)
        except Exception:
            return None

def toggle_mute():
    try:
        return _sound_impl.toggle_mute()
    except Exception:
        try:
            return _sound_impl.sound.toggle_mute()
        except Exception:
            return None

def play_music(loop=True):
    try:
        return _sound_impl.play_music(loop=loop)
    except Exception:
        try:
            return _sound_impl.sound.play_music(loop=loop)
        except Exception:
            return None

def stop_music():
    try:
        return _sound_impl.stop_music()
    except Exception:
        try:
            return _sound_impl.sound.stop_music()
        except Exception:
            return None
