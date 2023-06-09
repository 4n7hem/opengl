import pygame
from func.skybox_old import Skybox
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from func.camera import Camera

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)

skybox = Skybox()
camera = Camera()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -5)


clock = pygame.time.Clock()

while True:       

    camera.checar_teclas_pressionadas(None, None)
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_REFLECTION_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_REFLECTION_MAP)

    glColor3f(1.0, 1.0, 1.0)
    #glutSolidCube(1.0)

    skybox.draw()

    pygame.display.flip()
    clock.tick(60)