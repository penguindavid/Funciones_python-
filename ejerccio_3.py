# ejercicio 3 

import random

print("-----------------------------------------")
print("-----MOSTRAR CADENA N VECES EN-----------")
print("---------------PANTAllA------------------")
print("-----------------------------------------")


def calcular_promedio_lista(lista):
    suma = 0
    for i in lista:
        suma = suma + i 
    return suma


# lista vacia
lista = []

# tamaño de la lista
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(14, 18)
    lista.append(num)

# procesamiento 
print("lista : ", lista  )
print("El promedio de la lista es: ", calcular_promedio_lista(lista))





