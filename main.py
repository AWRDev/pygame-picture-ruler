from math import dist
import pygame
import sys



def draw_line(screen, start, second):
    pygame.draw.line(screen, 
                     (250, 0, 0), 
                     start, 
                     second, 5)
    pygame.draw.circle(screen, (0, 255, 255), 
                   start, 5, 3)
    pygame.draw.circle(screen, (0, 255, 0), 
                   second, 5, 5)

# Инициализация Pygame
pygame.init()

# Создание окна размером 640x480
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
img = pygame.image.load('test.jpg')

first_point = None
second_point = None
active_point = None
active_point_index = None

selected_point = None

first_point_value = 0
second_point_value = 0

lines = []

# Главный цикл программы
while True:
    for event in pygame.event.get():
        screen.fill((0,0,0))   
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            # print(event.pos)
            if(active_point != None):
                print(active_point)
            screen.set_at(event.pos, (0, 0, 255))
            active_point = None
            try:
                # print(lines[0][1][0]-lines[0][0][0])
                # print((lines[0][1][0]-lines[0][0][0])/(second_point_value-first_point_value))
                kef = (lines[0][1][1]-lines[0][0][1])/(second_point_value-first_point_value)
                print((event.pos[1]-lines[0][0][1])/(kef)+first_point_value)
            except:
                pass
            # print(lines)
            for i in range(len(lines)):
                for j in range(2):
                    # print(f"{i=},{j=}(dist(event.pos, lines[i][j]))")
                    if(dist(event.pos, lines[i][j])<10):
                        active_point = lines[i][j]
                        active_point_index = i

            if(first_point != None):
                draw_line(screen, first_point, event.pos)
            
            if(selected_point != None):
                # del lines[active_point_index]
                draw_line(screen, lines[active_point_index][0], event.pos)

                

        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected_point != None:
                draw_line(screen, lines[active_point_index][0], event.pos)
                lines.append((lines[active_point_index][0], event.pos, False))
                del lines[active_point_index]
                active_point = None
                selected_point = None
            elif active_point != None:
                selected_point = active_point
                lines[active_point_index] = (lines[active_point_index][0], 
                                             lines[active_point_index][1], 
                                             True)
                
            else:
                if (first_point == None):
                    first_point = event.pos
                    first_point_value = int(input())
                else:
                    second_point = event.pos
                    second_point_value = int(input())
                    draw_line(screen, first_point, second_point)
                    lines.append((first_point, second_point, False))
                    first_point = None
                    second_point = None
    
    screen.blit(img,(0,0))
    for line in lines:
        if(line[2] == False):
            draw_line(screen, line[0], line[1])
    pygame.display.update()
