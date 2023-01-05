import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.Surface((50, 50))
        self.image.fill(pygame.Color("Green"))
        self.rect = self.image.get_rect(center=(1280 // 2, 960 // 2))
        self.speedx = 0
        self.speedy = 0
        self.hp = 100

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -4
        if keystate[pygame.K_d]:
            self.speedx = 4

        if self.rect.right > 1280:
            self.rect.right = 1280
        if self.rect.left < 0:
            self.rect.left = 0

        if keystate[pygame.K_w]:
            self.speedy = -4
        if keystate[pygame.K_s]:
            self.speedy = 4

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > 960:
            self.rect.bottom = 960
        self.rect.x += self.speedx
        self.rect.y += self.speedy
