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

def accionMatrizSobreVector(v1,m1):
    v = []
    for i in range(len(m1)):    
            v.append(productoVectoresImaginarios(v1,m1[i]))
    return v


def multiplicacionMatrizVector(v1,m1):
    vector = [] 
    for i in range(len(m1)):
        suma = 0
        for j in range(len(m1[i])):
            mult= m1[i][j]*v1[j]
            suma += mult
        vector.append(suma)
    return vector 


def productoTensorial(m1,m2):
    matriz = []
    for i in range(len(m1)):
        matM = [[]] *len(m2)
        for j in range(len(m1[i])):
            m3 = matrizPorEscalar(m1[i][j],m2)
            for k in range(len(m2)):
                matM[k] = matM[k] + m3[k]
        for k in range(len(m2)):
            matriz.append(matM[k])
    return matriz

def vectorPorEscalar(n,vector):
    newVector = []
    for i in range(len(vector)):
        comp = n * vector[i]
        newVector.append(comp)
    return newVector
            
def productoTensorialVectores(v1,v2):
    vFinal = [0 for i in range(len(v1)*len(v2))]
    cont = 0
    for i in range(len(v1)):
        v3 = vectorPorEscalar(v1[i],v2)
        for k in range(len(v3)):
            vFinal[cont] = v3[k]
            cont+=1
    return vFinal
print(productoTensorialVectores([1,0,0,0],[1,0]))
def matrizPorEscalar(n,matriz):
    mat = [[0]*len(matriz) for i in range(len(matriz[0]))]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            mat[i][j] = n * matriz[i][j]
    return mat



def funcionEjercicio1(matriz,vectorI,clicks):
    estado = vectorI
    for i in range(clicks):
        estado = multiplicacionMatrizVector(estado,matriz)
    return estado 
        
def funcionEjercicio2(clicks):
    m1 = productoTensorial([[0,float(1/6),float(5/6)],[float(1/3),float(1/2),float(1/6)],[float(2/3),float(1/3),0]],[[float(1/3),float(2/3)],[float(2/3),float(1/3)]])
    vectorI= productoTensorialVectores([0.01,0.9,0.09],[0.05,0.95])
    estado = vectorI
    for i in range(clicks):
        estado = multiplicacionMatrizVector(estado,m1)
    return estado
def funcionEjercicio3(clicks):
    matriz = [[(0.70,0),(0.70,0),(0,0)],[(0,-0.70),(0,0.70),(0,0)],[(0,0),(0,0),(0,-1)]]
    vector = [(0.57,0),(0,0.51),(0.63,0)]
    for i in range(clicks):
        vector = accionMatrizSobreVector(vector,matriz)
    return vector

print(funcionEjercicio3(4))
matriz = [[0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,0,0,1],[0,0,1,0,0,0],[0,0,0,0,1,0],[1,0,0,0,0,0]]
vector =[6,5,4,3,2,1]

vectorPosI = [0.01,0.9,0.09]
vectorPerI = [0.05,0.95]
print(funcionEjercicio2(900))
#print(funcionEjercicio1(matriz,vector,3000))






