import pygame
import random

pygame.init()

screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0,0,0)

snake_segments = [(screen_width//2, screen_height//2)]
snake_dir = (1, 0)
snake_speed = 5

food_pos = (random.randint(0, screen_width//50 - 1) * 50, random.randint(0, screen_height//50-1)*50)

score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()


run = True

def is_collision(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key ==  pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)

    head_x, head_y = snake_segments[0]
    new_head = (head_x + snake_dir[0] * 50, head_y + snake_dir[1] * 50)
    if(new_head[0] < 0 or new_head[0] >= screen_width or 
       new_head[1] < 0 or new_head[1] >= screen_height or 
       new_head in snake_segments):
        run = False

    snake_segments.insert(0, new_head)

    if is_collision(new_head, food_pos):
        score += 1
        food_pos = (random.randint(0, screen_width//50 - 1) * 50, random.randint(0, screen_height//50 - 1)* 50)
    else:
        snake_segments.pop()

    screen.fill(black)
    pygame.draw.rect(screen, red,(*food_pos, 50, 50))

    for segment in snake_segments:
        pygame.draw.rect(screen, blue, (*segment, 50, 50))

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()
