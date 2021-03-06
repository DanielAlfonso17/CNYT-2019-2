
#----------------------------FUNCIONES REQUERIDAS---------------------------
def normaVectorImaginario(v1):
    suma =0
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            suma += ((v1[i][j])**2)
    return suma**(1/2)

def normaImaginario(c1):
    suma = 0
    suma = (c1[0]**2) +(c1[1]**2)
    return suma

def accionMatrizSobreVector(v1,m1):
    v = []
    for i in range(len(m1)):    
            v.append(productoVectoresImaginarios(v1,m1[i]))
    return v

def productoVectoresImaginarios(c1,c2):
    ini = (0,0)
    for i in range(len(c1)):
        suma = productoImaginarios(c1[i],c2[i])
        ini = sumaImaginarios(ini,suma)
    return ini

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

def multiplicacionEscalarVector(c1,v1):
    res = []
    for i in range(len(v1)):
        res.append(productoImaginarios(c1,v1[i]))
    return res

#(7) Transpuesta de matriz compleja
def matrizTranspuesta(m1):
    matriz=[]
    for i in range(0,len(m1[0])):
        columna = [row[i] for row in m1]
        matriz.append(columna)
    return matriz 
        
#(8) Conjugada de matriz compleja        
def matrizConjugada(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0],m1[i][j][1]*-1))
        matriz.append(vector)
    return matriz
#(9) Adjunta (daga) de matriz compleja

def matrizAdjunta(m1):
    matriz=matrizTranspuesta(m1)
    matriz=matrizConjugada(matriz)
    return matriz

def normalizacion(v1):
    normaVector = normaVectorImaginario(v1)
    vector = []

    vectorN=multiplicacionEscalarVector((1/normaVector,0),v1)
    return vectorN
        
def productoMatricesImaginarias(m1,m2):
    matriz = [[None] * len(m2[0]) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            columna = [row[j] for row in m2]
            matriz[i][j] = productoVectoresImaginarios(m1[i],columna)
    return matriz
    
#--------------------------------PROYECTO------------------------------------
def particulaLineaRecta(v1):
    probabilidad=[]
    normaVectorCuadrado = (normaVectorImaginario(v1))**2
    print("Vector de estado Inicial:",v1)

    for i in v1:
        j =(normaImaginario(i))/normaVectorCuadrado
        probabilidad.append(round(((normaImaginario(i))/normaVectorCuadrado),4))
    
    return probabilidad


    

v1=[[2, -1],
 [-1.5, 2.5],
 [-3.5, 5],
 [-4, 6],
 [-3.5, 2.5],
 [0, 0],
 [-3.5, 2.5],
 [6, -4],
 [0, 2.5],
 [-1, 1]]
print("-------------------------Prueba Particula Linea Recta-------------------------")
print("Parametro v1 Vector de estado Inicial" )
print("Vector de probabilidades calculado:",particulaLineaRecta(v1))

def calculadoraEstadisticaObservables(m1,v1):    
    vectorNormalizado=normalizacion(v1)
    vEncapsulado=[]
    for i in vectorNormalizado:
        vEncapsulado.append([i])
    vector = productoMatricesImaginarias(m1,vEncapsulado)
    adjuntaVector=matrizAdjunta(vector);
    productoAdjuntaVector= productoMatricesImaginarias(adjuntaVector,vEncapsulado)
    print("Valor Esperado:",round(productoAdjuntaVector[0][0][0],2))
    valorEsperado=productoAdjuntaVector[0][0][0]
    calculoVarianza=[[[valorEsperado,0],[0,0],[0,0],[0,0]],[[0,0],[valorEsperado,0],[0,0],[0,0]],[[0,0],[0,0],[valorEsperado,0],[0,0]],[[0,0],[0,0],[0,0],[valorEsperado,0]]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j][0]=m1[i][j][0]-calculoVarianza[i][j][0]
    matrizCuadrado=productoMatricesImaginarias(m1,m1)
    adjuntaVectorInicial=matrizAdjunta(vEncapsulado)
    matx=productoMatricesImaginarias(adjuntaVectorInicial,matrizCuadrado)
    varianza=productoMatricesImaginarias(matx,vEncapsulado)
    print("Varianza:",varianza[0][0][0])


    
m1 = [[[0,0],[0,-1/2],[0,-1],[-7/2,0]],
 [[0,1/2],[0,0],[7/2,0],[0,-1]],
 [[0,1],[7/2,0],[0,0],[0,-1/2]],
 [[-7/2,0],[0,1],[0,1/2],[0,0]]
]


vI= [[-2, 1],
 [1, 0],
 [0,-1],
 [3,2]
]
print("------------------Prueba Calculadora Estadistica Observables------------------")
print("-------Valor Esperado -------------------Varianza-----------------------------")
print("Parametro m1 matriz correspondiente al observable y v1 Vector de estado Inicial")
calculadoraEstadisticaObservables(m1,vI)


