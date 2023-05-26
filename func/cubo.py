import numpy as np
from func.cubiculo import Cube
from auxiliar.cores import cuboSolucionavel

class Cubo:

    def __init__(self):

        # Inicialize o cubo
        self.cubo = np.empty((3, 3, 3), dtype=object)
        cores = cuboSolucionavel()
        cube_size = 0.3  # o tamanho do cubo
    
        #Crie os cubos já pré-definidos
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    novo_cubo = Cube(position=[i,j,k], colors=cores[9*k+3*i+j])  #crie o cubo 
                    novo_cubo.changeSize(size=cube_size) #defina o tamanho do cubo (em escala)
                    self.cubo[i][j][k] = novo_cubo      

        #Inicialize a posição dos cubos
        cube_spacing = 0.33  # Espaço entre os cubos
        for i in range(3):
            for j in range(3):
                for k in range(3): #Iterando entre os 27 cubos
                    # Cálculo da posição dos cubos (para que todos não ocupem o mesmo espaço)
                    x = (i - 1) * (cube_size + cube_spacing)
                    y = (j - 1) * (cube_size + cube_spacing)
                    z = (k - 1) * (cube_size + cube_spacing)
                        
                    # Troque as coordenadas do cubo                   
                    cube = self.cubo[i][j][k]
                    cube.changePosition(position=[x,y,z])
    
    def desenharCubo(self):
        for i in range(3):
            for j in range(3):
                for k in range(3): #Iterando entre os 27 cubos
                    cube = self.cubo[i][j][k]                                                    
                    cube.draw()