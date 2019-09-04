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

def inversaMatriz(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0]*-1,m1[i][j][1]*-1))
        matriz.append(vector)
    return matriz

def esHermitiana(m1):
    m2 = matrizAdjunta(m1)
    if(m1 == m2):
        return True
    return False

def esUnitaria(m1):
    unitaria = True
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            if i == j and m1[i][j] == 1:
                unitaria = True 
            if i != j and m1[i][j] != 0:
                unitaria = False
    return unitaria

print(esUnitaria([[1,1],[1,1]]))
    
def complejoPorMatriz(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(productoImaginarios(m1[i][j],c1))
        matriz.append(vector)
    return matriz



class TestUM(unittest.TestCase):

    def test_caso_Adicion_Vectores_I(self):
        self.assertEqual([(22,-1.7),(7,-4),(10.2,-8.1),(0,-7)],adicionVectoresImaginarios([(6,-4),(7,3),(4.2,-8.1),(0,-3)],[(16,2.3),(0,-7),(6,0),(0,-4)]))

    def test_caso_Inversa_Vectores_I(self):
        self.assertEqual([(0.5,-0.5),(0.15,0.23),(-0.12,-0.47)],inversaVectoresImaginarios([(1,1),(2,-3),(-0.5,2)]))

    def test_caso_Producto_Vectores_I(self):
        self.assertEqual((0,20),productoVectoresImaginarios([(1,1),(2,2),(3,3)],[(3,3),(2,2),(1,1)]))
    
    def test_caso_sumaMatriz_1(self):
        self.assertEqual([[(8, -4), (11, 0)], [(3, 7), (-9, -7)]],adicionMatricesImaginarias([[[3,2],[4,-2]],[[1,2],[3,2]]],[[[5,-6],[7,2]],[[2,5],[-12,-9]]]))    
    
    def test_caso_Inversa_Matriz_I(self):
        self.assertEqual([[(0.2, -0.4), (0.25, -0.25)], [(0.17, -0.17), (0.1, -0.1)]],inversaMatrizImaginaria([[(1,2),(2,2)],[(3,3),(5,5)]]))
        
    def test_caso_Productro_Matrices_I(self):
        self.assertEqual([[(9,6), (5,-4)], [(10, 30), (0,0)],[(4,1),(0,1)]],productoMatricesImaginarias([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]],[[(1,-1),(0,-1)],[(0,5),(0,0)]]))

    def test_caso_Matriz_Transpuesta(self):
        self.assertEqual([[(4,5), (0,0),(-1,0)], [(1,0),(6, -2),(0,-1)]],matrizTranspuesta([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))

    def test_caso_Matriz_Conjugada(self):
        self.assertEqual([[(4,-5), (1,0)], [(0,0),(6,2)],[(-1,0),(0,1)]],matrizConjugada([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))    

    def test_caso_Matriz_Adjunta(self):
        self.assertEqual([[(4,-5), (0,0),(-1,0)], [(1,0),(6, 2),(0,1)]],matrizAdjunta([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))

    def test_caso_Matriz_Hermitiana(self):
        self.assertEqual(True,esHermitiana([[(2,0),(3,-1)],[(3,1),(-1,0)]]))


if __name__ =='__main__':
    unittest.main()
    

