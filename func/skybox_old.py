from OpenGL.GL import *
import pygame
from PIL import Image
from pygame.locals import *
import numpy as np

class Skybox:
    def __init__(self):
        self.textures = ['front.png', 'back.png', 'top.png', 'bottom.png', 'right.png', 'left.png']      
        self.vertices =  np.array([
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
            [-1, -1, -1], [-1, -1, 1], [-1, 1, 1], [-1, 1, -1]], dtype=np.float32)
        self.faces = [
            (0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15),(16,17,18,19),(20,21,22,23)
        ]
        self.skybox_list = self.create_skybox(30)

     
    def changeSize(self, size):
        np.multiply(self.vertices, size)
    
    def create_skybox(self, tamanho):
        texture_coordinates = [
            (0.0, 0.0),(0.0, 0.0),(0.0, 1.0),(1.0, 1.0)
        ]
        skybox_list = glGenLists(1)
        glNewList(skybox_list, GL_COMPILE)
        glPushMatrix()       
        glEnable(GL_TEXTURE_2D)
        self.changeSize(tamanho)
        for i, texture_file in enumerate(self.textures):
            texture = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texture)

            image = Image.open(".\\textures\\" + texture_file)
            image_data = np.array(image.convert("RGBA"))
            
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
            
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

            glBegin(GL_QUADS)
            for j in range(i*4, (i+1)*4):
                vertex = self.vertices[j]
                tex_coord = texture_coordinates[j % 4]
                glTexCoord2f(tex_coord[0], tex_coord[1])
                glVertex3f(vertex[0], vertex[1], vertex[2])
            glEnd()
        
        glPopMatrix()
        glEndList()
        return skybox_list
    

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glCallList(self.skybox_list)
        #glScalef(10, 10, 10)
        glDisable(GL_TEXTURE_2D)
