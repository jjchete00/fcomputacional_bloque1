#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:20:28 2021

@author: chetevidaljustamante
"""

import numpy as np
import matplotlib.pyplot as plt
from random import random,randrange,choice


N = int(input('Número de partículas? '))
T = float(input('Temperatura? '))
pas = int(input('Pasos del Monte Carlitos? '))

n = np.ones([N,3],int)
Et = 3*N*np.pi**2/2
E = []

for paso in range(pas):
    
    i = randrange(N)
    j = randrange(3)
    k = choice([0,1])

    if k == 0.: 
        dn = 1
        dE = ((np.pi**2)/(2))*(2*n[i,j]+1)
    if k == 1.: 
        dn = -1
        dE = ((np.pi**2)/(2))*(-2*n[i,j]+1)
    

    if n[i,j]>1 or dn==1:
        if random() < np.exp(-dE/T):
            n[i,j] += dn
            Et+=dE
        E.append(Et)


plt.figure()
t = np.linspace(0,pas,len(E))
plt.plot(t,E)
plt.xlabel('Pasos del Monte Carlo')
plt.ylabel('Energía')
plt.show()
















