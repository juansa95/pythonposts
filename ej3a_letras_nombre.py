# Ejercicio 3 - Ejercicio de cadenas
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre 
# por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que 
# tienen el nombre.

def run():
    nombre = input("Ingrese por favor su nombre: ")
    letras = 0
    for n in nombre:
        letras = letras +1
    print("El nombre " + str(nombre.upper()) + " tiene " + str(letras) + " letras")
if __name__ == "__main__":
    run()