from math import sin, cos, pi
import pygame

def scalar_product(vec0,vec1):
    value = 0
    for i in range(3):
        value += vec0[i]*vec1[i]
    return(value)

def scalar_vector_mult(num,vec):
    result = []
    for i in range(len(vec)):
        result += [num*vec[i]]
    return(result)

def vector_addition(vec0,vec1):
    return([vec0[i] + vec1[i] for i in range(len(vec0))])

def projetion(plane_base1,plane_base2,vec):
    return([scalar_product(vec,plane_base1),scalar_product(vec,plane_base2)])

def visible_verticies(verticies,normvec):
    prods = [scalar_product(vertex,normvec) for vertex in verticies]
    minimum = min(prods)
    return([vertex for vertex in verticies if scalar_product(vertex,normvec) > minimum])

def initialise(phi,theta,r):
    normal_vector = [cos(phi)*cos(theta),sin(phi)*cos(theta),sin(theta)]
    basis1 = [-sin(phi),cos(phi),0]
    basis2 = [-cos(phi)*sin(theta),-sin(phi)*sin(theta),cos(theta)]
    verticies = [[-r,-r,-r],[r,-r,-r],[-r,r,-r],[-r,-r,r],[r,r,-r],[r,-r,r],[-r,r,r],[r,r,r]]
    return([normal_vector,basis1,basis2,verticies])

def draw_line(surface,color,start,end,normal_vector,plane_basis_1,plane_basis_2,shift):
    p_start = projetion(plane_basis_1,plane_basis_2,start)
    p_end = projetion(plane_basis_1,plane_basis_2,end)
    pygame.draw.line(surface,color,vector_addition(p_start,shift),vector_addition(p_end,shift))

def draw_polygon(surface,color,vertex1,vertex2,vertex3,vertex4,normal_vector,plane_basis_1,plane_basis_2,shift):
    p_vertex1 = projetion(plane_basis_1,plane_basis_2,vertex1)
    p_vertex2 = projetion(plane_basis_1,plane_basis_2,vertex2)
    p_vertex3 = projetion(plane_basis_1,plane_basis_2,vertex3)
    p_vertex4 = projetion(plane_basis_1,plane_basis_2,vertex4)
    pygame.draw.polygon(surface,color, [vector_addition(p_vertex1,shift),vector_addition(p_vertex2,shift),vector_addition(p_vertex3,shift),vector_addition(p_vertex4,shift)])

def flat_Cube(surface,cube,x,y):
    x_start = 0.1*x
    y_start = 0.1*y
    cube_x_length = 0.8*x/3
    cube_y_length = 0.2*x
    for i in range(3):
        for j in range(3):
            #left
            pygame.draw.rect(surface,cube[4][j][i],(int(x_start + i*cube_x_length/3),int(y_start + cube_y_length + j*cube_y_length/3) ,int(cube_x_length/3) , int(cube_y_length/3)))
            #top
            pygame.draw.rect(surface,cube[0][j][i],(int(x_start + cube_x_length + i*cube_x_length/3),int(y_start + j*cube_y_length/3),int(cube_x_length/3), int(cube_y_length/3)))
            #front
            pygame.draw.rect(surface,cube[2][j][i],(int(x_start + cube_x_length + i*cube_x_length/3),int(y_start + cube_y_length + j*cube_y_length/3),int(cube_x_length/3), int(cube_y_length/3)))
            #bottom
            pygame.draw.rect(surface,cube[5][j][i],(int(x_start + cube_x_length + i*cube_x_length/3),int(y_start + 2*cube_y_length + j*cube_y_length/3),int(cube_x_length/3), int(cube_y_length/3)))
            #back
            pygame.draw.rect(surface,cube[3][j][i],(int(x_start + cube_x_length + i*cube_x_length/3),int(y_start + 3*cube_y_length + j*cube_y_length/3),int(cube_x_length/3), int(cube_y_length/3)))
            #rigth
            pygame.draw.rect(surface,cube[1][j][i],(int(x_start + 2*cube_x_length + i*cube_x_length/3),int(y_start + cube_y_length + j*cube_y_length/3) ,int(cube_x_length/3) , int(cube_y_length/3)))

def draw_rubikscube(surface,radius,phi,theta,shift,size,cube,lines):
    #lines is true or flase
    values = initialise(phi,theta,radius)
    verticies = values[3]
    plane_basis_1 = values[1]
    plane_basis_2 = values[2]
    normal_vector = values[0]
    v_verticies = visible_verticies(verticies,normal_vector)
    r = radius
    front = [[r,-r,-r],[r,r,-r],[r,r,r],[r,-r,r]]
    back = [[-r,-r,r],[-r,r,r],[-r,r,-r],[-r,-r,-r]]
    right = [[r,r,-r],[-r,r,-r],[-r,r,r],[r,r,r]]
    left = [[-r,-r,-r],[r,-r,-r],[r,-r,r],[-r,-r,r]]
    bottom = [[r,-r,r],[r,r,r],[-r,r,r],[-r,-r,r]]
    top = [[-r,-r,-r],[-r,r,-r],[r,r,-r],[r,-r,-r]]
    planes = [top,right,front,back,left,bottom]
    for k in range(6):
        plane = planes[k]
        if plane[0] in v_verticies and plane[1] in v_verticies and plane[2] in v_verticies and plane[3] in v_verticies:
            dif1 = vector_addition(plane[1],scalar_vector_mult(-1,plane[0]))
            dif2 = vector_addition(plane[3],scalar_vector_mult(-1,plane[0]))
            for i in range(size):
                for j in range(size):
                    point1 = vector_addition(plane[0],vector_addition(scalar_vector_mult(j/size,dif1),scalar_vector_mult(i/size,dif2)))
                    point2 = vector_addition(plane[0],vector_addition(scalar_vector_mult((j+1)/size,dif1),scalar_vector_mult(i/size,dif2)))
                    point3 = vector_addition(plane[0],vector_addition(scalar_vector_mult((j+1)/size,dif1),scalar_vector_mult((i+1)/size,dif2)))
                    point4 = vector_addition(plane[0],vector_addition(scalar_vector_mult(j/size,dif1),scalar_vector_mult((i+1)/size,dif2)))
                    draw_polygon(surface,cube[k][i][j],point1,point2,point3,point4,normal_vector,plane_basis_1,plane_basis_2,shift)
                    if lines:
                        draw_line(surface,(0,0,0),point1,point2,normal_vector,plane_basis_1,plane_basis_2,shift)
                        draw_line(surface,(0,0,0),point3,point4,normal_vector,plane_basis_1,plane_basis_2,shift)
                        draw_line(surface,(0,0,0),point1,point4,normal_vector,plane_basis_1,plane_basis_2,shift)
                        draw_line(surface,(0,0,0),point2,point3,normal_vector,plane_basis_1,plane_basis_2,shift)
