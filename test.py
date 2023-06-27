import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from func.background import Background


# Initialize Pygame
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)

# Enable depth testing
glEnable(GL_DEPTH_TEST) 

# Set up the projection matrix
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, width / height, 0.1, 50.0)

# Set up the modelview matrix
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Enable texturing
glEnable(GL_TEXTURE_2D)

# Create a Background object
background1 = Background(".\\textures\\front.png", width, height)

# Set up lighting and material properties


glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
glEnable(GL_COLOR_MATERIAL)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glRotatef(1, 1, 0, 0)

    # Draw the background
    background1.draw()

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)

# Clean up
pygame.quit()