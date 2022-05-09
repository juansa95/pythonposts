# Ejercicio 2 - Ejercicio de condicionales
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e 
# imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta 
# mayúsculas y minúsculas.

def run():
    contraseña = "contraseña"
    contraseña_usuario = input("Ingrese la contraseña por favor: ")
    contraseña_usuario = contraseña_usuario.lower()
    if contraseña == contraseña_usuario:
        print("La contraseña coincide")
    else:
        print("La contraseña no coicide")
if __name__ == "__main__":
    run()