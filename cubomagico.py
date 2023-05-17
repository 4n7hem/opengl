import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
import numpy as np
from func.cubiculo import Cube
from auxiliar.cores import cuboSolucionavel
import logging
from func.rotacoes import *
from auxiliar.solucionar import resposta

logging.basicConfig(level=logging.DEBUG) #talvez eu use isso depois
  
def main():         
    pygame.init() #Inicialize a tela    
    display = (800,600) # Tamanho da janela
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #Use o OpenGL
    pygame.display.set_caption('Rubiks Cube')

    vertex_shader = open("./shaders/vertex_shader.txt", "r").read()
    fragment_shader = open("./shaders/fragment_shader.txt", "r").read()

    program = compileProgram( 
        compileShader(vertex_shader, GL_VERTEX_SHADER),
        compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    glClearColor(1, 1, 1, 0) #fundo branco
    glEnable(GL_DEPTH_TEST) #isso faz com que não seja visível todos os lados de um cubo.
                            # caso seja comentado, alguns lados renderizarão o lado de dentro dos cubos por cima do de fora

    glDepthFunc(GL_LESS) #função de comparação de profundidade (estudar mais depois)

    glMatrixMode(GL_PROJECTION) # representação da lente da câmera
    gluPerspective(45, (display[0]/display[1]), 0.5, 40.0) #Perspectiva
   
    glMatrixMode(GL_MODELVIEW) # representação da câmera em si
    glTranslatef(0.0, 0.0, -5)

    glLightfv(GL_LIGHT0, GL_POSITION, (0,10,0,0)) #Posição da luz
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1,1,1,1)) #Cor da luz
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.7, 0.7, 0.7, 0.7])
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)    

    glEnable(GL_NORMALIZE) #Normalização das faces
    glShadeModel(GL_SMOOTH) #Smooth shading (sei o que faz não)

    # Inicialize o cubo
    cubo = np.empty((3, 3, 3), dtype=object)
    cores = cuboSolucionavel()
    cube_size = 0.3  # o tamanho do cubo

    #Crie os cubos já pré-definidos
    for i in range(3):
        for j in range(3):
            for k in range(3):
                novo_cubo = Cube(position=[i,j,k], colors=cores[9*k+3*i+j], program=program)  #crie o cubo 
                novo_cubo.changeSize(size=cube_size) #defina o tamanho do cubo (em escala)
                cubo[i][j][k] = novo_cubo      

    #Inicialize a posição dos cubos
    cube_spacing = 0.33  # Espaço entre os cubos
    for i in range(3):
        for j in range(3):
            for k in range(3): #Iterando entre os 27 cubos
                # Cálculo da posição dos cubos (para que todos não ocupem o mesmo espaço)
                x = (i - 1) * (cube_size + cube_spacing)
                y = (j - 1) * (cube_size + cube_spacing)
                z = (k - 1) * (cube_size + cube_spacing)
                    
                # Troque as coordenadas do cubo                   
                cube = cubo[i][j][k]
                cube.changePosition(position=[x,y,z])   

    respost = resposta()
    indice = 0 
    
    while True:               

        #Limpe sempre a tela
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glUseProgram(program)         
        
        #Aqui eu desenho o chão da aplicação
        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)  # Set floor color
        glVertex3f(-999.0, -5.0, -999.0)  # Define floor vertices
        glVertex3f(-999.0, -5.0, 999.0)
        glVertex3f(999.0, -5.0, 999.0)
        glVertex3f(999.0, -5.0, -999.0)
        glEnd()


        # Renderize a cada frame todos os cubos.
        for i in range(3):
            for j in range(3):
                for k in range(3): #Iterando entre os 27 cubos
                    cube = cubo[k][i][j]  
                    cube.configure_material()                                
                    cube.draw()
       
        # Troca de buffers e habilidade de fechar a janela                         
        pygame.display.flip()
        pygame.time.wait(2) #limitador da taxa de frames, para que o cubo só não gire na velocidade da luz     
        

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
                    nov_cubo = respost[1][indice](cubo, reverse=respost[0][indice])
                    cubo = nov_cubo
                    indice += 1
                   
            if event.type == pygame.QUIT:                
                pygame.quit()
                quit()

main()      

        