import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, coords, rect):
        super().__init__(group)
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color("White"))
        self.rect = self.image.get_rect(center=rect)
        self.x, self.y = coords

    def update(self):
        if self.rect.right > 1280:
            self.kill()

        if self.rect.left < 0:
            self.kill()

        if self.rect.top < 0:
            self.kill()

        if self.rect.bottom > 960:
            self.kill()

        if self.rect.x < self.x:
            self.rect.x += 1
        else:
            self.rect.x -= 1

        if self.rect.y < self.y:
            self.rect.y += 1
        else:
            self.rect.y -= 1
