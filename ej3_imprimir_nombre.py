#Ejercicio 3 - Tipos de Datos Simples
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
#introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/#ejercicio-2

def run():
    nombre = input(" Ingrese su nombre porfavor: ")
    print( "Hola " + str(nombre))
if __name__ == "__main__":
    run()