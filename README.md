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
Que nos devuelve tanto la suma como la resta. 

## Ejecutando las pruebas ⚙️
En nuestro archivo "main.py" que vendria siendo nuestro archivo principal 

