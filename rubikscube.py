from darstellung import *
from moves import *
from time import sleep

lines = True
size = 3
cube_old = cube(size)
cube = cube(size)
x = 750
y = 750
cube_radius = 125
phi = pi/4
theta = pi/4


pygame.init()
surface = pygame.display.set_mode((750,750))
running = True
draw_rubikscube(surface,cube_radius,phi,-theta,[250,250],size,cube,lines)
pygame.display.flip()

##while running:
##    next_move = input()
##    if next_move == right:
##        rigth(cube,0)
##    if next_move == left:
##        left(cube,0)
##    if next_move == up:
##        up(cube,0)
##    if next_move == down:
##        down(cube,0)
##    if next_move == front:
##        front(cube,0)
##    if next_move == back:
##        back(cube,0)
##    draw_rubikscube(surface,cube_radius,phi,theta,[250,250],size,cube,lines)
##    pygame.display.flip()
