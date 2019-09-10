import unittest
import Laboratorio2
class TestUM(unittest.TestCase):

    def test_caso_Adicion_Vectores_I(self):
        self.assertEqual([(22,-1.7),(7,-4),(10.2,-8.1),(0,-7)],Laboratorio2.adicionVectoresImaginarios([(6,-4),(7,3),(4.2,-8.1),(0,-3)],[(16,2.3),(0,-7),(6,0),(0,-4)]))

    def test_caso_Inversa_Vectores_I(self):
        self.assertEqual([(0.5,-0.5),(0.15,0.23),(-0.12,-0.47)],Laboratorio2.inversaVectoresImaginarios([(1,1),(2,-3),(-0.5,2)]))

    def test_caso_Producto_Vectores_I(self):
        self.assertEqual((0,20),Laboratorio2.productoVectoresImaginarios([(1,1),(2,2),(3,3)],[(3,3),(2,2),(1,1)]))
    
    def test_caso_sumaMatriz_1(self):
        self.assertEqual([[(8, -4), (11, 0)], [(3, 7), (-9, -7)]],Laboratorio2.adicionMatricesImaginarias([[[3,2],[4,-2]],[[1,2],[3,2]]],[[[5,-6],[7,2]],[[2,5],[-12,-9]]]))    
    
    def test_caso_Inversa_Matriz_I(self):
        self.assertEqual([[(0.2, -0.4), (0.25, -0.25)], [(0.17, -0.17), (0.1, -0.1)]],Laboratorio2.inversaMatrizImaginaria([[(1,2),(2,2)],[(3,3),(5,5)]]))
        
    def test_caso_Productro_Matrices_I(self):
        self.assertEqual([[(9,6), (5,-4)], [(10, 30), (0,0)],[(4,1),(0,1)]],Laboratorio2.productoMatricesImaginarias([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]],[[(1,-1),(0,-1)],[(0,5),(0,0)]]))

    def test_caso_Matriz_Transpuesta(self):
        self.assertEqual([[(4,5), (0,0),(-1,0)], [(1,0),(6, -2),(0,-1)]],Laboratorio2.matrizTranspuesta([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))

    def test_caso_Matriz_Conjugada(self):
        self.assertEqual([[(4,-5), (1,0)], [(0,0),(6,2)],[(-1,0),(0,1)]],Laboratorio2.matrizConjugada([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))    

    def test_caso_Matriz_Adjunta(self):
        self.assertEqual([[(4,-5), (0,0),(-1,0)], [(1,0),(6, 2),(0,1)]],Laboratorio2.matrizAdjunta([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))

    def test_caso_ProductoTensor(self):
        m=[[(1,0),(2,0)],[(3,0),(4,0)]]
        m1=[[(1,0),(2,0),(3,0)],[(1,0),(2,0),(3,0)],[(1,0),(2,0),(3,0)]]
        self.assertEqual([[(1, 0), (2, 0), (3, 0), (2, 0), (4, 0), (6, 0)], [(1, 0), (2, 0), (3, 0), (2, 0), (4, 0), (6, 0)], [(1, 0), (2, 0), (3, 0), (2, 0), (4, 0), (6, 0)], [(3, 0), (6, 0), (9, 0), (4, 0), (8, 0), (12, 0)], [(3, 0), (6, 0), (9, 0), (4, 0), (8, 0), (12, 0)], [(3, 0), (6, 0), (9, 0), (4, 0), (8, 0), (12, 0)]],Laboratorio2.productoTensorialImaginario(m,m1))

    def test_caso_Accion_Matriz_Vector(self):
        self.assertEqual([(9, -3), (-15, 0)],Laboratorio2.accionMatrizSobreVector([(-3,1),(5,0)],[[(2,0),(3,-1)],[(3,1),(-1,0)]]))
        

if __name__ =='__main__':
    unittest.main()
    
