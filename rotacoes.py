import numpy as np
import pygame
clock = pygame.time.Clock()

#A ideia é o seguinte:
# Seleciono todos os cubos do bloco escolhido
# Eu sei que a posição o qual eles devem girar entorno é (0,0,0), ou o cubo central
# Faça uma função que gire eles na direção desejada.
# Precisa ser uma rotação animada bonitinha, para dar nota

def mov_L(cubo, reverse=False):
    L_side = cubo[:, 0, :]

def mov_R(cubo, reverse=False):
    #Selecione todos os cubos relevantes ao movimento    
    R_sides = cubo[:, 2, :]
    #Encontre  o bloco do meio, guarde suas coordenadas    
    y = R_sides.shape[0] // 2
    z = 2
    bloco_meio = R_sides[y,z]
    #print(bloco_meio.getPosition())

    for linha in R_sides:        
        for bloco in linha:
            bloco.setEixo('x')
            bloco.setAngulo(10)
            bloco.setPivo([0,0,0])
            bloco.girar()

def mov_M(cubo, reverse=False):   
    M_side = cubo[:, :, 2]

#============================================

def mov_F(cubo, reverse=False):
    F_side = cubo[2, :, :]

def mov_B(cubo, reverse=False):
    B_side = cubo[0, :, :]

def mov_S(cubo, reverse=False):   
    S_side = cubo[1, :, :]

#============================================

def mov_D(cubo, reverse=False):
    D_side = cubo[:, :, 0]

def mov_U(cubo, reverse=False):   
    U_side = cubo[:, :, 2]

def mov_E(cubo, reverse=False):   
    E_side = cubo[:, :, 1]




