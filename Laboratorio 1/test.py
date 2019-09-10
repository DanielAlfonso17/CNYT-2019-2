import unittest
import Laboratorio
class TestUM(unittest.TestCase):
    #suma
    def test_caso_suma_1(self):
        self.assertEqual((1,3),Laboratorio.sumaImaginarios((1,2),(0,1)))
    #multiplicacion    
    def test_caso_producto_1(self):
        self.assertEqual((-52,-20),Laboratorio.productoImaginarios((-4,0),(13,5)))
    def test_caso_producto_2(self):
        self.assertEqual((1,21),Laboratorio.productoImaginarios((1,4),(5,1)))
    #resta    
    def test_caso_resta_1(self):
        self.assertEqual((3,4),Laboratorio.restaImaginarios((5,4),(2,0)))
    #division
    def test_caso_division_1(self):
        self.assertEqual((-1/5,8/5),Laboratorio.divisionImaginarios((3,2),(1,-2)))
    def test_caso_division_2(self):
        self.assertNotEqual((-3,-2),Laboratorio.divisionImaginarios((2,-3),(3,2)))
    #modulo
    def test_caso_modulo_1(self):
        self.assertEqual((34**0.5),Laboratorio.moduloImaginario((3,5)))
    #conjugado
    def test_caso_conjugado_1(self):
        self.assertEqual((1,-2),Laboratorio.conjugadoImaginario((1,2)))
    #polarAcartesiano
    def test_caso_polarAcartesiano_1(self):
        self.assertEqual((2.0,-5.0),Laboratorio.dePolarACartesiano((5.38,291.80)))
    #cartesianoApolar
    def test_caso_cartesianoApolar_1(self):
        self.assertEqual((3.16,71.57),Laboratorio.deCartesianoAPolar((1,3)))
    #fase
    def test_caso_fase_1(self):
        self.assertEqual((291.80),Laboratorio.faseComplejos((2,-5)))
if __name__ =='__main__':
    unittest.main()
