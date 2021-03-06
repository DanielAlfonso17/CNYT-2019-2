import matplotlib.pyplot as plt
import math
#------------------------------------Funciones Complementarias---------------------------------------------------#
def productoVectoresImaginarios(c1,c2):
    ini = (0,0)
    for i in range(len(c1)):
        suma = productoImaginarios(c1[i],c2[i])
        ini = sumaImaginarios(ini,suma)
    return ini

def sumaImaginarios(c1,c2):
    c3 = [0,0]
    c3[0] = c1[0] + c2[0]
    c3[1] = c1[1] + c2[1]
    return (c3[0],c3[1])

def productoImaginarios(c1,c2):
    c3 = [0,0,0,0]
    res = [0,0] 
    m = 0
    for j in c1:
        for i in c2:
            c3[m] = j*i
            m += 1        
    res[0] = c3[0] + (-1*c3[3]) 
    res[1] = c3[1] + c3[2]
    return (res[0],res[1])

def accionMatrizSobreVector(v1,m1):
    v = []
    for i in range(len(m1)):    
            v.append(productoVectoresImaginarios(v1,m1[i]))
    return v


def multiplicacionMatrizVector(v1,m1):
    vector = [] 
    for i in range(len(m1)):
        suma = 0
        for j in range(len(m1[i])):
            mult= m1[i][j]*v1[j]
            suma += mult
        vector.append(suma)
    return vector 


def productoTensorial(m1,m2):
    matriz = []
    for i in range(len(m1)):
        matM = [[]] *len(m2)
        for j in range(len(m1[i])):
            m3 = complejoPorMatriz(m1[i][j],m2)
            for k in range(len(m2)):
                matM[k] = matM[k] + m3[k]
        for k in range(len(m2)):
            matriz.append(matM[k])
    return matriz


def productoTensorialVectores(v1,v2):
    vFinal = [0 for i in range(len(v1)*len(v2))]
    cont = 0
    for i in range(len(v1)):
        v3 = complejoPorVector(v1[i],v2)
        for k in range(len(v3)):
            vFinal[cont] = v3[k]
            cont+=1
    return vFinal


def complejoPorMatriz(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(productoImaginarios(m1[i][j],c1))
        matriz.append(vector)
    return matriz

def complejoPorVector(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
            matriz.append(productoImaginarios(m1[i],c1))
    return matriz

#------------------------------------Dinamica del Sistema Clasico---------------------------------------------------#
#Parametro numero de clicks de tiempo 
def dinamicaSistemaClasico(clicks):
    # Matriz de dinámica para el sistema clásico de canicas
    matriz = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0]], 
     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0]], 
     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0]], 
     [[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]], 
     [[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]], 
     [[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]], 
     [[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]], 
     [[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
     [[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]], 
     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]], 
     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0]], 
     [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]
    # Vector de estado inicial 
    vectorI=[[10,0],[4,0],[1,0],[7,0],[2,0],[2,0],[11,0],[0,0],[3,0],[1,0],[0,0],[5,0],[2,0]]    
    estado = vectorI
    for i in range(clicks):
        estado = accionMatrizSobreVector(estado,matriz)
    fig = plt.figure(u'Evolucion Dinamica del Sistema Clasico despues de 25 clicks de Tiempo') # Figure
    ax = fig.add_subplot(111) # Axes

    nombres = ['P.0','P.1','P.2','P.3','P.4','P.5','P.6','P.7','P.8','P.9','P.10','P.11','P.12']
    datos = [estado[0][0],estado[1][0],estado[2][0],estado[3][0],estado[4][0],estado[5][0],estado[6][0],estado[7][0],estado[8][0],estado[9][0],estado[10][0],estado[11][0],estado[12][0]]
    xx = range(len(datos))

    ax.bar(xx, datos, width=0.5, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)

    plt.show()
    return estado
#Sistema dinamica clasico despues de 25 clicks
dinamicaSistemaClasico(25)
#------------------------------------Dinamica Sistema Probabilistico---------------------------------------------------#
def sistemaProbabilistico(clicks):
    # Matriz de la dinámica para el sistema probabilístico A
    MA = [[[0,0],[0.2,0],[0.3,0],[0.5,0]],
      [[0.3,0],[0.2,0],[0.1,0],[0.4,0]],
      [[0.4,0],[0.3,0],[0.2,0],[0.1,0]],
      [[0.3,0],[0.3,0],[0.4,0],[0,0]]]
    # Matriz de la dinámica para el sistema probabilístico B
    MB = [[[0,0],[1/6,0],[5/6,0]], 
      [[1/3,0],[1/2,0],[1/6,0]], 
      [[2/3,0],[1/3,0],[0,0]] 
     ]
    # Vector de estado inicial sistema probabilístico A
    VA = [[0.2,0],[0.1,0],[0.6,0],[0.1,0]]
    # Vector de estado inicial sistema probabilístico B
    VB = [[0.7,0],[0.15,0],[0.15,0]]
    m1 = productoTensorial(MA,MB)
    vectorI= productoTensorialVectores(VA,VB)
    estado = vectorI
    for i in range(clicks):
        estado = accionMatrizSobreVector(estado,m1)
    fig = plt.figure(u'Evolucion Dinamica del Sistema ensamblado A-B despues de 5 clicks de tiempo') # Figure
    ax = fig.add_subplot(111) # Axes

    nombres = ['00','01','02','10','11','12','20','21','22','30','31','32']
    datos = [estado[0][0],estado[1][0],estado[2][0],estado[3][0],estado[4][0],estado[5][0],estado[6][0],estado[7][0],estado[8][0],estado[9][0],estado[10][0],estado[11][0]]
    xx = range(len(datos))

    ax.bar(xx, datos, width=0.5, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)

    plt.show()
    return estado
#Sistema probabilistico despues de 5 clicks de tiempo 
sistemaProbabilistico(5)





