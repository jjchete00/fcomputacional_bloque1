#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:42:55 2021

@author: chetevidaljustamante
"""

import numpy as np
import matplotlib.pyplot as plt


sigma = 2.3151
n = 12.
m = 6.
eps = 0.167


def V(r):

    return 4*eps*( (sigma/r)**n - (sigma/r)**m )


# establezco el numero de particulas

Nx = int(input('Nx='))
Ny = int(input('Ny='))
Nz = int(input('Nz='))
tipo = input('Tipo de cristal:')
cond = input('Condiciones de contorno: 1 (libres) o 2 (periodicas) ')
N = [Nx,Ny,Nz]

anch = 3.603 #anchura de cada celda


def generaCristal(N,tipo):
    
    if tipo == 'fcc':
        # parte 1
        nAt = int(4*N[0]*N[1]*N[2])
        cristal = np.empty((nAt,3))
        celdaBase = np.array([[0,0,0],[0,0.5,0.5],[0.5,0,0.5],
                              [0.5,0.5,0]])
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

        return cristal*anch
                    
    if tipo == 'bcc':
            
        celdaBase = np.array([[0,0,0]])
        nAt = int(4*N[0]*N[1]*N[2])
        cristal = np.empty((nAt,3))
        iAt = 0 #indice del atomo
            
        for i in range(0,N[0]):
            for j in range(0,N[1]):
                for k in range(0,N[2]):
        
                    '''ATOMO1'''
                    cristal[iAt,0]=celdaBase[0,0]+i # coordenadas x
                    cristal[iAt,1]=celdaBase[0,1]+j # coordenadas y
                    cristal[iAt,2]=celdaBase[0,2]+k # coordenadas z
                    iAt+=1
        
        return cristal*anch
    





cristal = generaCristal(N,tipo)

x = []
y = []
z = []

for i in range(len(cristal)):
    x.append(cristal[i][0])
    y.append(cristal[i][1])
    z.append(cristal[i][2])




Ep = 0
E = []
if cond == '1': # superficies libres
    for i in range(len(cristal)):
        
        Ei = 0
        for j in range(len(cristal)):
            
            dx = x[j]-x[i]
            dy = y[j]-y[i]
            dz = z[j]-z[i]
            r = np.sqrt(dx**2+dy**2+dz**2)   

            if r==0:
                V_ij= 0
            elif r <= 3*sigma:
                V_ij=V(r)
                Ep += 0.5*V_ij #añado el potencial a la energia
            else:
                V_ij = 0
                
            Ei +=0.5*V_ij
            
        E.append(Ei)
  

if cond == '2': # condiciones periodicas
    
    for i in range(len(cristal)):
        
        Ei = 0
        for j in range(len(cristal)):

            dx = x[j]-x[i]
            dy = y[j]-y[i]
            dz = z[j]-z[i]
            
            if dx >0:
                if dx > Nx*anch/2:
                    dx-=Nx*anch
            if dx<0:
                if dx < -Nx*anch/2:
                    dx+=Nx*anch 
                    
            if dy>0:
                if dy > Ny*anch/2:
                    dy-=Ny*anch
            if dy<0:
                if dy < -Ny*anch/2:
                    dy+=Ny*anch
                
            if dz>0:
                if dz > Nz*anch/2:
                    dz-=Nz*anch
            if dz<0:
                if dz < -Nz*anch/2:
                    dz+=Nz*anch


            r = np.sqrt(dx**2+dy**2+dz**2)
            
            if r==0:
                V_ij= 0
            elif r <= 3*sigma:
                V_ij=V(r)
                Ep += 0.5*V_ij #añado el potencial a la energia
            else:
                V_ij = 0
                
            Ei += 0.5*V_ij
            
        E.append(np.round(Ei,decimals=13))

nAt = int(4*N[0]*N[1]*N[2])


print('La energia potencial es',Ep)
print('Energia por atomo = ',Ep/nAt)



'''GRAFICAS'''


#################### forma del cristal



fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.scatter(x, y, z,c='red',lw=10)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()



'''
AL APLICAR LAS CONDICIONES DE CONTORNO PERIODICAS SUMAMOS A CADA UNO DE LOS
ATOMOS DE LOS BORDES COMO SI HUBIESEN MAS ATOMOS A SUS LADOS...
POR LO TANTO, LA ENERGIA POTENCIAL POR ATOMO DEBERA SER MAYOR EN VALOR ABS
SI APLICAMOS LAS CONDICIONES PERIODICAS
'''


################ energia potencial de cada atomo



fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

col = ax.scatter(x, y, z,c=E,cmap='magma',lw=5)
fig.colorbar(col,label='Energía potencial')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()














