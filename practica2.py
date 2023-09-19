#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:36:53 2021

@author: chetevidaljustamante
"""

import numpy as np
import matplotlib.pyplot as plt



# constantes 

G = 6.6738e-11
M = 1.9891e30
mt = 5.9e24
h = 60*60
t0 = 0.
tf = 5*365*24*60*60+30


# funciones

def radio(x,y):
    r = np.sqrt(x**2 + y**2)
    return (-G*M*x/r**3 , -G*M*y/r**3)


# listas

t_anos = np.linspace(0,5,5*365*24+1)
t_seg = np.linspace(t0,tf+h,h)
N = len(t_anos)
x = np.empty(N)
y = np.empty(N)
r = np.empty(N)
vx = np.empty(2*N)
vy = np.empty(2*N)
v = np.empty(N)
Ep = np.empty(N)
Ec = np.empty(N)

# condiciones iniciales

x[0] = 1.4719e11  # empezamos en el perihelio
y[0] = 0.
vx[0] = 0.
vy[0] = 3.0287e4 

r[0] = np.sqrt(x[0]**2+y[0]**2)
v[0] = np.sqrt(vx[0]**2+vy[0]**2)
Ep[0] = -G*M*mt/r[0]
Ec[0] = 0.5*mt*v[0]**2

# primer punto semientero

vx[1] = vx[0] + 0.5*h*radio(x[0],y[0])[0]
vy[1] = vy[0] + 0.5*h*radio(x[0],y[0])[1]

for i in range(1,N):
    
    x[i] = x[i-1] + h * vx[2*i-1]
    y[i] = y[i-1] + h * vy[2*i-1]  
    r[i] = np.sqrt(x[i]**2 + y[i]**2)
    
    kx = h*radio(x[i],y[i])[0]
    ky = h*radio(x[i],y[i])[1]

    vx[2*i] = vx[2*i-1] + kx*0.5
    vy[2*i] = vy[2*i-1] + ky*0.5
    
    
    vx[2*i+1] = vx[2*i-1] + kx
    vy[2*i+1] = vy[2*i-1] + ky
    
    v[i] = np.sqrt(vx[2*i]**2+vy[2*i]**2)
    
    
    Ep[i] = -G*mt*M/r[i]
    Ec[i] = 0.5*mt*v[i]**2

# graficamos 


''' APARTADO a'''
plt.figure(1)
plt.title('Distancia al sol $(r)$ en función del tiempo')
plt.xlabel('$t (años)$')
plt.ylabel('$r (m)$')
plt.plot(t_anos,r)
plt.show()

'''APARTADO b'''
plt.figure(2)
plt.title('Trayectoria x = f(y) ')
plt.ylabel('$x (m)$')
plt.xlabel('$y (m)$')
plt.plot(y,x,c='r')
plt.show()
'''APARTADO c'''
plt.figure(3)
plt.title('Energías')
plt.plot(t_anos,Ep,c='b')
plt.plot(t_anos,Ec,c='y')
plt.plot(t_anos,Ec+Ep,c='g')
plt.show()



























