# Ejercicio 1 - Ejercicio de cadenas
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas 
# el nombre del usuario tantas veces como el número introducido.

def run():
    nombre = input("Cuál es su nombre?: ")
    entero = int(input("Escriba un numero entero: "))
    for i in range(0,entero):
        print(nombre)
if __name__ == "__main__":
    run()