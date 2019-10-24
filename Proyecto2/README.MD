# CNYT - CIENCIAS NATURALES Y TECNOLOGIA 
### PROYECTO # 2 Teoria Cuantica Basica
### Elaborador por: Daniel Felipe Alfonso Bueno 
### Docente: Sergio Alfonso Tello 
# Contenido 
### Descripcion del Proyecto 
En este proyecto podremos encontrar funciones con las cuales entenderemos con mayor facilidad la dinamica de un sistema cuantico, utilizando operaciones
para calcular las probabilidades o estados en las que puede estar dicho sistema cuantico dependiendo de su vector inicial. Ademas del papel fundamental
que juega la varianza para conocer la distribución a su valor esperado. 
#### Funciones: 
- particulaLineaRecta(v1) En esta funcion calcularemos un vector de probabilidades de todos los estados las cuales indican, la probabilidad de tomar un estado dado un
vector de estado inicial v1 

- calculadoraEstadisticaObservables(m1,v1) En esta funcion calcularemos la varianza y el valor esperado en un sistema cuantico definido por una matriz m1
y un vector de estado inicial v1

### Pruebas 
(1) Partícula en una recta.Esta funcion recibe como parametro un vector de estado inicial que es el siguiente: 

![img0](https://github.com/DanielAlfonso17/POOB/blob/master/vectorInicial.JPG)

Procedemos a calcular el vector de probabilidades, primero calculando la norma de nuestro vector de estado inicial, despues por cada estado 
aplicamos la norma de numero complejo al cuadrado dividido la normal al cuadrado  del vector inicial y esto lo añadimos a nuestro vector de probabilidades

![img0](https://github.com/DanielAlfonso17/POOB/blob/master/formulaProb.JPG)

Obteniendo como resultado el vector de probabilidad siguiente

![img0](https://github.com/DanielAlfonso17/POOB/blob/master/pruebaUno.JPG)

Comparando nuestro resultado con las pruebas dadas obtenemos un resultado correcto 

![img0](https://github.com/DanielAlfonso17/POOB/blob/master/vectorProbabi.JPG)

(2) Calculadora estadística para observables Esta funcion rebice como parametros un vector de estado inicial y una matriz los cuales son los 
siguientes 

![img0](https://github.com/DanielAlfonso17/POOB/blob/master/matrizDos.JPG)
![img0](https://github.com/DanielAlfonso17/POOB/blob/master/vectorDos.JPG)

Procedemos a normalizar nuestro vector de estado inicial, para despues hacer un producto de matrices entre nuestro vector normalizado 
y la matriz que tenemos, calculamos la adjunta de este resultado, para posteriormente realizar el producto entre el vector adjunto y nuestro
vector normalizado para obtener nuestro valor esperado. Posteriormente para calcular la varianza realizamos nuestra matriz identidad con el 
valor esperado en la diagonal. Le restamos a nuestra matriz original la matriz identidad con el valor esperado. Elevamos nuestra matriz al cuadrado
calculamos la adjunta del vector inicial normalizado, realizamos un producto entre la adjunta del vector inicial y nuestra matriz con la resta 
de la identidad y finalmente para obtener la varianza multiplicamos el resultado que obtuvimos anteriormente con el vector normalizado 
obtendremos correctamente el resultado siguiente: 

![img0](https://github.com/DanielAlfonso17/POOB/blob/master/varyvalor.JPG)

![img0](https://github.com/DanielAlfonso17/POOB/blob/master/pruebaDos.JPG)




