from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import pygame
from pygame.locals import *
from random import randint
import math


def rodar(cubo, pivo, angulo, eixo):
    #a matriz para mexer o pivô para a origem
    trad_matriz = np.array([
        [1,0,0,-pivo[0]],
        [0,1,0,-pivo[1]],
        [0,0,1,-pivo[2]],
        [0,0,0,1]
    ])

    #a matriz de rotação, dependendo do eixo
    angulo = np.radians(angulo)
    match eixo:
        case 'x':
            rotacao = np.array([
                [1,0,0,0],
                [0,np.cos(angulo),-np.sin(angulo),0],
                [0,np.sin(angulo), np.cos(angulo),0],
                [0,0,0,1]
            ])
        case 'y':
            rotacao = np.array([
                [np.cos(angulo), 0, np.sin(angulo), 0],
                [0,1,0,0],
                [-np.sin(angulo),0, np.cos(angulo),0],
                [0,0,0,1]
            ])
        case 'z':
            rotacao = np.array([
                [np.cos(angulo), -np.sin(angulo),0,0],
                [np.sin(angulo), np.cos(angulo),0,0],
                [0,0,1,0],
                [0,0,0,1]
            ])
        
    # a matriz que leva o pivô de volta pro lugar certo
    trad_back = np.array([
        [1,0,0,pivo[0]],
        [0,1,0,pivo[1]],
        [0,0,1,pivo[2]],
        [0,0,0,1]
    ])

    #Isso ira girar os cubos ao redor do cubo pivô
    trans_mat = np.dot(np.dot(trad_matriz, rotacao), trad_back)
    cubo.changePosition(position=np.dot(trans_mat, np.hstack((cubo.getPosition(),1)))[:3])

def trocaVertices(cubo):
    frente = 0
    tras = 1
    emcima = 2
    embaixo = 3
    direita = 4
    esquerda = 5
    match cubo.sentido:
        case 'forward': #Caso o movimento seja normal
            match cubo.eixo:        
                case 'x':
                    #Gire todos os colors no eixo X antihorário:
                    cubo.colors[[embaixo, tras, emcima, frente]] = cubo.colors[[frente, embaixo, tras, emcima]] 
                case 'y':
                    #Gire todos os colors no eixo Y antihorário:
                    cubo.colors[[direita, tras, esquerda, frente]] = cubo.colors[[frente, direita, tras, esquerda]]                     
                case 'z':
                    pass
                    #Gire todos os colors no eixo Z antihorário
                    cubo.colors[[embaixo, esquerda, emcima, direita]] = cubo.colors[[esquerda, emcima, direita, embaixo]]
                    
        case 'reverse': #Caso o movimento seja reverso
            match cubo.eixo:        
                case 'x':
                    #Gire todos os colors no eixo X horário:
                    cubo.colors[[emcima, frente, embaixo, tras]] = cubo.colors[[frente, embaixo, tras, emcima]]
                case 'y':
                    #Gire todos os colors no eixo Y horário
                    cubo.colors[[esquerda, tras, direita, frente]] = cubo.colors[[frente, direita, tras, esquerda]]
                    #trocar os vértices
                case 'z':
                    #Gire todos os colors no eixo Z horário                    
                    cubo.colors[[emcima, direita, embaixo, esquerda]]= cubo.colors[[esquerda, emcima, direita, embaixo]] 

    