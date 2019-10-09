# CNYT - CIENCIAS NATURALES Y TECNOLOGIA 
### PROYECTO # 1 Sistemas Dinamicos Clasicos, Probabilisticos y Cuanticos 
### Elaborador por: Daniel Felipe Alfonso Bueno 
### Docente: Sergio Alfonso Tello 
# Contenido 
### Descripcion del Proyecto 
En el proyecto contamos con funciones que nos permitiran ver la dinamica de diferentes sistemas a partir de clicks de tiempo.
Viendo con facilidad el comportamiento de estos sistemas y tratar de ilustrarlos en una grafica para que sea mas facil observar 
los comportamientos que toman los sistemas. 
Tenemos un grupo de funciones complementarias, en donde se encuentran las funciones basicas implementadas los laboratorios anteriores, 
las usaremos para el proyecto

#### Funciones: 

- dinamicaSistemaClasico(clicks) En esta funcion podremos determinar el comportamiento de un sistema clasico de canicas a partir de 
un numero de clicks de tiempo dados 

- sistemaProbabilistico(clicks) En esta funcion se determina el comportamiento de un sistema probabilistico a partir de un numero de 
clicks dados 

### Pruebas 

- Sistema Clasico de Canicas: Para esta prueba tenemos una matriz de dinamica
![img0](https://github.com/DanielAlfonso17/POOB/blob/master/clasico.PNG)

Dada por el siguiente grafo 

![img1](https://github.com/DanielAlfonso17/POOB/blob/master/3.PNG)

y tenemos el siguiente vector inicial: [[10,0],[4,0],[1,0],[7,0],[2,0],[2,0],[11,0],[0,0],[3,0],[1,0],[0,0],[5,0],[2,0]] 
Despues de 25 clicks obtenemos el siguiente resultado en la grafica que concuerda con el resultado pedido en las pruebas 

![img2](https://github.com/DanielAlfonso17/POOB/blob/master/1.PNG)

- Sistema Probabilistico: Para esta prueba tenemos una matriz de probabilidades dada por el siguiente grafo con los dos 
sistemas ensamblados 

![img3](https://github.com/DanielAlfonso17/POOB/blob/master/10.PNG)

Dos matrices para ensamblar los sistemas mediante un producto tensorial que son las siguientes junto con los dos vectores 
de estado inicial 

![img4](https://github.com/DanielAlfonso17/POOB/blob/master/probabilistico.PNG)

Ahora si ejecutamos el nuestro programa despues de 5 clicks de tiempo obtenemos el resultado esperado de probabilidades, que se muestra
en el siguiente grafico 

![img4](https://github.com/DanielAlfonso17/POOB/blob/master/2.PNG)











