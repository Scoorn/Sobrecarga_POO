#Importamos las clases con sus metodos en un programa principal para hacer uso de ellas
from vector import Vector
from transformador import Transformador
#Importamos la libreria os para limpiar pantalla y todo se observe mejor
import os

#Creamos una metodo para limpiar 
def limpiar_pantalla():
      os.system('cls' if os.name == 'nt' else 'clear')

while True:
    #Se crean varios caso para determinar lo que desea hacer el usuario y usar las clases que se crearon previamente
    print(":::::::::: BIENVENIDO AL PROGRAMA ::::::::::\n")
    print("Ing que opcion desea realizar \n")
    opc=int(input("1: CALCULO NORMA DE UN VECTOR 2D \n2: CALCULO NORMAL DE UN VECTOR 3D \n3: SUMA DE UNA LISTA DE NUMEROS Y MULTIPLICARLOS POR EL NUMERO QUE ESCOJAS\n4:Salir\n" ))

    
    if opc ==1:
        limpiar_pantalla()
        print("1: CALCULO NORMA DE UN VECTOR 2D")
        v0=int(input("Ingresa primer valor\n"))
        v1=int(input("Ingresa segundo valor\n"))
        vector=[v0,v1]
        norma=Vector().calculo_norma(vector)
        print(f"La norma del vector {v0} y {v1} es {norma}")

    elif opc==2:
        limpiar_pantalla()
        print("2: CALCULO NORMA DE UN VECTOR 3D")
        v0=int(input("Ingresa primer valor\n"))
        v1=int(input("Ingresa segundo valor\n"))
        v2=int(input("Ing tercer valor\n"))
        vector=[v0,v1,v2]
        norma=Vector().calculo_norma(vector)
        print(f"La norma del vector {v0} , {v1} y {v2} es {norma}")

    elif opc==3:
        limpiar_pantalla()
        print("3: SUMA DE UNA LISTA DE NUMEROS Y MULTIPLICARLOS POR EL NUMERO QUE ESCOJAS\n")
        lista=[]
        while True:
            entrada = input("Ingresa un valor o escribe la palabra 'fin' para terminar ")
            if entrada.lower() == 'fin':
                break
            try:
                lista.append(float(entrada))
            except ValueError:
             print("Entrada inválida. Ingresa un valor escribe la palabra o 'fin'.")
             
        x = int(input("Ingresa por qué número quieres multiplicar tu lista: "))
        suma, resultado = Transformador().transformar(lista, x)
        print(f"La suma de tu lista {lista} es {suma}, y multiplicado por {x} es {resultado}")
        
    elif opc==4:
        limpiar_pantalla()
        salir=input("¿Seguro que desea salir? \n")
        if salir.lower()=='si':
            break
     

        