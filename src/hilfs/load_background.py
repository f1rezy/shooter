import pygame
from load_image import load_image

tiles_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group)
        self.image = pygame.transform.scale(load_image("floor.png"), (32, 32))
        self.rect = self.image.get_rect().move(
            32 * pos_x, 32 * pos_y)


def generate_level():
    for y in range(15):
        for x in range(20):
            Tile(x, y)
