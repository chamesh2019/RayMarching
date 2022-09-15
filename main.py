from random import choice, randint
import pygame, sys, math

from pyparsing import White
from ray import Ray

SIZE = 1280, 720
FRAME_RATE = 30
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
angle = 0
objects = []

RAY = Ray(screen, SIZE)

while True:
    clock.tick(FRAME_RATE)
    screen.fill(BLACK)
    
    RAY.march(objects, angle)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            radius = randint(10, 100)
            color = choice(COLORS)
            objects.append((mouse_position, radius, color))
            pygame.draw.circle(screen, color, mouse_position, radius)
            pygame.display.update()                   

    angle += 0.01
    pygame.display.update()            
    