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
# Eu vou comentar somente o mov_R, mas todos os outros movimentos seguirão a exata mesma lógica

def mov_R(cubo, reverse=False):
    #Selecione todos os cubos relevantes ao movimento    
    R_sides = cubo[2, :, :]
    #O bloco do meio
    bloco_meio = [0,0,0] 
    for linha in R_sides:        
        for bloco in linha:
            bloco.setEixo('x')
            bloco.setAngulo(10)
            bloco.setPivo(bloco_meio)
            #Casos para caso o movimento seja horário ou antihorário
            if not reverse:
                bloco.setSentido('reverse')
            else:
                bloco.setSentido('forward')
            bloco.girar()
    #após isso, substitua as posições dos blocos no cubo, para manter ordem de referencia
    if not reverse:
        slice_nova = rodarCCWreverso(R_sides)
    else:
        slice_nova = rodarClockwise(R_sides)
    cubo[2, :, :] = slice_nova
    return cubo

def mov_L(cubo, reverse=False):
    L_sides = cubo[0, :, :]

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
    #após isso, substitua as posições dos blocos no cubo, para manter ordem de referencia
    # IMPORTANTE: O SENTIDO DA ROTAÇÃO INVERTE EM LADOS OPOSTOS
    if reverse:
        slice_nova = rodarClockwisereverso(L_sides)
    else:
        slice_nova = rodarCCW(L_sides)
    cubo[0, :, :] = slice_nova
    return cubo

def mov_M(cubo, reverse=False):   
    M_side = cubo[1, :, :]

#============================================

def mov_F(cubo, reverse=False):
    F_sides = cubo[:, :, 2]
    #O bloco do meio
    bloco_meio = [0,0,0]    

    for linha in F_sides:        
        for bloco in linha:
            bloco.setEixo('z')
            bloco.setAngulo(10)
            bloco.setPivo(bloco_meio)
            #Casos para caso o movimento seja horário ou antihorário
            if not reverse:
                bloco.setSentido('reverse')
            else:
                bloco.setSentido('forward')
            bloco.girar()
    #após isso, substitua as posições dos blocos no cubo, para manter ordem de referencia
    if not reverse:
        slice_nova = rodarClockwisereverso(F_sides)
    else:
        slice_nova = rodarCCW(F_sides)
    cubo[:, :, 2] = slice_nova
    return cubo
    
def mov_B(cubo, reverse=False):
    B_sides = cubo[:, :, 0]
    #O bloco do meio
    bloco_meio = [0,0,0]    

    for linha in B_sides:        
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
    #após isso, substitua as posições dos blocos no cubo, para manter ordem de referencia
    if reverse:
        slice_nova = rodarClockwisereverso(B_sides)
    else:
        slice_nova = rodarCCW(B_sides)
    cubo[:, :, 0] = slice_nova
    return cubo

def mov_S(cubo, reverse=False):   
    S_side = cubo[:, :, 1]

#============================================

def mov_D(cubo, reverse=False):
    D_sides = cubo[:, 0, :]
    #O bloco do meio
    bloco_meio = [0,0,0]   

    for linha in D_sides:        
        for bloco in linha:
            bloco.setEixo('y')
            bloco.setAngulo(10)
            bloco.setPivo(bloco_meio)
            #Casos para caso o movimento seja horário ou antihorário
            if reverse:
                bloco.setSentido('reverse')
            else:
                bloco.setSentido('forward')
            bloco.girar()
    #após isso, substitua as posições dos blocos no cubo, para manter ordem de referencia
    if reverse:
        slice_nova = rodarClockwisereverso(D_sides, caso_y=True)
    else:        
        slice_nova = rodarCCW(D_sides, caso_y=True)
    cubo[:, 0, :] = slice_nova
    return cubo

def mov_U(cubo, reverse=False):   
    U_sides = cubo[:, 2, :]
    
    #O bloco do meio
    bloco_meio = [0,0,0]    

    for linha in U_sides:        
        for bloco in linha:
            bloco.setEixo('y')
            bloco.setAngulo(10)
            bloco.setPivo(bloco_meio)
            #Casos para caso o movimento seja horário ou antihorário
            if not reverse:
                bloco.setSentido('reverse')
            else:
                bloco.setSentido('forward')
            bloco.girar()
    #após isso, substitua as posições dos blocos no cubo, para manter ordem de referencia
    if not reverse:
        slice_nova = rodarCCWreverso(U_sides, caso_y=True)
    else:
        slice_nova = rodarClockwise(U_sides, caso_y=True)
    cubo[:, 2, :] = slice_nova
    return cubo

def mov_E(cubo, reverse=False):   
    E_side = cubo[:, 1, :]




