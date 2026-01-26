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

        _sound_impl = _Dummy()

sound = _sound_impl

__all__ = ['sound']
