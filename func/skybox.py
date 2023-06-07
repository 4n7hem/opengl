import pygame


class Skybox:
    def __init__(self):
        self.texture = self.get_texture_cube(dir_path = "..\\textures\\")
          

    def get_texture_cube(self, dir_path, ext='png'):

        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
       
        textures = []
        for face in faces:
            texture = pygame.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pygame.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pygame.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pygame.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube