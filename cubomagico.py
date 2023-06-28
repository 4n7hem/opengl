import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
import numpy as np
from func.cubiculo import Cube
from func.cubo import Cubo
from func.chao import Chao
from func.background import Background
from func.camera import Camera
from func.luz import Luz
from auxiliar.cores import cuboSolucionavel
import logging

from auxiliar.solucionar import resposta


logging.basicConfig(level=logging.DEBUG) #talvez eu use isso depois
  
def main():         
    pygame.init() #Inicialize a tela    
    display = (800,600) # Tamanho da janela
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #Use o OpenGL
    pygame.display.set_caption('Rubiks Cube')

    #vertex_shader = open("./shaders/vertex_shader.txt", "r").read()
    #fragment_shader = open("./shaders/fragment_shader.txt", "r").read()

    #program = compileProgram( 
    #    compileShader(vertex_shader, GL_VERTEX_SHADER),
    #    compileShader(fragment_shader, GL_FRAGMENT_SHADER))   
    

    glClearColor(.4, .7, 1, 0) #fundo azul
    glEnable(GL_DEPTH_TEST) #isso faz com que não seja visível todos os lados de um cubo.
                            # caso seja comentado, alguns lados renderizarão o lado de dentro dos cubos por cima do de fora
    # Enable texturing
    glEnable(GL_TEXTURE_2D)
  
    glMatrixMode(GL_PROJECTION) # representação da lente da câmera    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) #Perspectiva
   
    glMatrixMode(GL_MODELVIEW) # representação da câmera em si    
    glTranslatef(0.0, 0.0, -5)

    # Set up the viewport
    #glViewport(0, 0, display[0], display[1])

    #Inicialize o Cubo 
    rubik_cube = Cubo() 

    #A resposta estática do cubo padrão
    respost = resposta()     

    #Inicialize o chão
    chao = Chao()
    chao.carregar_padrao_quadriculado()

    #Inicialize a camera
    camera = Camera()

    #Inicialização da luz
    pos_Luz = [1.0,1.0,1.0,1.0]
    luz = Luz(pos_Luz)
    
    luz.configurar_luz()

    #background = Background(".\\textures\\front.png")

    while True:

        #Limpe sempre a tela        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glEnable(GL_COLOR_MATERIAL)        
        

        #glEnable(GL_TEXTURE_GEN_S)
        #glEnable(GL_TEXTURE_GEN_T)
        #glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_REFLECTION_MAP)
        #glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_REFLECTION_MAP)

        #Rodar a camera conforme teclas são apertadas
        camera.checar_teclas_pressionadas(rubik_cube.cubo, respost)  

        #background.draw()      

        #Ligue a luz e as cores de materiais                        
               
        luz.ligar_luz()    

        # Renderize a cada frame todos os cubos.        
        rubik_cube.desenharCubo()        
        
        #Desenhe o chão                  
        chao.draw()
        
        #Só por desencargo de consciência
        luz.desligar_luz()

        # Troca de buffers                      
        pygame.display.flip()
        pygame.time.wait(2) #limitador da taxa de frames, para que o cubo só não gire na velocidade da luz     
main()      

        