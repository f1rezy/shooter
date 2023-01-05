import pygame
from player import Player

size = WIDTH, HEIGHT = 1280, 960
FPS = 60

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("")
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    player = Player(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.fill(pygame.Color("Black"))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
