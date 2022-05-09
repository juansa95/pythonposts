# Ejercicio 12 - Tipos de Datos Simples
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa 
# que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una 
# barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

def run():
    costo_barra = 3.49
    descuento = 0.6
    barras = int(input("Ingrese por favor el numero de barras vendidas que no son del dia: "))
    print("El precio habitual del pan es: $" + str(round(costo_barra * barras,2)) + ", el descuento que se le hace es: $ " + str(round(barras*descuento,2)) + " y el coste final es : $" + str(round(costo_barra*barras-descuento*barras,2)))
if __name__ == "__main__":
    run()