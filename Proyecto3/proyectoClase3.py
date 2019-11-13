import math
from Laboratorio import *
from Laboratorio2 import *
from tallerClase import *
from Proyecto import *
matrizCero = [[(1,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(1,0),(0,0)],[(0,0),(0,0),(0,0),(1,0)]]
matrizCeroUno = [[(1,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(1,0)],[(0,0),(0,0),(1,0),(0,0)]]
matrizUno = [[(0,0),(1,0),(0,0),(0,0)],[(1,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(1,0)],[(0,0),(0,0),(1,0),(0,0)]]
matrizUnoCero = [[(0,0),(1,0),(0,0),(0,0)],[(1,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(1,0),(1,0)]]
Uno = [(0,0),(1,0)]
Cero = [(1,0),(0,0)]
matrizHadamard = [[(1/(2**(1/2)),0),(1/(2**(1/2)),0)],[(1/(2**(1/2)),0),(-(1/(2**(1/2))),0)]]
matrizIdentidad = [[(1,0),(0,0)],[(0,0),(1,0)]] 

def simulacionAlgoritmoDeutsch():
    phiCero = productoTensorialVectores(Cero,Uno)
    HH = productoTensorial(matrizHadamard,matrizHadamard)
    phiUno = accionMatrizSobreVector(phiCero,HH)
    phiDos = accionMatrizSobreVector(phiUno,matrizCero)
    HI = productoTensorial(matrizHadamard,matrizIdentidad)
    phiTres = accionMatrizSobreVector(phiDos,HI)
    for i in phiTres:
        print(moduloImaginario(i)**2)
    
    
    
simulacionAlgoritmoDeutsch()
    
