from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import pygame
from pygame.locals import *
from random import randint
import math
from girarPosicao import rodar

class Cube:
    def __init__(self, position, colors):
        self.position = position
        self.colors = colors
        self.girando = False
        self.eixo = None
        self.pivot = None
        self.adicional = 0
        self.angulo = 0        
        self.vertices = np.array([
            # Front face
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],
            # Back face
            [-1, -1, -1], [-1, 1, -1], [1, 1, -1], [1, -1, -1],
            # Top face
            [-1, 1, -1], [-1, 1, 1], [1, 1, 1], [1, 1, -1],
            # Bottom face
            [-1, -1, -1], [1, -1, -1], [1, -1, 1], [-1, -1, 1],
            # Right face
            [1, -1, -1], [1, 1, -1], [1, 1, 1], [1, -1, 1],
            # Left face
            [-1, -1, -1], [-1, -1, 1], [-1, 1, 1], [-1, 1, -1]
        ], dtype=np.float32)
    
    def getPosition(self):
        return self.position

    def changePosition(self, position):
        self.position = position
    
    def getVertices(self):
        return self.vertices
    
    def changeVertices(self, vertices):
        self.vertices = vertices

    def changeSize(self, size):
        self.vertices = np.multiply(self.vertices, size)
    
    def setColor(self, color):
        self.colors = color

    def setAngulo(self, angulus):
        self.adicional = angulus
    
    def setPivo(self, pivo):
        self.pivot = pivo
    
    def getAngulo(self):
        return self.angulo

    def setEixo(self, eixo):
        self.eixo = eixo
    
    def girar(self):
        self.girando = True

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        if self.girando:
            self.angulo = self.angulo + self.adicional
            match self.eixo:
                case 'x':
                    glRotate(self.angulo, 1, 0, 0)
                case 'y':
                    glRotate(self.angulo, 0, 1, 0)
                case 'z':
                    glRotate(self.angulo, 0, 0, 1)            
            rodar(self,self.pivot, self.adicional, self.eixo)            
            pygame.time.wait(10)
            if self.angulo >= 90:                
                self.girando = False
                self.angulo = 0
                self.adicional = 0 
                match self.eixo:
                    case 'x':
                        pass
                        #trocar os vértices
                    case 'y':
                        pass
                        #trocar os vértices
                    case 'z':
                        pass
                        #trocar os vértices      
        glBegin(GL_QUADS)
        for i in range(6):
            glColor3f(*self.colors[i])
            for j in range(4):
                glVertex3f(*self.vertices[i*4+j])
        glEnd()
        glPopMatrix()