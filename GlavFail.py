import random

import pygame
pygame.init()

SCREEN_WIDTH = 880
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра В ТИР")

icon = pygame.image.load("img/Стрелы")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint( 1, SCREEN_WIDTH - (target_width + 1))
target_y = random.randint( 1, SCREEN_HEIGHT - (target_height + 1))

color = (random.randint (0, 255), random.randint (0, 255), random.randint(0, 255))

running = True
while  running:
    pass


pygame.quit()