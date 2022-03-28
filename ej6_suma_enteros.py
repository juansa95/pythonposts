#Ejercicio 6 - Tipos de Datos Simples
#Escribir un programa que lea un entero positivo n, introducido por el usuario y después muestre en pantalla la suma de 
# todos los enteros desde 1 hasta n. La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:

def run():
    numero_entero = int(input("Ingrese un numero entero positivo por favor : "))
    sumatoria = 0
    for valor in range(1, numero_entero + 1, 1):
        sumatoria = sumatoria + valor
    print(sumatoria)
if __name__ == "__main__":
    run()