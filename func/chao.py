from OpenGL.GL import *

class Chao():
    def __init__(self):
        pass


    def draw(self):
        #Aqui eu desenho o chão da aplicação
        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)  # Set floor color
        glVertex3f(-999.0, -5.0, -999.0)  # Define floor vertices
        glVertex3f(-999.0, -5.0, 999.0)
        glVertex3f(999.0, -5.0, 999.0)
        glVertex3f(999.0, -5.0, -999.0)
        glEnd()