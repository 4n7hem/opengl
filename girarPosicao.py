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

    trans_mat = np.dot(np.dot(trad_matriz, rotacao), trad_back)
    cubo.changePosition(position=np.dot(trans_mat, np.hstack((cubo.getPosition(),1)))[:3])
    #cubo.changeVertices(np.dot(trans_mat, np.hstack(cubo.getVertices(), np.ones(8,1), axis=1).T)[:3].T)