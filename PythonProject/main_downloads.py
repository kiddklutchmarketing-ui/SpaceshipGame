import pygame
import sys
import importlib
import importlib.util
from pathlib import Path

# Ensure the script's directory and the user's home directory are on sys.path so local
# modules (player.py, bullet.py) placed in the project folder or the user folder can be
# imported when running from the project folder.
project_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(project_dir))
sys.path.insert(1, str(Path.home()))

from settings import *
from player import Player
from bullet import Bullet
try:
    if importlib.util.find_spec("enemy") is not None:
        mod = importlib.import_module("enemy")
        Enemy = getattr(mod, "Enemy")
        Boss = getattr(mod, "Boss")
    else:
        # module not available on sys.path
        raise ImportError
except Exception:
    # Fallback Enemy/Boss implementations to avoid import errors during development/testing.
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x=0, y=0, *groups):
            super().__init__(*groups)
            self.image = pygame.Surface((24, 24))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect(center=(x, y))
            self.speed = 2

        def update(self):
            self.rect.y += self.speed

    class Boss(Enemy):
        def __init__(self, x=0, y=0, *groups):
            super().__init__(x, y, *groups)
            self.image = pygame.Surface((64, 64))
            self.image.fill((128, 0, 128))
            self.rect = self.image.get_rect(center=(x, y))
            self.speed = 1

try:
    if importlib.util.find_spec("effects") is not None:
        mod = importlib.import_module("effects")
        Explosion = getattr(mod, "Explosion")
    else:
        # module not available on sys.path
        raise ImportError
except Exception:
    # Fallback Explosion implementation to avoid import errors during development/testing.
    class Explosion(pygame.sprite.Sprite):
        def __init__(self, x=0, y=0, *groups):
            super().__init__(*groups)
            self.image = pygame.Surface((16, 16))
            self.image.fill((255, 255, 0))
            self.rect = self.image.get_rect(center=(x, y))
            self.lifetime = 30

        def update(self):
            self.lifetime -= 1
            if self.lifetime <= 0:
                self.kill()

from ui import draw_ui
from sound import SoundEngine   # ← ADD THIS
try:
    from powerup import PowerUp
except Exception:
    # Fallback PowerUp for development
    class PowerUp(pygame.sprite.Sprite):
        def __init__(self, x=0, y=0, type='health', *groups):
            super().__init__(*groups)
            self.type = type
            self.image = pygame.Surface((16, 16))
            if type == 'health':
                self.image.fill((0, 255, 0))
            elif type == 'rapid':
                self.image.fill((255, 160, 0))
            else:
                self.image.fill((200, 200, 200))
            self.rect = self.image.get_rect(center=(x, y))


# dynamic import for pygame
try:
    pygame = importlib.import_module("pygame")
except Exception:
    try:
        pygame = importlib.import_module("pygame_ce")
    except Exception:
        raise ImportError("pygame not installed. Install with: python -m pip install pygame")

try:
    if importlib.util.find_spec("player") is not None:
        mod = importlib.import_module("player")
        Player = getattr(mod, "Player")
    else:
        # module not available on sys.path
        raise ImportError
except Exception:
    # Fallback Player implementation to avoid import errors during development/testing.
    class Player(pygame.sprite.Sprite):
        def __init__(self, *groups):
            super().__init__(*groups)
            self.image = pygame.Surface((32, 32))
            self.image.fill((0, 255, 0))
            self.rect = self.image.get_rect(center=(0, 0))
            self.health = 100
            # firing: cooldown in milliseconds
            self.fire_cooldown = 300
            self._base_fire_cooldown = self.fire_cooldown
            self._last_shot = 0
            # rapid-fire timer in ms
            self.rapid_timer = 0

        def try_shoot(self, *groups):
            now = pygame.time.get_ticks()
            if now - self._last_shot >= self.fire_cooldown:
                Bullet(self.rect.centerx, self.rect.top, *groups)
                self._last_shot = now


try:
    mod = importlib.import_module("bullet")
    Bullet = getattr(mod, "Bullet")
except Exception:
    # Fallback Bullet implementation to avoid import errors during development/testing.
    # This simple Sprite matches a common Bullet interface: accepts groups when constructed
    # and implements update() to move upward and self.kill() when off-screen.
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y, *groups):
            super().__init__(*groups)
            self.image = pygame.Surface((4, 10))
            self.image.fill((255, 255, 0))
            self.rect = self.image.get_rect(center=(x, y))
            self.speed = -8

        def update(self):
            self.rect.y += self.speed
            if self.rect.bottom < 0:
                self.kill()

# Initialize pygame
pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (600, 400)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Player + Bullet Test")

# Sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

# Create player (added to all_sprites)
player = Player(all_sprites)
player.rect.midbottom = (WIDTH // 2, HEIGHT - 20)

clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # spawn bullet into both groups, respect cooldown if supported
                if hasattr(player, 'try_shoot'):
                    player.try_shoot(all_sprites, bullets)
                else:
                    player.shoot(all_sprites, bullets)

    # Update
    all_sprites.update()

    # handle rapid-fire timer on player (restore cooldown when expired)
    try:
        if getattr(player, 'rapid_timer', 0) > 0:
            player.rapid_timer = max(0, player.rapid_timer - dt)
            if player.rapid_timer == 0:
                player.fire_cooldown = getattr(player, '_base_fire_cooldown', getattr(player, 'fire_cooldown', 300))
    except Exception:
        pass

    # Power-up collisions
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for p in hits:
        if getattr(p, 'type', None) == "health":
            player.health = min(100, getattr(player, 'health', 100) + 30)
        elif getattr(p, 'type', None) == "rapid":
            # enable rapid-fire on player for a short duration
            try:
                player.rapid_timer = 5000  # ms
                player.fire_cooldown = 100
            except Exception:
                pass

    # Draw
    screen.fill((50, 100, 200))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
