# Ejercicio 8 - Tipos de Datos Simples
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> 
# y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la 
# división entera respectivamente.

def run():
    a = int(input("Ingrese el primer numero por favor: "))
    b = int(input("Ingrese el segundo numero por favor: "))
    cociente = a // b
    resto = a % b
    print (" El cociente de la división es: " + str(float(cociente)) + " y el resto es: " + str(float(resto)))
if __name__ == "__main__":
    run()