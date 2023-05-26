from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *


class Luz():

    def __init__(self, pos):
        self.pos_Luz = pos

    def configurar_luz(self):
        glLightfv(GL_LIGHT0, GL_POSITION, self.pos_Luz ) #Posição da luz
        #glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8,0.8,0.8)) #Cor da luz
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2))
        #glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1,1,1))
        #glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128)

    def ligarLuz(self):
        glEnable(GL_LIGHT0)
    
    def desligarLuz(self):
        glDisable(GL_LIGHT0)