# Ejercicio 5 - Ejercicio de cadenas
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

def run():
    frase = input("Ingrese una frase por favor: ")
    print(frase[::-1])
if __name__ == "__main__":
    run()