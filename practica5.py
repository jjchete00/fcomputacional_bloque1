import numpy as np
import matplotlib.pyplot as plt


sigma = 2.3151
n = 12.
m = 6.
eps = 0.167


def V(r):

    return 4*eps*( (sigma/r)**n - (sigma/r)**m )

def derV(r):
    
    return 4*eps*( (m*sigma**m)/r**(m+1) - (n*sigma**n)/r**(n+1) ) 


# establezco el numero de particulas

Nx = int(input('Nx='))
Ny = int(input('Ny='))
Nz = int(input('Nz='))
tipo = input('Tipo de cristal:')
cond = input('Condiciones de contorno:')
N = [Nx,Ny,Nz]
nAt = int(4*N[0]*N[1]*N[2])

anch = 3.603 #anchura de cada celda
mc = 63.55 #uma

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
F = np.zeros([len(cristal),3])
F_lista=[]

if cond == '1':
    for i in range(len(cristal)):
        Ei = 0
        for j in range(len(cristal)):
            
            dx = x[i]-x[j]
            dy = y[i]-y[j]
            dz = z[i]-z[j]
            r = np.sqrt(dx**2+dy**2+dz**2)   

            if r==0:
                V_ij= 0
                
            elif r <= 3*sigma:
                V_ij=V(r)
                Ep += 0.5*V_ij #añado el potencial a la energia
                
                F[i][0] += -0.5* derV(r)*dx/r
                F[i][1] += -0.5* derV(r)*dy/r
                F[i][2] += -0.5* derV(r)*dz/r
                Ft = np.round(np.sqrt(F[i][0]**2+F[i][1]**2+F[i][2]**2),decimals=2)
            else:
                V_ij = 0

            Ei +=0.5*V_ij
            

        F_lista.append(Ft)
        E.append(Ei)
  

if cond == '2':
    
    for i in range(len(cristal)):
        
        Ei = 0
        for j in range(len(cristal)):

            dx = x[i]-x[j]
            dy = y[i]-y[j]
            dz = z[i]-z[j]
            

            if dx >0:
                if dx > Nx*anch/2:
                    dx-=Nx*anch
            if dx<0:
                if dx < -Nx*anch/2:
                    dx+=Nx*anch 
                    5
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
                
                F[i][0] += -0.5* derV(r)*dx/r
                F[i][1] += -0.5* derV(r)*dy/r
                F[i][2] += -0.5* derV(r)*dz/r
                
                Ft = np.round(np.sqrt(F[i][0]**2+F[i][1]**2+F[i][2]**2),decimals=2)
                
            else:
                V_ij = 0
                
                
            Ei += 0.5*V_ij
            
        F_lista.append(Ft)
        E.append(Ei)
        
           
        
        
        

V = np.random.random_sample([len(cristal),3])-0.5

'''GRAFICAS'''


################ fuerza ejercida por cada átomo

# la matriz de escalares F

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

col = ax.scatter(x, y, z,c=F_lista,cmap='magma',lw=4)
fig.colorbar(col,label='Fuerza')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()



# la matriz de vectores Fi

U = []
W = []
H = []

for i in range(len(F)):
    U.append(10*F[i,0])
    W.append(10*F[i,1])
    H.append(10*F[i,2])

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#col = ax.scatter(x, y, z,c=F_lista,cmap='inferno',lw=3)
ax.quiver(x, y, z,U,W,H,color='purple')
#fig.colorbar(col,label='Fuerza')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()









