# Ejercicio 1 - Ejercicio de condicionales
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def run():
    edad = int(input("Ingrese su edad por favor: "))
    if edad >= 18:
        print(" Es mayor de edad")
    else:
        print("No es mayor de edad")
if __name__ == "__main__":
    run()