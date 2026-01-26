import pygame
import random
from settings import *

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6,12))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=(x,y))

    def update(self):
        self.rect.y += 6
        if self.rect.top > HEIGHT:
            self.kill()


def try_fire(enemy, *groups):
    """Attempt to fire from an enemy with a ~1/121 chance.

    If firing occurs, an EnemyBullet is created at the enemy's bottom center,
    added to any provided sprite groups, and returned. Otherwise returns None.
    """
    if random.randint(0, 120) == 1:
        eb = EnemyBullet(enemy.rect.centerx, enemy.rect.bottom)
        if groups:
            try:
                eb.add(*groups)
            except Exception:
                # best-effort: ignore group-add failures during dev
                pass
        return eb
    return None
