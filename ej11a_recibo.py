# Ejercicio 11 - Ejercicio de cadenas
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla 
# una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades 
# con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

def run():
    nombre = input("Ingrese por favor el nombre del producto: ")
    precio = float(input("Ingrese por favor el precio del producto con 2 decimales: "))
    unidades = int(input("Ingrese por favor las unidades del producto: "))
    precio_total = precio * unidades
    print(str(nombre) + "\n" + str(unidades) + "\n" + str(float(round(precio,2))) + "\n"+  str(precio_total))
if __name__ == "__main__":
    run()