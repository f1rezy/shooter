import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color("Green"))
        self.rect = self.image.get_rect(center=(640 // 2, 480 - 20))
        self.speedx = 0
        self.hp = 100

    def update(self):
        self.speedx = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8

        self.rect.centerx += self.speedx

        if self.rect.right > 1280:
            self.rect.right = 1280
        if self.rect.left < 0:
            self.rect.left = 0
