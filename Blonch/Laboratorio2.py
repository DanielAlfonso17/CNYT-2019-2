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

def restaImaginarios(c1,c2):
    c3 = [0,0]
    uno = (-1*c2[0])
    dos = (-1*c2[1])
    c3[0] = c1[0] + uno
    c3[1] = c1[1] + dos
    return (c3[0],c3[1])

def conjugadoImaginario(c1):
    c3 = [0,0]
    c3[0] = c1[0]
    c3[1] = (-1*c1[1])
    return (c3[0],c3[1])

def inversoImaginario(c1):
    resA = (-1*c1[0])
    resB = (-1*c1[1])
    return (resA,resB)

def conjugadoImaginario(c1):
    c3 = [0,0]
    c3[0] = c1[0]
    c3[1] = (-1*c1[1])
    return (c3[0],c3[1])

"""
Funciones Laboratorio 2
"""

#(1) Suma de vectores complejos 
def adicionVectoresImaginarios(c1,c2):
    res = [] 
    for i in range(len(c1)):
        res.append(sumaImaginarios(c1[i],c2[i]))
    return res

#(2)Inverso aditivo de vector complejo 
def inversaVectoresImaginarios(c1):
    res = []
    for i in range(len(c1)):
        res.append(inversoImaginario(c1[i]))
    return res

#(3) Multiplicacion de escalar por vector complejo 
def multiplicacionEscalarVector(c1,v1):
    res = []
    for i in range(len(v1)):
        res.append(productoImaginarios(c1,v1[i]))
    return res

#(4) Suma de matrices complejos 
def adicionMatricesImaginarias(m1,m2):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m2[i])):
            vector.append(sumaImaginarios(m1[i][j],m2[i][j]))
        matriz.append(vector)
    return matriz

#(5) Inverso aditivo de matriz compleja
def inversaMatrizImaginaria(m1):
    matriz = []
    for i in range(0,len(m1)):
        matriz.append(inversaVectoresImaginarios(m1[i]))
    return matriz

#(6) Multipliacion espacalar por matriz compleja 
def complejoPorMatriz(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(productoImaginarios(m1[i][j],c1))
        matriz.append(vector)
    return matriz

#(7) Transpuesta de matriz compleja
def matrizTranspuesta(m1):
    matriz=[]
    for i in range(0,len(m1[0])):
        columna = [row[i] for row in m1]
        matriz.append(columna)
    return matriz 
        
#(8) Conjugada de matriz compleja        
def matrizConjugada(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0],m1[i][j][1]*-1))
        matriz.append(vector)
    return matriz
#(9) Adjunta (daga) de matriz compleja

def matrizAdjunta(m1):
    matriz=matrizTranspuesta(m1)
    matriz=matrizConjugada(matriz)
    return matriz

#(10) Producto de matrices complejas
def productoMatricesImaginarias(m1,m2):
    matriz = [[None] * len(m2[0]) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            columna = [row[j] for row in m2]
            matriz[i][j] = productoVectoresImaginarios(m1[i],columna)
    return matriz
#(11) Acción de matriz compleja sobre vector complejo
def accionMatrizSobreVector(v1,m1):
    v = []
    for i in range(len(m1)):    
            v.append(productoVectoresImaginarios(v1,m1[i]))
    return v

#(12) Producto interno de vectores complejos

def productoInternoVectoresImaginarios(c1,c2):
    ini = (0,0)
    for i in range(len(c1)):
        c3 = conjugadoImaginario(c1[i])
        suma = productoImaginarios(c3,c2[i])
        ini = sumaImaginarios(ini,suma)
    return ini


#(13) Norma de vector complejo
def normaVectorImaginario(v1):
    suma =0
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            suma += ((v1[i][j])**2)
    return suma**(1/2)

#(14) Distancia entre dos vectores complejos
def distanciaDosVectoresImaginarios(v1,v2):
    suma = 0
    for i in range(len(v1)):
        for j in range(len(v1[i])):
            resta =v2[i][j]-v1[i][j]
            suma += resta**2
    return suma**(1/2)
#(15) ¿Es la matriz compleja una matriz unitaria?
def matrizUnitaria(m1):
    esUnitaria = False
    MatrizId=[[(1,0) if j == i else (0,0) for j in range(len(m1))] for i in range(len(m1))]
    for i in range(len(m1)):
        if(len(m1)!=len(m1[i])):
            return "La matriz debe tener el mismo numero de filas y columnas"        

    if(productoMatricesImaginarias(m1,matrizAdjunta(m1))==MatrizId):
        esUnitaria = True
    return esUnitaria

#(16) ¿Es la matriz compleja una matriz hermitiana?
def matrizHermitiana(m1):
    m1T = matrizAdjunta(m1)
    if m1T == m1:
        return True
    return False

def productoVectoresImaginarios(c1,c2):
    ini = (0,0)
    for i in range(len(c1)):
        suma = productoImaginarios(c1[i],c2[i])
        ini = sumaImaginarios(ini,suma)
    return ini
#(17) Producto tensorial de matrices complejas  
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




