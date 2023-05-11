import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def draw_cube():
    glBegin(GL_QUADS)
    
    # Front face
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 0.0, 0.0]) # red
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100.0)    
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glNormal3f(0,  0,  -1)
    
    # Back face
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [0.0, 1.0, 0.0])  # green
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100.0)    
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glNormal3f(-1,  0,  0)
    
    # Top face
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [0.0, 0.0, 1.0])  # blue
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100.0)    
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glNormal3f(0,  0, 1)
    
    # Bottom face
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 1.0, 0.0]) # yellow
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100.0)    
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glNormal3f(1,  0,  0)
    
    # Right face
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 0.0, 1.0])# magenta
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100.0)     
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glNormal3f(0,  1,  0)
    
    # Left face
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [0.0, 1.0, 1.0])# cyan
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100.0)    
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glNormal3f(0, -1,  0)    
    
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    # Set up the camera
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)    

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5) 

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))
    glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0))


    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    inv = np.linalg.inv(viewMatrix)    
    #print(inv)

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )        
       
        glRotatef(1, 3, 2, 1)  
        draw_cube()

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        

        pygame.display.flip()
        pygame.time.wait(10)

# Call the main function
main()