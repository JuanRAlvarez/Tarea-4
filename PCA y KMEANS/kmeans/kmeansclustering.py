import numpy as np
import matplotlib as plt
from pylab import *

datos = np.loadtxt('data.dat')
a = np.shape(datos)
n_puntos = a[0]

posx = datos[:,0]
posy = datos[:,1]

n_centros = 2

centrosx = np.empty((n_centros))
centrosy = np.empty((n_centros))
distcentros = np.empty((n_puntos,n_centros))
minimos = np.empty((n_puntos))
colores = np.random.random((n_centros,3))
clustersx = np.empty((0))
clustersy = np.empty((0))


n_iteraciones = 100


for i in range(n_centros):
    a = 14 * np.random.random() - 2
    b = 14 * np.random.random() - 2
    centrosx[i] = a
    centrosy[i] = b


for i in range(n_puntos):
    distcentros[i,:] = np.sqrt((posx[i] - centrosx)**2 + (posy[i] - centrosy)**2)
    minimos[i] = np.argmin(distcentros[i,:])

tama = []
tam = 0
for i in range(n_centros):
    arr_x = np.empty((0))
    arr_y = np.empty((0))
    
    for j in range(n_puntos):
        if (int(minimos[j])==i):
            arr_x = np.append(arr_x,posx[j])
            arr_y = np.append(arr_y,posy[j])
    tam += np.size(arr_x)
    tama.append(tam)
    
    clustersx = np.append(clustersx,arr_x)
    clustersy = np.append(clustersy,arr_y)


clustersx = np.split(clustersx,tama)
clustersy = np.split(clustersy,tama)


for k in range(n_iteraciones):
    for l in range(n_centros):
        if(clustersx[l]!=np.array([])):
            centrosx[l] = np.mean(clustersx[l])
            centrosy[l] = np.mean(clustersy[l])
        else:
            centrosx[l] += (2*np.random.random() - 1)
            centrosy[l] += (2*np.random.random() - 1)
    for i in range(n_puntos):
        distcentros[i,:] = np.sqrt((posx[i] - centrosx)**2 + (posy[i] - centrosy)**2)
        minimos[i] = np.argmin(distcentros[i,:])
    
    
    tama = []
    tam = 0
    clustersx = np.empty((0))
    clustersy = np.empty((0))
    for i in range(n_centros):
        arr_x = np.empty((0))
        arr_y = np.empty((0))
        
        for j in range(n_puntos):
            if (int(minimos[j])==i):
                arr_x = np.append(arr_x,posx[j])
                arr_y = np.append(arr_y,posy[j])
        tam += np.size(arr_x)
        tama.append(tam)
        
        clustersx = np.append(clustersx,arr_x)
        clustersy = np.append(clustersy,arr_y)
    
    clustersx = np.split(clustersx,tama)
    clustersy = np.split(clustersy,tama)


for i in range(n_centros):
    plt.xlabel("Puntos en x")
    plt.ylabel("Puntos en y")
    plt.title("K-means clustering")
    plt.scatter(clustersx[i],clustersy[i],c=colores[i])
    plt.scatter(centrosx[i],centrosy[i],c=colores[i],s=110)

plt.show()