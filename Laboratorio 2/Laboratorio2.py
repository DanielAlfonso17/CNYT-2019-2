import math
import unittest

"""
Funciones Requeridas 
"""
def sumaImaginarios(c1,c2):
    c3 = [0,0]
    c3[0] = c1[0] + c2[0]
    c3[1] = c1[1] + c2[1]
    return (round(c3[0],2),round(c3[1],2))

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

def conjugadoImaginario(c1):
    c3 = [0,0]
    c3[0] = c1[0]
    c3[1] = (-1*c1[1])
    return (c3[0],c3[1])

def inversoImaginario(c1):
    conj = conjugadoImaginario(c1)
    a = conj
    b = (c1[0]**2) + (c1[1]**2)
    resA = round((a[0]/b),2)
    resB = round((a[1]/b),2)
    return (resA,resB)


"""
Funciones Laboratorio 2
"""


def adicionVectoresImaginarios(c1,c2):
    res = [] 
    for i in range(len(c1)):
        res.append(sumaImaginarios(c1[i],c2[i]))
    return res 

def inversaVectoresImaginarios(c1):
    res = []
    for i in range(len(c1)):
        res.append(inversoImaginario(c1[i]))
    return res

def productoVectoresImaginarios(c1,c2):
    ini = (0,0)
    for i in range(len(c1)):
        suma = productoImaginarios(c1[i],c2[i])
        ini = sumaImaginarios(ini,suma)
    return ini
        
def adicionMatricesImaginarias(m1,m2):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m2)):
            vector.append((m1[i][j][0]+m2[i][j][0],m1[i][j][1]+m2[i][j][1]))
        matriz.append(vector)
    return matriz

def inversaMatrizImaginaria(m1):
    matriz = []
    for i in range(0,len(m1)):
        matriz.append(inversaVectoresImaginarios(m1[i]))
    return matriz


def productoMatricesImaginarias(m1,m2):
    matriz = [[None] * len(m2[0]) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            columna = [row[j] for row in m2]
            matriz[i][j] = productoVectoresImaginarios(m1[i],columna)
    return matriz

def matrizTranspuesta(m1):
    matriz=[]
    for i in range(0,len(m1[0])):
        columna = [row[i] for row in m1]
        matriz.append(columna)
    return matriz 
        
        
def matrizConjugada(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0],m1[i][j][1]*-1))
        matriz.append(vector)
    return matriz

def matrizAdjunta(m1):
    matriz=matrizTranspuesta(m1)
    matriz=matrizConjugada(matriz)
    return matriz

def accionMatrizSobreVector(v1,m1):
    v = []
    for i in range(len(m1)):    
            v.append(productoVectoresImaginarios(v1,m1[i]))
    return v

def inversaMatriz(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0]*-1,m1[i][j][1]*-1))
        matriz.append(vector)
    return matriz

def complejoPorMatriz(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(productoImaginarios(m1[i][j],c1))
        matriz.append(vector)
    return matriz

def productoTensorialImaginario(m1,m2):
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




