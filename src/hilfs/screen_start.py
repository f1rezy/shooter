import pygame
import sys
from load_image import load_image

clock = pygame.time.Clock()

FPS = 60


def screen_start(screen):
    fon = pygame.transform.scale(load_image('back_all.png'), (640, 480))
    fon_rect = fon.get_rect()
    screen.blit(fon, fon_rect)

    font_name = pygame.font.Font(None, 60)
    name_text = font_name.render('dungeon shooter', True, (100, 200, 250))
    name_rect = name_text.get_rect()
    name_rect.center = fon_rect.center
    name_rect.top -= 200

    font_ruls = pygame.font.Font(None, 22)
    ruls_text = font_ruls.render('Перед началом игры убедитесь,'
                                 ' что ваши силы равны тому чтобы пройти'
                                 ' эту игру', True, (100, 150, 250))
    ruls_rect = ruls_text.get_rect(center=(320, 100))

    font_start = pygame.font.Font(None, 30)
    start_text = font_start.render('Для начала игры, нажмите любую клавишу клавиатуры', True, (100, 150, 250))
    start_rect = start_text.get_rect(center=(320, 240))

    key_a = load_image('key_a.png')
    rect_a = key_a.get_rect(center=(50, 350))

    font_a = pygame.font.Font(None, 20)
    key_a_text = font_a.render('- передвижение влево', True, 'Gray')
    key_a_rect = key_a_text.get_rect(center=(160, 350))

    key_d = load_image('key_d.png')
    rect_d = key_d.get_rect(center=(50, 430))

    font_d = pygame.font.Font(None, 20)
    key_d_text = font_d.render('- передвижение вправо', True, 'Gray')
    key_d_rect = key_d_text.get_rect(center=(160, 430))

    key_space = load_image('key_space.png')
    rect_space = key_space.get_rect(center=(320, 390))

    font_space = pygame.font.Font(None, 20)
    key_space_text = font_space.render('- стрельба', True, 'Gray')
    key_space_rect = key_space_text.get_rect(center=(440, 390))

    screen.blit(name_text, name_rect)
    screen.blit(ruls_text, ruls_rect)
    screen.blit(key_a, rect_a)
    screen.blit(key_d, rect_d)
    screen.blit(key_a_text, key_a_rect)
    screen.blit(key_d_text, key_d_rect)
    screen.blit(key_space, rect_space)
    screen.blit(key_space_text, key_space_rect)
    screen.blit(start_text, start_rect)

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
