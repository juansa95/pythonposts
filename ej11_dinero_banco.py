# Ejercicio 10 - Tipos de Datos Simples
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
# que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience 
# leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y 
# mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

def run():
    deposito = float(input("Ingrese por favor el dinero a depositar en la cuenta de ahorros: $ "))
    interes = 0.04
    ahorro = deposito + deposito*interes
    print(" El dinero depositeado es : $" + str(round(deposito,2)) + ". El ahorro del primer año es: $" + str(round(ahorro,2)))
    print(" El ahorro del segundo año es: $" + str(round(ahorro * 2,2)) + " y el ahorro del tercer año es: $" + str(round(ahorro,2)))
if __name__ == "__main__":
    run()