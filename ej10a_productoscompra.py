#Ejercicio 10 - Ejercicio de cadenas
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
# y muestre por pantalla cada uno de los productos en una línea distinta.

def run():
    compras = input("Ingrese los productos de una cesta de la compra, separados por comas por favor: ")
    compras = compras.replace("," , "\n")
    print(compras)
if __name__ == "__main__":
    run()