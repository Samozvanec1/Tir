

import random

import pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
global text

pygame.display.set_caption("Игра В ТИР")

icon = pygame.image.load("img/Стрелы.jpg")
pygame.display.set_icon(icon)

dom_img = pygame.image.load("img/dom.png")
dom_width = 285
dom_height = 182
dom_x = 300
dom_y = 280

dino_img = pygame.image.load("img/dino.png")
dino_width = 300
dino_height = 156
dino_x = 700
dino_y = 595

grib_img = pygame.image.load("img/grib.png")
grib_width = 300
grib_height = 406
grib_x = -5
grib_y = 353

kust_img = pygame.image.load("img/kust.png")
kust_width = 300
kust_height = 236
kust_x = 650
kust_y = 80

avto_img = pygame.image.load("img/avto.png")
avto_width = 300
avto_height = 212
avto_x = random.randint( 1, SCREEN_WIDTH - (avto_width + 1))
avto_y = random.randint( 1, SCREEN_HEIGHT - (avto_height + 1))

dzin_img = pygame.image.load("img/dzin.png")
dzin_width = 300
dzin_height = 466
dzin_x = random.randint( 1, SCREEN_WIDTH - (dzin_width + 1))
dzin_y = random.randint( 1, SCREEN_HEIGHT - (dzin_height + 1))


lampa_img = pygame.image.load("img/lampa.png")
lampa_width = 300
lampa_height = 213
lampa_x = random.randint( 1, SCREEN_WIDTH - (lampa_width + 1))
lampa_y = random.randint( 1, SCREEN_HEIGHT - (lampa_height + 1))


target_img = pygame.image.load("img/target.png")
target_width = 80
target_height =105
target_x = random.randint( 1, SCREEN_WIDTH - (target_width + 1))
target_y = random.randint( 1, SCREEN_HEIGHT - (target_height + 1))


dzin_speed_x = random.choice([-1, 1])
dzin_speed_y = random.choice([-1, 1])


lampa_speed_x = random.choice([-1.5, 1.5])
lampa_speed_y = random.choice([-1.5, 1.5])

avto_speed_x = random.choice([-0.5, 0.5])
avto_speed_y = random.choice([-0.5, 0.5])



# Скорость и направление движения цели
target_speed_x = random.choice([-0.5, 0.5])
target_speed_y = random.choice([-0.5, 0.5])



color = (random.randint (0, 255), random.randint (0, 255), random.randint(0, 255))

running = True
Schet = 0
mirrored = False  # Переменная для отслеживания зеркального состояния мишени


while  running:
    screen.fill(color)
    font = pygame.font.SysFont('Times New Roman', 50)
    text = font.render("Yes, накликали:  ", True, 'WHITE')
    font = pygame.font.SysFont('Times New Roman', 250)
    text2 = font.render(str(Schet), True, 'WHITE')
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                mirrored = not mirrored  # Переключаем зеркальное отображение
                target_x = random.randint(0, SCREEN_WIDTH - (target_width))
                target_y = random.randint(0, SCREEN_HEIGHT - (target_height))
                target_speed_x = random.choice([-2, 2])
                target_speed_y = random.choice([-2, 2])
                Schet += 1

    # Обновляем положение цели
    target_x += target_speed_x
    target_y += target_speed_y

    avto_x += avto_speed_x
    avto_y += avto_speed_y


    lampa_x += lampa_speed_x
    lampa_y += lampa_speed_y

    dzin_x += dzin_speed_x
    dzin_y += dzin_speed_y


    # Проверяем, не вышла ли цель за пределы экрана
    if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    if avto_x < 0 or avto_x > SCREEN_WIDTH - avto_width:
        avto_speed_x = -avto_speed_x
    if avto_y < 0 or avto_y > SCREEN_HEIGHT - avto_height:
        avto_speed_y = -avto_speed_y


    if lampa_x < 0 or lampa_x > SCREEN_WIDTH - lampa_width:
        lampa_speed_x = -lampa_speed_x
    if lampa_y < 0 or lampa_y > SCREEN_HEIGHT - lampa_height:
        lampa_speed_y = -lampa_speed_y

    if dzin_x < 0 or dzin_x > SCREEN_WIDTH - dzin_width:
            dzin_speed_x = -dzin_speed_x
    if dzin_y < 0 or dzin_y > SCREEN_HEIGHT - dzin_height:
            dzin_speed_y = -dzin_speed_y


     # Проверяем состояние зеркальности и отображаем мишень
    if mirrored:
            mirrored_img = pygame.transform.flip(target_img, True, False)
            screen.blit(mirrored_img, (target_x, target_y))
    else:
            screen.blit(target_img, (target_x, target_y))

    if mirrored:
        dom2_img = pygame.transform.flip(dom_img, True, False)
        screen.blit(dom2_img, (300, 200))
    else:
        screen.blit(dom_img, (300, 200))


    #screen.blit(target_img, (target_x, target_y))
    screen.blit(text, (10, 10))
    screen.blit(text2, (10,30))
   # screen.blit(dom_img, (dom_x, dom_y))
    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(grib_img, (grib_x, grib_y))
    screen.blit(kust_img, (kust_x, kust_y))
    screen.blit(avto_img, (avto_x, avto_y))
    screen.blit(lampa_img, (lampa_x, lampa_y))
    screen.blit(dzin_img, (dzin_x, dzin_y))


    pygame.display.update()


pygame.quit()