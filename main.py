import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption

point1_pos = [100, 100]
point2_pos = [400, 300]

ball_size1 = 10
ball_size2 = 5
mouse_size = 5

font_point = pygame.font.SysFont(None, 20)

def draw_points():
    pygame.draw.circle(screen, white, point1_pos, ball_size2)
    pygame.draw.circle(screen, red, point2_pos, ball_size1)

def reposition_point2():
    point2_pos[0] = random.randint(ball_size1, width - ball_size1)
    point2_pos[1] = random.randint(ball_size1, height - ball_size1)

points = 0
font = pygame.font.Font('freesansbold.ttf', 16)
text = font.render('Points: ' + str(points), True, green, black)
textRect = text.get_rect()
textRect.center = (400, 10)

running = True
while running:
    screen.fill((black))
    screen.blit(text, textRect)

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        point1_pos[1] -= 1
    if keys[pygame.K_s]:
        point1_pos[1] += 1
    if keys[pygame.K_a]:
        point1_pos[0] -= 1
    if keys[pygame.K_d]:
        point1_pos[0] += 1

    draw_points()
    pygame.display.flip()

    distance = ((point1_pos[0] - point2_pos[0])**2 + (point1_pos[1] - point2_pos[1])**2)**0.5
    if distance < 2 * ball_size1:
        reposition_point2()
        points = points + 1
        text = font.render('Points: ' + str(points), True, green, black)

    distance_mouse = ((mouse_pos[0] - point1_pos[0])**2 + (mouse_pos[1] - point1_pos[1])**2)**0.5
    if distance_mouse < 2 * mouse_size:
        print('points:', points)
        print('Game Over')
        running = False

pygame.quit()