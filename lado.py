from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from random import randint

class Cube:
    def __init__(self, position, colors):
        self.position = position
        self.colors = colors
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
    
    def changePosition(self, position):
        self.position = position
    
    def changeSize(self, size):
        self.vertices = np.multiply(self.vertices, size)
    
    def setColor(self, color):
        self.colors = color        

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glBegin(GL_QUADS)
        for i in range(6):
            glColor3f(*self.colors[i])
            for j in range(4):
                glVertex3f(*self.vertices[i*4+j])
        glEnd()
        glPopMatrix()
