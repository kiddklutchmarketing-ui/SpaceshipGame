import random

class CameraShake:
    def __init__(self):
        self.intensity = 0

    def shake(self, strength=5):
        self.intensity = strength

    def apply(self, rect):
        if self.intensity > 0:
            self.intensity -= 1
            rect.x += random.randint(-3,3)
            rect.y += random.randint(-3,3)


# module-level singleton and convenience function so other modules can call
# `import camera; camera.shake()` without instantiating.
camera = CameraShake()

def shake(strength=5):
    """Trigger a camera shake of given strength (convenience wrapper).

    Usage: `import camera; camera.shake(6)`
    """
    try:
        camera.shake(strength)
    except Exception:
        pass
