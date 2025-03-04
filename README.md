# Sobrecarga de Metodos 
## Descripcion general 🚀
Para comenzar debemos saber que en una sobrecarga en la pogramacion orientada a objetos, se podria decir que es la posibilidad de tener varios métodos o funciones con el mismo nombre, pero con diferentes funcionalidades. En este proyecto se pondra en practica dicha sobrecargar con ejemplos sencillos. 
## Explicacion de primer ejemplo
Tenemos 3 archivos: "vector.py" es el encargado de calcular la norma de un vector. Se crea la clase Vector con el metodo
```
calculo_norma
```

Este metodo recibe un parametro vector que permite segun la ejecucion de su uso saber que dimension tendra es por ello que importamos la libreria
```
import numpy as np
```

Esta contiene una funcion que hace el calculo de cualquier norma de un vector o una matriz (y otros calculos que no se incluyen en este ejemplo) para un dimension que como se dijo previamente la define quien la necesite y con que proposito de calculo, en este caso la utilizaremos para el calcular la norma de un vector 2D y 3D.
```
np.linalg.norm()
```
## Explicacion segundo ejemplo
"transformador.py" en ella definimos una clase Transformador con un metodo:
```
transformar
```
La cual hace una suma de un lista de numero y esa misma la multiplica por un factor, todo definido por el usuario. Y asi retornamos:
```
return suma,resultado
```
Que nos devuelve tanto la suma como la multiplicacion de la lista. 

## Ejecutando las pruebas ⚙️
## Primer ejemplo
En nuestro archivo "main.py" que vendria siendo nuestro archivo principal 
importamos las clases (recuerda que estan en archivos separados): 
```
from vector import Vector
from transformador import Transformador
```
Asi podremos utilizarlas en nuestro programa. Creamos una funcion para limpiar la terminal de ejecusion y no se vea todo colapsado
```
def limpiar_pantalla():
      os.system('cls' if os.name == 'nt' else 'clear')
```
La llamaremos cada vez que sea conveniente limpiar la terminal. 
Ahora bien colocamos:
```
while True:
```
Para hacer que el programa se repita hasta el usuario decida salir. 
colocamos un menu que contiene el uso de nuestras diferentes funciones
```
opc=int(input("1: CALCULO NORMA DE UN VECTOR 2D \n2: CALCULO NORMAL DE UN VECTOR 3D \n3: SUMA DE UNA LISTA DE NUMEROS Y MULTIPLICARLOS POR EL NUMERO QUE ESCOJAS\n4:Salir\n" ))
```
En la opcion 1 Calcularemos la norma de un vector 2D solicitamos los datos correspondientes para hacer el calculo instanciamos nuestra clase, le pasamos los parametros recibidos 
```
vector=[v0,v1]
        norma=Vector().calculo_norma(vector)
        print(f"La norma del vector {v0} y {v1} es {norma}")

```
Se hace el calculo y deberia aparecer un salida similar (todo depende de los numero que ingrese el usuario) a esta:
```
1: CALCULO NORMA DE UN VECTOR 2D
Ingresa primer valor
3
Ingresa segundo valor
4
La norma del vector 3 y 4 es 5.0
```
En el caso de la opcion 2 es un muy similar utilizamos el mismo metodo solo cambia que solicitan 3 valores y la salida:
```
vector=[v0,v1,v2]
        norma=Vector().calculo_norma(vector)
        print(f"La norma del vector {v0} , {v1} y {v2} es {norma}")
```
Se le pasan 3 valores a la funcion ya que es un vector 3D y deberia verse asi: 
```
2: CALCULO NORMA DE UN VECTOR 3D
Ingresa primer valor
3
Ingresa segundo valor
4
Ing tercer valor
5
La norma del vector 3 , 4 y 5 es 7.0710678118654755
```
Recuerda que varia en el calculo, ya que puedes ingresar varios numeros para probar su funcionalidad. 
## Segundo ejemplo
Aqui utilizamos nuestra clase Transformador se emplea un:
```
while True:
```
Para que se repita hasta que el usuario escriba "fin" en la terminal y asi obtener una lista de numeros la cual sumaremos
```
try:
   lista.append(float(entrada))
 except ValueError:
    print("Entrada inválida. Ingresa un valor escribe la palabra o 'fin'.")
```
Con esto verificamos que el usuario no se equivoque e ingrese una entrada invalida. Y tambien vamos agregando los numeros ingresados a nuestra lista, pidiendo el factor multiplicador. 
Y ahora instanciamos y le pasamos los parametros recibido:
```
suma, resultado = Transformador().transformar(lista, x)
        print(f"La suma de tu lista {lista} es {suma}, y multiplicado por {x} es {resultado}")
```
La salida deberia verse asi (siempre recuerda que el calculo cambia dependiendo de lo que se ingrese):
```
3: SUMA DE UNA LISTA DE NUMEROS Y MULTIPLICARLOS POR EL NUMERO QUE ESCOJAS

Ingresa un valor o escribe la palabra 'fin' para terminar 1
Ingresa un valor o escribe la palabra 'fin' para terminar 2
Ingresa un valor o escribe la palabra 'fin' para terminar 3
Ingresa un valor o escribe la palabra 'fin' para terminar fin
Ingresa por qué número quieres multiplicar tu lista: 2
La suma de tu lista [1.0, 2.0, 3.0] es 6.0, y multiplicado por 2 es 12.0
```
Por ultimo queda la salida del programa como tal, en ella se pregunta si se desea salir, si la respuesta es si, sale del programa, si se responde no, se vuelve a repetir el ciclo hasta que decidamos salir. 

## Autora✒️
Norkys Peña 
## Gratitud 🎁
Si deseas apoyar siguenos y comenta por alguna duda. 
Aceptamos donaciones $$ 🤑
