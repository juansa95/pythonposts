# Ejercicio 5 - Ejercicio de condicionales
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 $ mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def run():
    edad = int(input("Ingrese su edad por favor: "))
    ingresos = float(input("Cuales son sus ingresos:$ "))
    if edad > 16 and ingresos >= 1000:
        print ("El ususario debe tributar")
    else:
        print ("El usuario no debe tributar")
if __name__ == "__main__":
    run()