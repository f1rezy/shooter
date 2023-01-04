import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("")
    size = width, height = 1280, 960
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
