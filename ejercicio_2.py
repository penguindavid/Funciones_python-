# construir una funcion que reciba una cadena digitada(como parametro)por el usuario y que lo muestre n veces en la pantalla. el valor n tambien es digitado por el usuario

print("-----------------------------------------")
print("-----MOSTRAR CADENA N VECES EN-----------")
print("---------------PANTAllA------------------")
print("-----------------------------------------")

# definicion de la funcion 
def mostrarnombre(cadena, n):
    pass
    for _ in range(n):
        print(cadena)

cadena = input("Por favor, introduce una cadena: ")
n = int(input("¿Cuántas veces deseas mostrar la cadena?: "))

# Llamar a la función
mostrarnombre(cadena, n)
