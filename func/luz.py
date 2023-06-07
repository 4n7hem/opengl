from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *


class Luz():

    def __init__(self, pos):
        self.pos_Luz = pos

    def configurar_luz(self):
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        #glLightModeliv(GL_LIGHT_MODEL_TWO_SIDE, 1)

        glLightfv(GL_LIGHT1, GL_POSITION, self.pos_Luz ) #Posição da luz
        glLightfv(GL_LIGHT1, GL_AMBIENT, (0.2, 0.2, 0.2)) # Luz ambiente
        glLightfv(GL_LIGHT1, GL_DIFFUSE, (0.8,0.8,0.8)) #Luz difusa 

        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1,1,1))
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128)

        pass

    def ligar_luz(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT1)
    
    def desligar_luz(self):
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT1)