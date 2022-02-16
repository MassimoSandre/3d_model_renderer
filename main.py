import pygame
from pygame.locals import *
from object import Object

ROTATING_SPEED = 0.01

pygame.init()
size = width, height = 620, 540

black = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size, RESIZABLE)

clock = pygame.time.Clock()

myobj = Object("model.obj",100,(200,200,200))



running = True
rotating = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                myobj.set_pos([*event.pos,0])

            if event.button == 2: 
                rotating = not rotating

            
            
    screen.fill(black)


    myobj.render(screen)
    


    if rotating:
        myobj.rotate_x(ROTATING_SPEED)
        myobj.rotate_y(ROTATING_SPEED)
        myobj.rotate_z(ROTATING_SPEED)

       
    pygame.display.update()
    clock.tick(60)