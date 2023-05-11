import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from lado import Cube
from cores import cuboSolucionavel
import logging

logging.basicConfig(level=logging.DEBUG)

# Inicialize o cubo
cubo = np.empty((3, 3, 3), dtype=object).flatten()
cores = cuboSolucionavel()


#Crie os cubos já pré-definidos
i = 0
j = 0
k = 0
for unidade in cubo:
    cube_size = 0.3  # size of each cube
    valor = 9*k+3*i+j#magic number yaaay    
    if valor <= len(cores)-1:
        novo_cubo = Cube(position=[i,j,k], colors=cores[valor])
    else:
        novo_cubo = Cube(position=[i,j,k], colors=[[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    novo_cubo.changeSize(size=cube_size)
    cubo[valor]= novo_cubo    
    if i == 2 and j == 2:
        k += 1
        i = 0
        j = 0
    elif j == 2:
        j = 0
        i += 1
    else:
        j += 1


def main():    
    pygame.init() #Inicialize a tela
    display = (1280,732) # Tamanho da janela
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #Use o OpenGL
    pygame.display.set_caption('Rubiks Cube')

    glClearColor(1, 1, 1, 0)
    glEnable(GL_DEPTH_TEST)
    #glDepthFunc(GL_LESS)

    glMatrixMode(GL_PROJECTION)  
    gluPerspective(45, (display[0]/display[1]), 0.5, 40.0) #Perspectiva
   
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5) 

    
    
    while True:               

        #Limpe sempre a tela
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 

        # Draw the cubes and other game objects
        
        cube_spacing = 0.4  # spacing between cubes
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    # Calculate the position of the current cube
                    x = (i - 1) * (cube_size + cube_spacing)
                    y = (j - 1) * (cube_size + cube_spacing)
                    z = (k - 1) * (cube_size + cube_spacing)
                    
                    # Draw the faces of the current cube                    
                    cube = cubo[9*k+3*i+j]
                    cube.changePosition(position=[x,y,z])                    
                    cube.draw()  
        for event in pygame.mouse.get_pressed(3):
            if event:
                if abs(prev_pos_x - pygame.mouse.get_pos()[0]) == 0:
                    glRotatef(10, 1, 0, 0)  # Camera view
                elif abs(prev_pos_y - pygame.mouse.get_pos()[1]) == 0:
                    glRotatef(10, 0, 1, 0)  # Camera view
                elif abs(prev_pos_y - pygame.mouse.get_pos()[1]) > 1 and abs(
                        prev_pos_x - pygame.mouse.get_pos()[0]) > 1:
                    glRotatef(10, 1, 1, 0)  # Camera view
            prev_pos_x = pygame.mouse.get_pos()[0]
            prev_pos_y = pygame.mouse.get_pos()[1]
        #glRotatef(1, 3, 2, 1)
        # Swap buffers and handle Pygame events                           
        pygame.display.flip()
        pygame.time.wait(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

main()      

        

    
    


    


