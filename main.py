import sys

import pygame
from player import Player
from bullet import Bullet
from enemy import Enemy
from load_image import load_image
from screen_start import screen_start
from screen_end import screen_end
from text import text
from write_res import write

SIZE = WIDTH, HEIGHT = 640, 480
FPS = 60
enemy_images = {
    '1': load_image('enemy1.png'),
    '2': load_image('enemy1.png'),
    '3': load_image('enemy2.png'),
    '4': load_image('enemy2.png'),
    '5': load_image('enemy3.png'),
    '6': load_image('enemy3.png'),
}

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

    screen_start(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Bullet(bullets_group, (player.rect.centerx, player.rect.top))

            if event.type == time:
                enemy = Enemy(enemy_images[str(level)])
                enemy_group.add(enemy)

        if player.hp <= 0:
            print(global_score)
            write(global_score)
            screen_end(screen)
            running = False

        if score == 10:
            level += 1
            score = 0
            speed += 2
            timer //= 2
            pygame.time.set_timer(time, timer)
            player.hp += 20
            if player.hp > 100:
                player.hp -= (player.hp % 100)

        screen.fill(pygame.Color("Black"))
        player_group.draw(screen)
        player_group.update(enemy_group)

        hits = pygame.sprite.groupcollide(enemy_group, bullets_group, True, True)
        for hit in hits:
            global_score += 1
            score += 1

        bullets_group.draw(screen)
        bullets_group.update()
        enemy_group.draw(screen)
        enemy_group.update(speed, player_group)
        text(screen, str(score), 36, WIDTH / 2, 10, font_name)
        text(screen, f"level: {level}", 36, 75, 10, font_name)
        text(screen, f"hp: {player.hp}", 36, 575, 10, font_name)
        pygame.display.flip()
        clock.tick(FPS)
