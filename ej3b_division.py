# Ejercicio 3 - Ejercicio de condicionales
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero 
# el programa debe mostrar un error.

def run():
    numero_uno = int(input("Ingrese el primer numero por favor: "))
    numero_dos = int(input("Ingrese el segundo numero por favor: "))
    division = numero_uno // numero_dos
    print(str(numero_uno) + " / " + str(numero_dos) + " = " + str(division))
    if numero_uno % numero_dos == 0:
        print("error")
if __name__ == "__main__":
    run()