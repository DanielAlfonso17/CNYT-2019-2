import unittest
import Laboratorio2
class TestUM(unittest.TestCase):

    #(1) Suma de vectores complejos 
    def test_caso_Adicion_Vectores_PMinima(self):
        self.assertEqual([(16,0),(1,1),(3,-9)],Laboratorio2.adicionVectoresImaginarios([(8,3),(-1,-4),(0,-9)],[(8,-3),(2,5),(3,0)]))
    #(1) Suma de vectores complejos 
    def test_caso_Adicion_Vectores_I(self):
        self.assertEqual([(22,-1.7),(7,-4),(10.2,-8.1),(0,-7)],Laboratorio2.adicionVectoresImaginarios([(6,-4),(7,3),(4.2,-8.1),(0,-3)],[(16,2.3),(0,-7),(6,0),(0,-4)]))
    #(2)Inverso aditivo de vector complejo 
    def test_caso_Inversa_Vectores_PMinima(self):
        self.assertEqual([(5,-2),(-3,0),(0,1)],Laboratorio2.inversaVectoresImaginarios([(-5,2),(3,0),(0,-1)]))
    #(2)Inverso aditivo de vector complejo 
    def test_caso_Inversa_Vectores_I(self):
        self.assertEqual([(-1,-1),(-2,3),(5,-2)],Laboratorio2.inversaVectoresImaginarios([(1,1),(2,-3),(-5,2)]))
    
    def test_caso_Producto_Vectores_I(self):
            self.assertEqual((0,20),Laboratorio2.productoVectoresImaginarios([(1,1),(2,2),(3,3)],[(3,3),(2,2),(1,1)]))
    #(3) Multiplicacion de escalar por vector complejo 
    def test_caso_Producto_Escalar_Por_Vector_PMinima(self):
        self.assertEqual([(-3,-7),(2,0),(7,11)],Laboratorio2.multiplicacionEscalarVector((-1,1),[(-2,5),(-1,-1),(2,-9)]))
    #(4) Suma de matrices complejos         
    def test_caso_sumaMatriz_1(self):
        self.assertEqual([[(8, -4), (11, 0)], [(3, 7), (-9, -7)]],Laboratorio2.adicionMatricesImaginarias([[[3,2],[4,-2]],[[1,2],[3,2]]],[[[5,-6],[7,2]],[[2,5],[-12,-9]]]))
    #(4) Suma de matrices complejos         
    def test_caso_sumaMatriz_PMinima(self):
        self.assertEqual([[(-15, -5), (-10, -6),(7,3)], [(4, 17), (6, -7),(14,-10)],[(5,5),(2,-1),(-2,-1)]],Laboratorio2.adicionMatricesImaginarias([[(-8, -3), (-6, -4),(0,-4)], [(-1, 8), (6, -10),(8,-5)],[(4,0),(8,5),(-7,-9)]],[[(-7, -2), (-4, -2),(7,7)], [(5, 9), (0, 3),(6,-5)],[(1,5),(-6,-6),(5,8)]]))
    #(5) Inverso aditivo de matriz compleja
    def test_caso_Inversa_Matriz_I(self):
        self.assertEqual([[(0.2, -0.4), (0.25, -0.25)], [(0.17, -0.17), (0.1, -0.1)]],Laboratorio2.inversaMatrizImaginaria([[(-0.2,0.4),(-0.25,0.25)],[(-0.17,0.17),(-0.1,0.1)]]))
    #(5) Inverso aditivo de matriz compleja
    def test_caso_Inversa_Matriz_PMinima(self):
        self.assertEqual([[(-7, -3), (1, -7)], [(9, 4), (7, 9)]],Laboratorio2.inversaMatrizImaginaria([[(7,3),(-1,7)],[(-9,-4),(-7,-9)]]))
    #(6) Multipliacion espacalar por matriz compleja
    def test_caso_Complejo_por_Matriz(self):
        self.assertEqual([[(0,13),(-4,32)],[(22,32),(28,10)]],Laboratorio2.complejoPorMatriz((-2,3),[[(3,-2),(8,-4)],[(4,-10),(-2,-8)]]))
    #(7) Transpuesta de matriz compleja
    def test_caso_Matriz_Transpuesta(self):
        self.assertEqual([[(4,5), (0,0),(-1,0)], [(1,0),(6, -2),(0,-1)]],Laboratorio2.matrizTranspuesta([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))
    #(7) Transpuesta de matriz compleja
    def test_caso_Matriz_Transpuesta_PMinima(self):
        self.assertEqual([[(5,9), (8,2)], [(-7,-5),(-3, -7)],[(-1,-4),(7,-8)]],Laboratorio2.matrizTranspuesta([[(5,9),(-7,-5),(-1,-4)],[(8,2),(-3,-7),(7,-8)]]))
    #(8) Conjugada de matriz compleja        
    def test_caso_Matriz_Conjugada(self):
        self.assertEqual([[(4,-5), (1,0)], [(0,0),(6,2)],[(-1,0),(0,1)]],Laboratorio2.matrizConjugada([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))    
    #(8) Conjugada de matriz compleja        
    def test_caso_Matriz_Conjugada_PMinima(self):
        self.assertEqual([[(-6,-1), (3,-8)], [(2,6),(3,0)]],Laboratorio2.matrizConjugada([[(-6,1),(3,8)],[(2,-6),(3,0)]]))
    #(9) Adjunta (daga) de matriz compleja
    def test_caso_Matriz_Adjunta(self):
        self.assertEqual([[(4,-5), (0,0),(-1,0)], [(1,0),(6, 2),(0,1)]],Laboratorio2.matrizAdjunta([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))
    #(9) Adjunta (daga) de matriz compleja
    def test_caso_Matriz_Adjunta_PMinima(self):
        self.assertEqual([[(7,-7), (5,0)], [(3,-8),(8, 6)],[(8,-4),(-10,1)]],Laboratorio2.matrizAdjunta([[(7,7),(3,8),(8,4)],[(5,0),(8,-6),(-10,-1)]]))
    #(10) Producto de matrices complejas
    def test_caso_Productro_Matrices_I(self):
        self.assertEqual([[(9,6), (5,-4)], [(10, 30), (0,0)],[(4,1),(0,1)]],Laboratorio2.productoMatricesImaginarias([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]],[[(1,-1),(0,-1)],[(0,5),(0,0)]]))
    #(10) Producto de matrices complejas
    def test_caso_Productro_Matrices_I_PMinima(self):
        self.assertEqual([[(-33,153), (120,0),(-44,-22)], [(87,0), (-26,-117),(107,70)],[(0,165),(147,26),(69,-36)]],Laboratorio2.productoMatricesImaginarias([[(-6,2),(0,6),(7,2)],[(6,9),(7,7),(-6,-6)],[(5,8),(-6,8),(6,9)]],[[(9,-6),(-3,-4),(5,-2)],[(3,6),(-1,-5),(0,-5)],[(9,9),(8,-4),(-8,-4)]]))
    #(11) Acción de matriz compleja sobre vector complejo
    def test_caso_Accion_Matriz_Vector(self):
        self.assertEqual([(9, -3), (-15, 0)],Laboratorio2.accionMatrizSobreVector([(-3,1),(5,0)],[[(2,0),(3,-1)],[(3,1),(-1,0)]]))

    #(11) Acción de matriz compleja sobre vector complejo
    def test_caso_Accion_Matriz_Vector(self):
        self.assertEqual([(9, -3), (-15, 0)],Laboratorio2.accionMatrizSobreVector([(-3,1),(5,0)],[[(2,0),(3,-1)],[(3,1),(-1,0)]]))

    #(11) Acción de matriz compleja sobre vector complejo
    def test_caso_Accion_Matriz_Vector_PMinima(self):
        self.assertEqual([(54, -32), (0, 17),(41,30)],Laboratorio2.accionMatrizSobreVector([(1,-3),(4,3),(-3,1)],[[(-1,5),(1,-7),(-6,3)],[(-3,-9),(2,-5),(1,-10)],[(-6,5),(6,-5),(3,-2)]]))

    #(12) Producto interno de vectores complejos
    def test_caso_Producto_Interno_Vector_PMinima(self):
        self.assertEqual((4,1),Laboratorio2.productoInternoVectoresImaginarios([(2,-1),(-8,-5),(-2,-6)],[(6,-3),(5,-1),(-6,-2)]))

    #(13) Norma de vector complejo
    def test_caso_Norma_Vectores_Imaginarios_PMinima(self):
        self.assertEqual(10,Laboratorio2.normaVectorImaginario([(4,5),(3,1),(0,-7)]))

    #(14) Distancia entre dos vectores complejos
    def test_caso_Distancia_entre_Vectores_PMinima(self):
        self.assertEqual(12,Laboratorio2.distanciaDosVectoresImaginarios([(2,7),(4,-1),(2,-4)],[(7,8),(2,-8),(1,4)]))

    #(15) ¿Es la matriz compleja una matriz unitaria?
    def test_caso_Matriz_Unitaria_PMinima(self):
        self.assertEqual(True,Laboratorio2.matrizUnitaria([[((1/(2**(1/2))),0),(0,(1/(2**(1/2))))],[(0,(1/(2**(1/2)))),((1/(2**(1/2))),0)]]))

    #(15) ¿Es la matriz compleja una matriz unitaria?
    def test_caso_Matriz_Unitaria_PMinima1(self):
        self.assertEqual(False,Laboratorio2.matrizUnitaria([[(0,1),(1,0),(0,0)],[(0,0),(0,1),(1,0)],[(1,0),(0,0),(0,1)]]))
    

    #(16) ¿Es la matriz compleja una matriz hermitiana?
    def test_caso_Matriz_Hermitiana(self):
        self.assertEqual(True,Laboratorio2.matrizHermitiana([[(2,0),(3,-1)],[(3,1),(-1,0)]]))
        
    #(16) ¿Es la matriz compleja una matriz hermitiana?
    def test_caso_Matriz_Hermitiana_PMinima(self):
        self.assertEqual(True,Laboratorio2.matrizHermitiana([[(3,0),(2,-1),(0,-3)],[(2,1),(0,0),(1,-1)],[(0,3),(1,1),(0,0)]]))

    #(16) ¿Es la matriz compleja una matriz hermitiana?
    def test_caso_Matriz_Hermitiana_PMinima1(self):
        self.assertEqual(False,Laboratorio2.matrizHermitiana([[(1,0),(3,-1)],[(3,1),(0,1)]]))

    #(17) Producto tensorial de matrices complejas    
    def test_caso_ProductoTensor(self):
        m=[[(1,0),(2,0)],[(3,0),(4,0)]]
        m1=[[(1,0),(2,0),(3,0)],[(1,0),(2,0),(3,0)],[(1,0),(2,0),(3,0)]]
        self.assertEqual([[(1, 0), (2, 0), (3, 0), (2, 0), (4, 0), (6, 0)], [(1, 0), (2, 0), (3, 0), (2, 0), (4, 0), (6, 0)], [(1, 0), (2, 0), (3, 0), (2, 0), (4, 0), (6, 0)], [(3, 0), (6, 0), (9, 0), (4, 0), (8, 0), (12, 0)], [(3, 0), (6, 0), (9, 0), (4, 0), (8, 0), (12, 0)], [(3, 0), (6, 0), (9, 0), (4, 0), (8, 0), (12, 0)]],Laboratorio2.productoTensorialImaginario(m,m1))

    #(17) Producto tensorial de matrices complejas    
    def test_caso_ProductoTensor_PMinima(self):
        m=[[(1,1),(0,0)],[(1,0),(0,1)]]
        m1=[[(-1,2),(-2,-2),(0,2)],[(2,3),(3,1),(2,2)],[(-2,1),(1,-1),(2,1)]]
        self.assertEqual([[(-3, 1), (0, -4), (-2, 2), (0, 0), (0, 0), (0, 0)], [(-1, 5), (2, 4), (0, 4), (0, 0), (0, 0), (0, 0)], [(-3, -1), (2, 0), (1, 3), (0, 0), (0, 0), (0, 0)], [(-1, 2), (-2, -2), (0, 2), (-2, -1), (2, -2), (-2, 0)], [(2, 3), (3, 1), (2, 2), (-3, 2), (-1, 3), (-2, 2)], [(-2, 1), (1, -1), (2, 1), (-1, -2), (1, 1), (-1, 2)]],Laboratorio2.productoTensorialImaginario(m,m1))
    
        

if __name__ =='__main__':
    unittest.main()
    
