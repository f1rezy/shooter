import pygame
from player import Player
from bullet import Bullet
from enemy import Enemy

SIZE = WIDTH, HEIGHT = 640, 480
FPS = 60
WHITE = (255, 255, 255)
hp = 100

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("shooter")
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    time = pygame.USEREVENT + 1
    pygame.time.set_timer(time, 500)

    font_name = pygame.font.match_font('arial')


    def score_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)


    sprite_group = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    player = Player()
    sprite_group.add(player)
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet((player.rect.centerx, player.rect.top))
                bullets_group.add(bullet)

            if event.type == time:
                enemy = Enemy()
                enemy_group.add(enemy)
                sprite_group.add(enemy)

        hits = pygame.sprite.spritecollide(player, enemy_group, False)
        if hits:
            running = False

        screen.fill(pygame.Color("Black"))
        sprite_group.draw(screen)
        sprite_group.update()

        hits = pygame.sprite.groupcollide(enemy_group, bullets_group, True, True)
        for hit in hits:
            enemy = Enemy()
            sprite_group.add(enemy)
            enemy_group.add(enemy)
            score += 1

        bullets_group.draw(screen)
        bullets_group.update()
        enemy_group.draw(screen)
        enemy_group.update()
        score_text(screen, str(score), 36, WIDTH / 2, 10)
        pygame.display.flip()
        clock.tick(FPS)
