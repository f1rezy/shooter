import pygame
from random import randrange


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color("Red"))
        self.rand_x = randrange(50, 1230, 100)
        self.rect = self.image.get_rect(center=(self.rand_x, 10))
        self.speedy = 0

    def update(self):
        self.speedy = 0
        if self.rect.bottom != 1100:
            self.speedy = 2
        elif self.rect.bottom == 1100:
            self.kill()

        self.rect.centery += self.speedy
