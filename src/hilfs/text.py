import pygame


def text(surf, text, size, x, y, font_name):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, pygame.Color("white"))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
