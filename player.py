import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color("Green"))
        self.rect = self.image.get_rect(center=(640 // 2, 480 - 20))
        self.speedx = 0
        self.hp = 100

    def update(self, enemy_group):
        if pygame.sprite.spritecollideany(self, enemy_group):
            self.hp -= 10

        self.speedx = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5

        self.rect.centerx += self.speedx

        if self.rect.right > 640:
            self.rect.right = 640
        if self.rect.left < 0:
            self.rect.left = 0
