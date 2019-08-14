import unittest
import math 
def sumaImaginarios(c1,c2):
    c3 = [0,0]
    c3[0] = c1[0] + c2[0]
    c3[1] = c1[1] + c2[1]
    return c3

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
    return res
        
def restaImaginarios(c1,c2):
    c3 = [0,0]
    c2[0] = (-1*c2[0])
    c2[1] = (-1*c2[1])
    c3[0] = c1[0] + c2[0]
    c3[1] = c1[1] + c2[1]
    return c3

def moduloImaginario(c1):
    modulo = (c1[0]**2+c1[1]**2)**(1/2)
    return modulo

def conjugadoImaginario(c1):
    c3 = [0,0]
    c3[0] = c1[0]
    c3[1] = (-1*c1[1])
    return c3

def divisionImaginarios(c1,c2):
    conjugado = conjugadoImaginario(c2)
    numerador = productoImaginarios(c1,conjugado)
    denominador = productoImaginarios(c2,conjugado)
    res = [0,0]
    res[0] = numerador[0] / denominador[0]
    res[1] = numerador[1] / denominador[0]
    return res

def deCartesianoAPolar(c1):
    r = moduloImaginario(c1)
    a = c1[0]
    b = c1[1] 
    alfa = math.atan(b/a)
    return r,alfa
    
    
c1 = [8,2]
c2 = [-9,-12]

print(deCartesianoAPolar(c1))
