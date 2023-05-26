from OpenGL.GL import *
from PIL import Image
import pygame
import numpy as np

class Chao():
    def __init__(self):
        self.positions = None
        self.colors = None

    def carregar_padrao_quadriculado(self):
        size= 1
        rows = 100
        cols = 100
        self.positions = np.zeros((rows*cols*4,3), dtype=np.float32)
        self.colors = np.zeros((rows*cols*4,3), dtype=np.float32)

        for i in range(rows):
            for j in range(cols):                
                index = (i * cols + j) * 4

                x = -size * cols / 2 + j * size
                z = -size * rows / 2 + i * size

                self.positions[index] = [x, -5.0, z]
                self.positions[index+1] = [x, -5.0, z+size]
                self.positions[index+2] = [x+size, -5.0, z+size]
                self.positions[index+3] = [x+size, -5.0, z]

                if(i+j)%2 == 0:
                    for x in range (index, index+4):                
                        self.colors[x] = [1.0,1.0,1.0]
                else:
                    for x in range (index, index+4):
                        self.colors[x] = [0.0,0.0,0.0]



    def draw(self):
        #Aqui eu desenho o chão da aplicação  
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glVertexPointer(3, GL_FLOAT, 0 , self.positions)
        glColorPointer(3, GL_FLOAT, 0 , self.colors)

        glDrawArrays(GL_QUADS, 0, len(self.positions))

        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)
       
