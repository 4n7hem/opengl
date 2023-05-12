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
    frente = [0,1,2,3]
    tras = [4,5,6,7]
    emcima = [8,9,10,11]
    embaixo = [12,13,14,15]
    direita = [16,17,18,19]
    esquerda = [20,21,22,23]
    match cubo.sentido:
        case 'forward': #Caso o movimento seja normal
            match cubo.eixo:        
                case 'x':
                    #Gire todos os vertices no eixo X antihorário:
                    cubo.vertices[[frente, embaixo, tras, emcima]] = cubo.vertices[[embaixo, tras, emcima, frente]]
                case 'y':
                    #Gire todos os vertices no eixo Y antihorário:
                    cubo.vertices[[frente, direita, tras, esquerda]] = cubo.vertices[[direita, tras, esquerda, frente]]                    
                case 'z':
                    pass
                    #Gire todos os vertices no eixo Z antihorário
                    cubo.vertices[[esquerda, emcima, direita, embaixo]] = cubo.vertices[[embaixo, esquerda, emcima, direita]]
                    
        case 'reverse': #Caso o movimento seja reverso
            match cubo.eixo:        
                case 'x':
                    #Gire todos os vertices no eixo X horário:
                    cubo.vertices[[frente, embaixo, tras, emcima]] = cubo.vertices[[emcima, frente, embaixo, tras]]
                case 'y':
                    #Gire todos os vertices no eixo Y horário
                    cubo.vertices[[frente, direita, tras, esquerda]] = cubo.vertices[[esquerda, tras, direita, frente]]
                    #trocar os vértices
                case 'z':
                    #Gire todos os vertices no eixo Z horário                    
                    cubo.vertices[[esquerda, emcima, direita, embaixo]] = cubo.vertices[[emcima, direita, embaixo, esquerda]]

    