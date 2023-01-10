import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color("White"))
        self.rect = self.image.get_rect(center=rect)

    def update(self):
        if self.rect.top < 0:
            self.kill()
        self.rect.y -= 4
