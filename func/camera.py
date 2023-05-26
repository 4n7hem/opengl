import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from func.rotacoes import *

class Camera():

    def __init__(self):        
        self.indice = 0

    def checar_teclas_pressionadas(self, cubo, respost):
        for event in pygame.event.get():
        #Controle do cubo com WASD 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_w:
                    glRotatef(15, 1, 0, 0)  # Gire para cima
                if event.key == pygame.K_a:
                    glRotatef(15, 0, 1, 0) # Gire para a direita
                if event.key == pygame.K_s:
                    glRotatef(15, -1, 0, 0) # Gire para baixo
                if event.key == pygame.K_d:                    
                    glRotatef(15, 0, -1, 0)  # Gire para a esquerda
            # Eles giram em relação ao cubo, e não a camera.
            #Keybind de movimentos para debug
                if event.key == pygame.K_0:
                    nov_cubo = mov_R(cubo)
                    cubo = nov_cubo
                if event.key == pygame.K_9:
                    nov_cubo = mov_L(cubo)
                    cubo = nov_cubo
                if event.key == pygame.K_8:
                    nov_cubo = mov_F(cubo)
                    cubo = nov_cubo
                if event.key == pygame.K_7:
                    nov_cubo = mov_B(cubo)
                    cubo = nov_cubo
                if event.key == pygame.K_6:
                    nov_cubo = mov_D(cubo)
                    cubo = nov_cubo
                if event.key == pygame.K_5:
                    nov_cubo = mov_U(cubo)
                    cubo = nov_cubo
                if event.key == pygame.K_p:
                    nov_cubo = mov_F(cubo, reverse=True)                    
                    cubo = nov_cubo
                if event.key == pygame.K_o:
                    nov_cubo = mov_L(cubo, reverse=True)
                    cubo = nov_cubo
                if event.key == pygame.K_i:
                    nov_cubo = mov_D(cubo, reverse=True)
                    cubo = nov_cubo
                if event.key == pygame.K_1:
                    nov_cubo = respost[1][self.indice](cubo, reverse=respost[0][self.indice])
                    cubo = nov_cubo
                    self.indice += 1
                   
            if event.type == pygame.QUIT:                
                pygame.quit()
                quit()