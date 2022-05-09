# Ejercicio 8 - Ejercicio de cadenas
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla 
# el número de euros y el número de céntimos del precio introducido.

def run():
    precio = input["Cuál es el precio de un producto en euros con dos decimales: ")
    centimos = precio[precio.find(".")+1:]
    precio = precio[:precio.find(".")]
    print("El numero de euros es " + str(precio) + " y el numero de centimos es: " + str(centimos))
if __name__ == "__main__":
    run()