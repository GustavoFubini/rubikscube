import pygame
from darstellung import *
from moves import *

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,128,0)
yellow = (255,255,0)
colors = [white,red,green,blue,orange,yellow]

def reverse(liste):
    list_n = []
    for i in range(len(liste)):
        list_n.append(liste[len(liste)-1-i])
    return(list_n)

def cube(size):
    cube = []
    #0 is top,5 is bottom,1 is rigth,4 is left,2 is front,3 is back
    for i in range(6):
        plane = []
        for j in range(size):
            row = []
            for k in range(size):
                row.append(colors[i])
            plane.append(row)
        cube.append(plane)
    return(cube)

def rotation_right(cube,plane_num,size):
    #only the plane rotated is being changed
    plane_new = [[0 for i  in range(size)] for j in range(size)]
    plane = cube[plane_num]
    for i in range(size):
        for j in range(size):
            plane_new[j][size-1-i] = plane[i][j]
    cube[plane_num] = plane_new

def right(cube,distance,size):
    if distance == 0:
        rotation_right(cube,1,size)
    for i in range(size):
        cube[0][i][size-1-distance],cube[2][i][size-1-distance],cube[5][i][size-1-distance],cube[3][i][size-1-distance] = cube[2][i][size-1-distance],cube[5][i][size-1-distance],cube[3][i][size-1-distance],cube[0][i][size-1-distance]

def left(cube,distance,size):
    if distance == 0:
        rotation_right(cube,4,size)
    for i in range(size):
        cube[0][i][distance],cube[2][i][distance],cube[5][i][distance],cube[3][i][distance] = cube[3][i][distance],cube[0][i][distance],cube[2][i][distance],cube[5][i][distance]

def front(cube,distance,size):
    if distance == 0:
        rotation_right(cube,2,size)
    for i in range(size):
        cube[0][size-1-distance][i],cube[1][i][distance],cube[5][distance][size-1-i],cube[4][size-1-i][size-1-distance] = cube[4][size-1-i][size-1-distance],cube[0][size-1-distance][i],cube[1][i][distance],cube[5][distance][size-1-i]
 
def back(cube,distance,size):
    if distance == 0:
        rotation_right(cube,3,size)
    for i in range(size):
        cube[0][distance][i],cube[1][i][size-1-distance],cube[5][size-1-distance][size-1-i],cube[4][size-1-i][distance] = cube[1][i][size-1-distance],cube[5][size-1-distance][size-1-i],cube[4][size-1-i][distance],cube[0][distance][i]

def up(cube,distance,size):
    if distance == 0:
        rotation_right(cube,0,size)
    cube[1][distance],cube[2][distance],cube[4][distance],cube[3][size-1-distance] = reverse(cube[3][size-1-distance]),cube[1][distance],cube[2][distance],reverse(cube[4][distance])

def down(cube,distance,size):
    if distance == 0:
        rotation_right(cube,5,size)
    cube[1][size-1-distance],cube[2][size-1-distance],cube[4][size-1-distance],cube[3][distance] = cube[2][size-1-distance],cube[4][size-1-distance],reverse(cube[3][distance]),reverse(cube[1][size-1-distance])
