import pygame
from random import randrange


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (50, 70))
        self.rand_x = randrange(50, 590, 50)
        self.rect = self.image.get_rect(center=(self.rand_x, 10))
        self.speedy = 0

    def update(self, speed, group):
        if pygame.sprite.spritecollideany(self, group):
            self.kill()

        self.speedy = 0

        if self.rect.bottom >= 500:
            self.kill()

        self.speedy = speed
        self.rect.centery += self.speedy
