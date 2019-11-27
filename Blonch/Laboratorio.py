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
    if denominador == (0,0):
        return "Division por cero no valida" 
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
    res = radianesAGrados(angulo)
    return res
        
def deCartesianoAPolar(c1):
    mod = moduloImaginario(c1)
    fase = faseComplejos(c1)
    return (round(mod,2),round(fase,2))
    
def dePolarACartesiano(c1):
    return ((round(((c1[0]*math.cos(math.radians(c1[1]))*1000)/(1000)),2),round(((1000*c1[0]*math.sin(math.radians(c1[1])))/1000),2)))

