import pygame

display_length, display_width = 800, 800 


pygame.init()

pygame.display.set_caption("Modelo básico de funcionamento para Pygame")

main_screen = pygame.display.set_mode([display_length, display_width])
Clock = pygame.time.Clock()

i = 0 

while 1:

    i = i + 1
    if i > 255:
        i = 0 

    main_screen.fill([255,255,255])








    pygame.display.update()
    Clock.tick(120)