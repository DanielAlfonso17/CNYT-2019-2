import math
import unittest


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

def sumaMatrices(m1,m2):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0]+m2[i][j][0],m1[i][j][1]+m2[i][j][1]))
        matriz.append(vector)
    return matriz


def productoMatrices(m1,m2):
    pass
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
            vector.append(producto(m1[i][j],c1))
        matriz.append(vector)
    return matriz

def matrizTranspuesta(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(m1[j][i])
        matriz.append(vector)
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


class TestUM(unittest.TestCase):
    #suma
    def test_caso_sumaMatriz_1(self):
        self.assertEqual([[(8, -4), (11, 0)], [(3, 7), (-9, -7)]],sumaMatrices([[[3,2],[4,-2]],[[1,2],[3,2]]],[[[5,-6],[7,2]],[[2,5],[-12,-9]]]))
    #Negativa de Matriz   
    def test_caso_NegativaDeMatriz_1(self):
        self.assertEqual([[(-5, 6), (-7, -2)], [(-2, -5), (12, 9)]],inversaMatriz([[[5,-6],[7,2]],[[2,5],[-12,-9]]]))
    """def test_caso_producto_2(self):
        self.assertEqual((1,21),producto((1,4),(5,1)))"""
   
        

if __name__ =='__main__':
    unittest.main()
    

