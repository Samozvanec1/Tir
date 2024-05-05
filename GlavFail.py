import random

import pygame
pygame.init()

SCREEN_WIDTH = 880
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
global text

pygame.display.set_caption("Игра В ТИР")

icon = pygame.image.load("img/Стрелы.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint( 1, SCREEN_WIDTH - (target_width + 1))
target_y = random.randint( 1, SCREEN_HEIGHT - (target_height + 1))

color = (random.randint (0, 255), random.randint (0, 255), random.randint(0, 255))

running = True
Schet = 0


while  running:
    screen.fill(color)
    font = pygame.font.SysFont('Times New Roman', 50)
    text = font.render("Yes, накликли:  ", True, 'WHITE')
    font = pygame.font.SysFont('Times New Roman', 250)
    text2 = font.render(str(Schet), True, 'WHITE')
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - (target_width))
                target_y = random.randint(0, SCREEN_HEIGHT - (target_height))

                Schet +=1




    screen.blit(target_img, (target_x, target_y))
    screen.blit(text, (10, 10))
    screen.blit(text2, (10,30))

    pygame.display.update()


pygame.quit()