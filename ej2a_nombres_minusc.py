# Ejercicio 2 - Ejercicio de cadenas
#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre 
# completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la 
# primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas 
# como quiera.

def run():
    nombre = input("Escriba su nombre en minsucula o mayuscula por favor: ")
    print (nombre.lower())
    print (nombre.upper())
    print (nombre.title())
if __name__ == "__main__":
    run()