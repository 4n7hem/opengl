import numpy as np

def rodarClockwise(slice):
    temp = slice.copy()

    for i in range(3):
        for j in range(3):
            new_i = -j + 2
            new_j = i
            temp[new_i, new_j] = slice[i,j]
    slice[:] = temp

def rodarCCW(slice):
    #roda o negócio 3 vezes horário, o que vira antihorário
    #desculpa, eu sou burro, acontece
    temp = slice.copy()
    for nada in range(3):
        for i in range(3):
            for j in range(3):
                new_i = -j + 2
                new_j = i
                temp[new_i, new_j] = slice[i,j]
        slice[:] = temp