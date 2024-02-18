import pygame

pygame.init()

screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.display.update()
pygame.quit()
