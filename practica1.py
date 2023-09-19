#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:38:38 2021

@author: chetevidaljustamante
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


Nx = int(input('Nx='))
Ny = int(input('Ny='))
Nz = int(input('Nz='))
tipo = input('Tipo de cristal:')
N = [Nx,Ny,Nz]

anchura = 1



def generaCristal(N,tipo):
    
    if tipo == 'fcc':

        nAt = int(4*N[0]*N[1]*N[2])
        cristal = np.empty((nAt,3))
        celdaBase = np.array([[0,0,0],[0,0.5,0.5],[0.5,0,0.5],[0.5,0.5,0]])
        iAt = 0 #indice del atomo
    
        for i in range(0,N[0]):
            for j in range(0,N[1]):
                for k in range(0,N[2]):
                    
                    '''ATOMO1'''
                    cristal[iAt,0]=celdaBase[0,0]+i # coordenadas x
                    cristal[iAt,1]=celdaBase[0,1]+j # coordenadas y
                    cristal[iAt,2]=celdaBase[0,2]+k # coordenadas z
                    '''ATOMO2'''
                    cristal[iAt+1,0]=celdaBase[1,0]+i # coordenadas x
                    cristal[iAt+1,1]=celdaBase[1,1]+j # coordenadas y
                    cristal[iAt+1,2]=celdaBase[1,2]+k # coordenadas z
                    '''ATOMO3'''
                    cristal[iAt+2,0]=celdaBase[2,0]+i # coordenadas x
                    cristal[iAt+2,1]=celdaBase[2,1]+j # coordenadas y
                    cristal[iAt+2,2]=celdaBase[2,2]+k # coordenadas z
                    '''ATOMO4'''
                    cristal[iAt+3,0]=celdaBase[3,0]+i # coordenadas x
                    cristal[iAt+3,1]=celdaBase[3,1]+j # coordenadas y
                    cristal[iAt+3,2]=celdaBase[3,2]+k # coordenadas z
                    iAt+=4
                    
        return cristal 
                    
    if tipo == 'b':
            
        celdaBase = np.array([0,0,0])
        nAt = int(4*N[0]*N[1]*N[2])
        cristal = np.empty((nAt,3))
        iAt = 0 #indice del atomo
            
        for i in range(0,N[0]):
            for j in range(0,N[1]):
                for k in range(0,N[2]):
        
                    '''ATOMO1'''
                    cristal[iAt,0]=celdaBase[0]+i # coordenadas x
                    cristal[iAt,1]=celdaBase[1]+j # coordenadas y
                    cristal[iAt,2]=celdaBase[2]+k # coordenadas z
                    
                    iAt+=1
        
        return cristal
    

# arreglo variables para graficar

C = generaCristal(N,tipo)

xs = []
ys = []
zs = []

for i in range(0,len(C)):
    xs.append(C[i][0])
    ys.append(C[i][1])
    zs.append(C[i][2])

# grafica 
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.scatter(xs, ys, zs,c='red')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()







