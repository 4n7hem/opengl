import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from lado import Cube
from cores import cuboSolucionavel
import logging

logging.basicConfig(level=logging.DEBUG) #talvez eu use isso depois

# Inicialize o cubo
cubo = np.empty((3, 3, 3), dtype=object).flatten()
cores = cuboSolucionavel()


#Crie os cubos já pré-definidos
i = 0
j = 0
k = 0
for unidade in cubo:
    cube_size = 0.3  # o tamanho do cubo
    valor = 9*k+3*i+j#magic number yaaay        
    
    novo_cubo = Cube(position=[i,j,k], colors=cores[valor])  #crie o cubo 
        
    novo_cubo.changeSize(size=cube_size) #defina o tamanho do cubo (em escala)    
    cubo[valor]= novo_cubo

    #iterador(usando isso em python, eu sinto que estou fazendo algo errado)
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

    glClearColor(1, 1, 1, 0) #fundo branco
    glEnable(GL_DEPTH_TEST) #isso faz com que não seja visível todos os lados de um cubo.
                            # caso seja comentado, alguns lados renderizarão o lado de dentro dos cubos por cima do de fora

    glDepthFunc(GL_LESS) #função de comparação de profundidade (estudar mais depois)

    glMatrixMode(GL_PROJECTION) # representação da lente da câmera
    gluPerspective(45, (display[0]/display[1]), 0.5, 40.0) #Perspectiva
   
    glMatrixMode(GL_MODELVIEW) # representação da câmera em si
    glTranslatef(0.0, 0.0, -5)    
    
    while True:               

        #Limpe sempre a tela
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 

        # Renderize a cada frame todos os cubos.       
        cube_spacing = 0.35  # Espaço entre os cubos
        for i in range(3):
            for j in range(3):
                for k in range(3): #Iterando entre os 27 cubos
                    # Cálculo da posição dos cubos (para que todos não ocupem o mesmo espaço)
                    x = (i - 1) * (cube_size + cube_spacing)
                    y = (j - 1) * (cube_size + cube_spacing)
                    z = (k - 1) * (cube_size + cube_spacing)
                    
                    # Desenhe o cubo na tela                   
                    cube = cubo[9*k+3*i+j]
                    cube.changePosition(position=[x,y,z])                    
                    cube.draw()
       
        # Troca de buffers e habilidade de fechar a janela                         
        pygame.display.flip()
        pygame.time.wait(10) #limitador da taxa de frames, para que o cubo só não gire na velocidade da luz 


        for event in pygame.event.get():
        #Controle do cubo com WASD 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    glRotatef(20, 1, 0, 0)  # Camera view
                if event.key == pygame.K_a:
                    glRotatef(20, 0, 0, 1) # Camera view
                if event.key == pygame.K_s:
                    glRotatef(20, -1, 0, 0) # Camera view
                if event.key == pygame.K_d:                    
                    glRotatef(20, 0, 0, -1)  # Camera view


            if event.type == pygame.QUIT:                
                pygame.quit()
                quit()

main()      

        

    
    


    


