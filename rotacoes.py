import numpy as np
import pygame
from rodarMatriz import *
clock = pygame.time.Clock()

#A ideia é o seguinte:
# Seleciono todos os cubos do bloco escolhido
# Eu sei que a posição o qual eles devem girar entorno é (0,0,0), ou o cubo central
# Faça uma função que gire eles na direção desejada.
# Precisa ser uma rotação animada bonitinha, para dar nota
# Após isso, troque os blocos no objeto do cubo para representar sua posição atual

def mov_R(cubo, reverse=False):
    #Selecione todos os cubos relevantes ao movimento    
    R_sides = cubo[:, 2, :]
    #O bloco do meio
    bloco_meio = [0,0,0]    

    for linha in R_sides:        
        for bloco in linha:
            bloco.setEixo('x')
            bloco.setAngulo(10)
            bloco.setPivo(bloco_meio)
            #Casos para caso o movimento seja horário ou antihorário
            if reverse:
                bloco.setSentido('reverse')
            else:
                bloco.setSentido('forward')
            bloco.girar()
    #após isso, substitua as posições dos blocos no cubo, para manter ordem de referencia
            #if reverse:
                #rodarClockwise(R_sides)
            #else:
                #rodarCCW(R_sides)

def mov_L(cubo, reverse=False):
    L_sides = cubo[:, 0, :]

    bloco_meio = [0,0,0]

    for linha in L_sides:        
        for bloco in linha:
            bloco.setEixo('x')
            bloco.setAngulo(10)
            bloco.setPivo(bloco_meio)
            if reverse:
                bloco.setSentido('reverse')
            else:
                bloco.setSentido('forward')
            bloco.girar()


def mov_M(cubo, reverse=False):   
    M_side = cubo[:, :, 2]

#============================================

def mov_F(cubo, reverse=False):
    F_sides = cubo[2, :, :]
    #O bloco do meio
    bloco_meio = [0,0,0]    

    for linha in F_sides:        
        for bloco in linha:
            bloco.setEixo('z')
            bloco.setAngulo(10)
            bloco.setPivo(bloco_meio)
            #Casos para caso o movimento seja horário ou antihorário
            if reverse:
                bloco.setSentido('reverse')
            else:
                bloco.setSentido('forward')
            bloco.girar()
    

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




