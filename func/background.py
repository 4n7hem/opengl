import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

class Background:
    def __init__(self, image_path):
        # Load the image
        image = Image.open(image_path)
        image_data = image.convert("RGBA").tobytes()
        image_width, image_height = image.size

        # Create a texture object
        self.texture = glGenTextures(1)

        # Bind the texture
        glBindTexture(GL_TEXTURE_2D, self.texture)

        # Set texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Set the texture image data
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

        # Set up the spot light parameters
        light_position = [0, 0, 1, 1]  # Last value set to 1 to indicate a spot light
        light_direction = [0, 0, -1]
        light_cutoff = 30.0  # Spot light cone angle in degrees
        light_exponent = 2.0  # Spot light intensity falloff
        light_attenuation = [0.2, 0.5, 0.7]  # Constant, linear, and quadratic attenuation

        # Enable spot light features
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, light_direction)
        glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, light_cutoff)
        glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, light_exponent)
        glLightfv(GL_LIGHT0, GL_CONSTANT_ATTENUATION, light_attenuation[0])
        glLightfv(GL_LIGHT0, GL_LINEAR_ATTENUATION, light_attenuation[1])
        glLightfv(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, light_attenuation[2])

        

    def draw(self):
        # Clear the screen and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)

        # Render the background quad
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 1)
        glVertex3f(-50, -50, -40)
        glTexCoord2f(1, 1)
        glVertex3f(50, -50, -40)
        glTexCoord2f(1, 0)
        glVertex3f(50, 50, -40)
        glTexCoord2f(0, 0)
        glVertex3f(-50, 50, -40)
        glEnd()

        # Enable lighting and color material
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
