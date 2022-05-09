# Ejercicio 6 - Ejercicio de cadenas
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

def run():
    frase = input("Introduce una frase por favor: ")
    vocal = input("intruce una vocal por favor: ")
    frase = frase.replace(vocal,vocal.upper())
    print(str(frase))
if __name__ == "__main__":
    run()