# construir una funcion que reciba su nombre como parametro y que lo muestre en la pantalla 5 veces 

print("--------------------------------")
print("--DIGITE UN NOMBRE--")
print("--------------------------------")

# definicion de la funcion
def mostrarnombre(nombre):
    """print(f"1. {nombre}")
    print(f"2. {nombre}")
    print(f"3. {nombre}")
    print(f"4. {nombre}")
    print(f"5. {nombre}")"""
    
    for i in range (1,6):
        print(f"{i}. {nombre}")

mostrarnombre("nombre")

