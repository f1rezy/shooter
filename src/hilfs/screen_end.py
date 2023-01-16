import pygame
import sys
from load_image import load_image

clock = pygame.time.Clock()

FPS = 60


def screen_end(screen):
    fon = pygame.transform.scale(load_image('back_all.png'), (640, 480))
    fon_rect = fon.get_rect()
    screen.blit(fon, fon_rect)

    font_name = pygame.font.Font(None, 50)
    name_text = font_name.render('Упс... Вы проиграли', True, (100, 200, 250))
    name_rect = name_text.get_rect()
    name_rect.center = fon_rect.center
    name_rect.top -= 200

    last_score = open('../../results.txt').readlines()
    font_last = pygame.font.Font(None, 50)
    last_text = font_last.render(f'Ваш счёт - {last_score[-1]}', True, (100, 200, 250))
    last_rect = last_text.get_rect()
    last_rect.center = fon_rect.center

    screen.blit(name_text, name_rect)
    screen.blit(last_text, last_rect)

    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                start = False
        pygame.display.flip()
        clock.tick(FPS)
