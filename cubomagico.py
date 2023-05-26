import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
import numpy as np
from func.cubiculo import Cube
from func.cubo import Cubo
from func.chao import Chao
from func.camera import Camera
from auxiliar.cores import cuboSolucionavel
import logging

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
    
    sombra_vertex = open("./shaders/shadowMap_vertex.txt", "r").read()
    sombra_frag = open("./shaders/shadowMap_fragment.txt", "r").read()
    
    sombra = compileProgram( 
        compileShader(sombra_vertex , GL_VERTEX_SHADER),
        compileShader(sombra_frag , GL_FRAGMENT_SHADER))    

    glClearColor(.4, .7, 1, 0) #fundo azul
    glEnable(GL_DEPTH_TEST) #isso faz com que não seja visível todos os lados de um cubo.
                            # caso seja comentado, alguns lados renderizarão o lado de dentro dos cubos por cima do de fora

    #glDepthFunc(GL_LESS) #função de comparação de profundidade (estudar mais depois)

    pos_Luz = [0,3,0]
    
    #glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)  
    #glLightModeliv(GL_LIGHT_MODEL_TWO_SIDE, 1) 

    glMatrixMode(GL_PROJECTION) # representação da lente da câmera    
    gluPerspective(45, (display[0]/display[1]), 0.5, 40.0) #Perspectiva
   
    glMatrixMode(GL_MODELVIEW) # representação da câmera em si    
    glTranslatef(0.0, 0.0, -5)
    
    glEnable(GL_NORMALIZE) #Normalização das faces
    glShadeModel(GL_SMOOTH) #Smooth shading (sei o que faz não)

    #Inicialize o Cubo 
    rubik_cube = Cubo() 

    #A resposta estática do cubo padrão
    respost = resposta()
     

    #Inicialize o chão
    chao = Chao()
    chao.carregar_padrao_quadriculado()

    #Inicialize a camera
    camera = Camera()

    while True:

        #Rodar a camera conforme teclas são apertadas
        camera.checar_teclas_pressionadas(rubik_cube.cubo, respost)

        #Limpe sempre a tela
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


        #Ligue a luz e as cores de materiais
        glEnable(GL_LIGHTING)      
        glEnable(GL_COLOR_MATERIAL)

        #Esfera de debug
        sphere = gluNewQuadric() #Create new sphere
        glPushMatrix()
        glTranslatef(pos_Luz[0],pos_Luz[1],pos_Luz[2]) #Move to the place
        glColor4f(0.5, 0.2, 0.2, 1) #Put color
        gluSphere(sphere, 0.1, 20, 20) #Draw sphere
        glPopMatrix()

        # Renderize a cada frame todos os cubos.
        rubik_cube.desenharCubo()
        
        #Desenhe o chão        
        chao.draw()

        # Troca de buffers e habilidade de fechar a janela                         
        pygame.display.flip()
        pygame.time.wait(2) #limitador da taxa de frames, para que o cubo só não gire na velocidade da luz     
main()      

        