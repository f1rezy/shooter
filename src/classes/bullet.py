import pygame
from load_image import load_image


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, rect):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image("arrow.png"), (14, 42))
        self.rect = self.image.get_rect(center=rect)

    def update(self):
        if self.rect.top < 0:
            self.kill()
        self.rect.y -= 4
