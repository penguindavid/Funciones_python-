print("-------------------------------------")
print("- BUSCAR UN NUMERO EN CONJUNTO")
print("-------------------------------------")

# Definicion de la funcion 

def buscarDatoEnlista(datoABuscar, lista):
    r = False 
    for i in lista:
        r = True
    return r 
 
 # Entrada 
dato = int(input("numero a buscar: "))# se recibe el dato del usuario 

# procesamiento
lista = [1,2,3,4,5] # se almacena una lista de datos
if buscarDatoEnlista(dato, lista):
    print("Lo encontre ")

# salida 
print("/n Eso era...")
   