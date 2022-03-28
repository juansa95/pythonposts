#Ejercicio 5 - Tipos de Datos Simples
#Escribir un programa que pregunte al usuario por el número de horas trabajadas 
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

def run():
    horas_trabajadas = float(input("Ingrese por favor el numero de horas trabajadas: "))
    costo_horas = float(input("Ingrese por favor el valor de hora trabajada: $ "))
    pago = horas_trabajadas * costo_horas

    print(" El pago correspondiente a " + str(horas_trabajadas) + " horas trabajadas, es de: $ " + str(pago))

if __name__ == "__main__":
    run()