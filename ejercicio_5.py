import random

print("-----------------------------------------")
print("-----MOSTRAR CADENA N VECES EN-----------")
print("---------------PANTAllA------------------")
print("-----------------------------------------")


def calcular_promedio_pares(lista):
    suma = 0
    contador = 0  # Renamed variable from 'count' to 'contador'
    for i in lista:
        if i % 2 == 0:
            suma += i
            contador += 1
    if contador == 0:
        return 0  
    promedio = suma / contador
    return promedio


# Lista vacía
lista = []

# Tamaño de la lista
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(14, 18)
    lista.append(num)

# Procesamiento
print("Lista : ", lista)
print("El promedio de los datos pares es: ", calcular_promedio_pares(lista))

