import pygame
from player import Player
from bullet import Bullet

size = WIDTH, HEIGHT = 1280, 960
FPS = 60

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("shooter")
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    player_group = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    player = Player(player_group)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Bullet(bullets_group, event.pos, player.rect.center)
        screen.fill(pygame.Color("Black"))
        player_group.draw(screen)
        player_group.update()
        bullets_group.draw(screen)
        bullets_group.update()
        pygame.display.flip()
        clock.tick(FPS)
