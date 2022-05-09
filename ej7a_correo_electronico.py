# Ejercicio 7 - Ejercicio de cadenas
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo 
# electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

def run():
    correo = input("Ingrese su correo electronico por favor: ")
    correo = correo[:correo.find("@")] 
    print(str(correo) + "@ceu.es")
if __name__ == "__main__":
    run()