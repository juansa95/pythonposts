# Ejercicio 4 - Ejercicio de condicionales
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def run():
    numero = int(input("Ingrese un numero entero por favor: "))
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
if __name__ == "__main__":
    run()