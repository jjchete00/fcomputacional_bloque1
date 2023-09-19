#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 15:13:48 2021

@author: chetevidaljustamante
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

def f(x):
    return np.sin(1/(x*(2-x)))**2
''' gaussiana
def f(x):
    return np.exp(-x**2)
'''
'''Hola!
Las respuestas a las preguntas estan en:
1. Lineas 68-87  
2. Lineas 24-67
3. Lineas 90-132 
4. Lineas 68-87
La respuesta a la pregunta planteada esta en la linea 137 
'''
'''EJERCICIO 2'''
# defino el rectangulo donde integrare

h,l = 1,0 # maximo y minimo del rectangulo
a,b = -2,2 # intervalo de integracion


# pasos del monte carlo

N = 10000 

# ploteo los puntos aleatorios dentro del rectangulo
p_x = (b-a)*np.random.rand(N)+a
p_y = (h-l)*np.random.rand(N)+l


#aqui metere los que quedan por debajo de la funcion
y_acept = []
x_acept = []
y_nacept = []
x_nacept = []

# que puntos quedan debajo de la curva?
bajo = 0
for i in range(0,N):
    if p_y[i]<f(p_x[i]):
        x_acept.append(p_x[i])
        y_acept.append(p_y[i])
        bajo+=1
    else:
        x_nacept.append(p_x[i])
        y_nacept.append(p_y[i])


N_p = bajo/N # el porcentaje de puntos que caen bajo la funcion
A = (h-l)*(b-a) # area del rectangulo
I = N_p*A# el valor del area de la funcion dentro del rectangulo [a,b]x[l,h]
err = np.sqrt((I*(A-I))/N)



# printeo el valor de la integral

print('La integral vale ',I,'+-',err)
      

''' EJERCICIO 1 Y 4 '''

# graficamos

t = np.linspace(a,b,1000)

plt.figure(1)
plt.title('$f(x)$')
plt.plot(t,f(t))
plt.show()
plt.figure(2)
plt.title('Puntos generados aleatoriamente(Monte Carlo)')
plt.plot(x_acept,y_acept,'.',c='g',label='puntos aceptados')
plt.plot(x_nacept,y_nacept,'.',c='r',label='puntos no aceptados')
plt.plot(t,f(t),c='black',lw=2,label='función')
plt.legend()
plt.show()



''' EJERCICIO 3'''
'''
AHORA CALCULO EL VALOR DE I EN FUNCION DEL NUMERO DE PASOS N
'''

n = 10 # valor del intervalo de pasos 

integrales = []
errores = []
errores_max = []
errores_min = []

while n < N:
    
    bajo = 0
    for i in range(0,n):
        if p_y[i]<f(p_x[i]):
            bajo+=1
            
    n_p = bajo/n # el porcentaje de puntos que caen bajo la funcion
    
    
    A = (h-l)*(b-a) # area del rectangulo
    I = n_p*A #el valor del area de la funcion dentro del rectangulo [a,b]x[l,h]
    err = np.sqrt((I*(A-I))/N)
    
    integrales.append(I)
    errores.append(err)
    errores_max.append(I+err)
    errores_min.append(I-err)
    n+=10


t2 = np.linspace(0,N,len(integrales))


plt.figure()
plt.title('Convergencia de I al aumentar pasos en el MC ')
plt.plot(t2,integrales,c='black',label = 'I')
plt.plot(t2,errores_max,c='red',label = 'I $\pm$ error')
plt.plot(t2,errores_min,c='red')
plt.legend()
plt.show()



'''
Los calculos se haran menos precisos dependiendo de lo grande que sea la altura
de nuestro rectangulo (si mantenemos el numero de puntos aleatorio)
Esto es porque hay un area mayor y la probabilidad de que cada punto aleatorio
caiga en la region menor que la funcion es menor.

Si aumentamos el numero de pasos del Monte Carlo, el valor de la integral sera
mucho mas preciso (su error disminuira) ya que tenemos un conjunto de datos 
mayor y nuestro metodo se basa en probabilidad
'''



















