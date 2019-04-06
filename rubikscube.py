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
clock = pygame.time.Clock()
draw_rubikscube(surface,cube_radius,phi,-theta,[250,250],size,cube,lines)
pygame.display.flip()

last_move = 'f'
run = True
while run:
    clock.tick(0.5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    move = input()
    if not(move in ['r','l','u','d','f','b']):
        move = last_move
    if move == 'r':
        right(cube,0,size)
    if move == 'l':
        left(cube,0,size)
    if move == 'u':
        up(cube,0,size)
    if move == 'd':
        down(cube,0,size)
    if move == 'f':
        front(cube,0,size)
    if move == 'b':
        back(cube,0,size)
    draw_rubikscube(surface,cube_radius,phi,-theta,[250,250],size,cube,lines)
    pygame.display.flip()
    last_move = move
    move = ''
pygame.quit()
