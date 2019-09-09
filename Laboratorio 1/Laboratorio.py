import unittest
import math 
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
        
def restaImaginarios(c1,c2):
    c3 = [0,0]
    uno = (-1*c2[0])
    dos = (-1*c2[1])
    c3[0] = c1[0] + uno
    c3[1] = c1[1] + dos
    return (c3[0],c3[1])

def moduloImaginario(c1):
    modulo = (c1[0]**2+c1[1]**2)**(1/2)
    return modulo

def conjugadoImaginario(c1):
    c3 = [0,0]
    c3[0] = c1[0]
    c3[1] = (-1*c1[1])
    return (c3[0],c3[1])

def divisionImaginarios(c1,c2):
    conjugado = conjugadoImaginario(c2)
    numerador = productoImaginarios(c1,conjugado)
    denominador = productoImaginarios(c2,conjugado)
    res = [0,0]
    res[0] = numerador[0] / denominador[0]
    res[1] = numerador[1] / denominador[0]
    return (res[0],res[1])

def radianesAGrados(radianes):
    grados = (radianes * 180) / math.pi
    return grados

def faseComplejos(c1):
    angulo = 0
    a = c1[0]
    b = c1[1]
    if (a < 0 and b > 0):
        angulo = math.atan(b/a) + math.pi
    elif( a < 0 and b < 0):
        angulo = math.atan(b/a) + math.pi
    elif (a > 0 and b < 0):
        angulo = math.atan(b/a) + (math.pi*2)
    elif (a == 0 and b > 0):
        angulo = (math.pi) / 2
    elif (a == 0 and b < 0):
        angulo = (-(math.pi)/2) + (math.pi + math.pi)
    elif (a < 0 and b == 0):
        angulo = (math.pi) 
    else:
        angulo = math.atan(b/a)
    res = round(radianesAGrados(angulo),2)
    return res
        
def deCartesianoAPolar(c1):
    mod = moduloImaginario(c1)
    fase = faseComplejos(c1)
    return (round(mod,2),round(fase,2))
    
def dePolarACartesiano(c1):
    return ((round(((c1[0]*math.cos(math.radians(c1[1]))*1000)/(1000)),2),round(((1000*c1[0]*math.sin(math.radians(c1[1])))/1000),2)))

class TestUM(unittest.TestCase):
    #suma
    def test_caso_suma_1(self):
        self.assertEqual((1,3),sumaImaginarios((1,2),(0,1)))
    #multiplicacion    
    def test_caso_producto_1(self):
        self.assertEqual((-52,-20),productoImaginarios((-4,0),(13,5)))
    def test_caso_producto_2(self):
        self.assertEqual((1,21),productoImaginarios((1,4),(5,1)))
    #resta    
    def test_caso_resta_1(self):
        self.assertEqual((3,4),restaImaginarios((5,4),(2,0)))
    #division
    def test_caso_division_1(self):
        self.assertEqual((-1/5,8/5),divisionImaginarios((3,2),(1,-2)))
    def test_caso_division_2(self):
        self.assertNotEqual((-3,-2),divisionImaginarios((2,-3),(3,2)))
    #modulo
    def test_caso_modulo_1(self):
        self.assertEqual((34**0.5),moduloImaginario((3,5)))
    #conjugado
    def test_caso_conjugado_1(self):
        self.assertEqual((1,-2),conjugadoImaginario((1,2)))
    #polarAcartesiano
    def test_caso_polarAcartesiano_1(self):
        self.assertEqual((2.0,-5.0),dePolarACartesiano((5.38,291.80)))
    #cartesianoApolar
    def test_caso_cartesianoApolar_1(self):
        self.assertEqual((3.16,71.57),deCartesianoAPolar((1,3)))
    #fase
    def test_caso_fase_1(self):
        self.assertEqual((291.80),faseComplejos((2,-5)))
if __name__ =='__main__':
    unittest.main()
