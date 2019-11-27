from Laboratorio import *
from Laboratorio2 import * 
import math

def esferaBlonch(ket1,ket2):
    vector = [ket1,ket2]
    for i in vector:
        modFase= deCartesianoAPolar(i)
        r = modFase[0]
        alpha = modFase[1]
        print(modFase)
        a = r*math.cos(alpha)
        b = r*math.sin(alpha)
    
esferaBlonch([1,0],[0,1])
