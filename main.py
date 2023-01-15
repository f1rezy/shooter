import pygame
from player import Player
from bullet import Bullet
from enemy import Enemy

SIZE = WIDTH, HEIGHT = 640, 480
FPS = 60


def text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, pygame.Color("white"))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("shooter")
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    timer = 1000

    time = pygame.USEREVENT + 1
    pygame.time.set_timer(time, timer)

    font_name = pygame.font.match_font('arial')

    player_group = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    player = Player(player_group)
    global_score = 0
    score = 0
    level = 1
    speed = 2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Bullet(bullets_group, (player.rect.centerx, player.rect.top))
            if event.type == time:
                enemy = Enemy()
                enemy_group.add(enemy)

        if player.hp <= 0:
            running = False

        if score == 10:
            level += 1
            score = 0
            speed += 2
            timer /= 2
            player.hp += 20
            if player.hp > 100:
                player.hp -= (player.hp % 100)

        screen.fill(pygame.Color("Black"))
        player_group.draw(screen)
        player_group.update(enemy_group)

        hits = pygame.sprite.groupcollide(enemy_group, bullets_group, True, True)
        for hit in hits:
            enemy = Enemy()
            enemy_group.add(enemy)
            global_score += 1
            score += 1

        bullets_group.draw(screen)
        bullets_group.update()
        enemy_group.draw(screen)
        enemy_group.update(speed, player_group)
        text(screen, str(score), 36, WIDTH / 2, 10)
        text(screen, f"level: {level}", 36, 75, 10)
        text(screen, f"hp: {player.hp}", 36, 575, 10)
        pygame.display.flip()
        clock.tick(FPS)
