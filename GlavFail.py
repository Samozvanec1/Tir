import random
import heapq
import pygame
pygame.init()
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
def astar(grid, start, goal):
    # Инициализация словарей для хранения стоимостей и предыдущих точек
    cost = {start: 0}
    came_from = {start: None}


    # Приоритетная очередь для хранения точек и их оценок (приоритетов)
    priority_queue = [(0, start)]


    while priority_queue:

        current_cost, current_point = heapq.heappop(priority_queue)

        # Если достигнута целевая точка, завершаем алгоритм
        if current_point == goal:
            break


    for neighbor in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = current_point[0] + neighbor[0], current_point[1] + neighbor[1]


    new_cost = cost[current_point] + 1 # Стоимость перемещения на одну ячейку




    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
        if (x, y) not in cost or new_cost < cost[(x, y)]:
            cost[(x, y)] = new_cost
            priority = new_cost + manhattan_distance((x, y), goal)  
                    # Оценка для приоритета
            heapq.heappush(priority_queue, (priority, (x, y)))
            came_from[(x, y)] = current_point
            path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()


    return path
def create_grid(SCREEN_HEIGHT, SCREEN_WIDTH):
    main_list = []
    append_list = []
    for i in range(SCREEN_HEIGHT):
        for i in range(SCREEN_WIDTH):
            append_list.append(0)
        main_list.append(append_list)
        append_list = []
    return main_list
        


SCREEN_WIDTH = 880
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
print(create_grid(SCREEN_HEIGHT, SCREEN_WIDTH))
grid = create_grid(SCREEN_HEIGHT, SCREEN_WIDTH)
for point in astar(grid, (30,50), (43,97)):
    print(point)
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
while  running:
    screen.fill(color)
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - (target_width))
                target_y = random.randint(0, SCREEN_HEIGHT - (target_height))
    screen.blit(target_img, (target_x, target_y))

    pygame.display.update()


pygame.quit()