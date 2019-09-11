

def multiplicacionMatrizVector(v1,m1):
    vector = [] 
    for i in range(len(m1)):
        suma = 0
        for j in range(len(m1[i])):
            mult= m1[i][j]*v1[j]
            suma += mult
        vector.append(suma)
    return vector 
    
    
            

def funcionEjercicio1(matriz,vectorI,clicks):
    estado = vectorI
    for i in range(clicks):
        estado = multiplicacionMatrizVector(estado,matriz)
    return estado 
        

matriz = [[0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,0,0,1],[0,0,1,0,0,0],[0,0,0,0,1,0],[1,0,0,0,0,0]]
vector =[6,5,4,3,2,1]

print(funcionEjercicio1(matriz,vector,3000))

def matrizPorEscalar(n,matriz):
    mat = [[0]*len(matriz) for i in range(len(matriz[0]))]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            mat[i][j] = n * matriz[i][j]
    return mat

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

print(productoTensorial([[1,1,1],[1,1,1],[1,1,1]],[[1,0],[1,0]]))
