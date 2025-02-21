#!/usr/bin/python

import numpy as np
from astropy.nddata import NDData

def alinear(x1,y1,x2,y2,dim_1_x,dim_1_y,dim_2_x,dim_2_y, actual): # 1: Referencia 2: Pos. de la imagen actual
    """
    desplaza el objeto de estudio a un punto de referencia comun

    args:
        - x1,y1,x2,y2: coordenadas antes-despues
        - dim_1_x,dim_1_y,dim_2_x,dim_2_y: dimensiones de la matriz, antes y antes-despues
        - actual: matriz de la imagen a alinear

    return:
        - matriz desplazada
        
    """

    actual = NDData(actual)
    diferencia_x = x1 - x2
    diferencia_y = y1 - y2

    matriz_final = np.zeros((dim_1_x,dim_1_y))
    matriz_final = NDData(matriz_final)

    for i in range(dim_2_x):
        for j in range(dim_2_y):
            x = i + diferencia_x
            y = j + diferencia_y

            if ( x > 0 and x < dim_1_x and y > 0 and y < dim_1_y):
                matriz_final.data[x][y] = actual.data[i][j]

    return matriz_final