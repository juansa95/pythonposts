# Ejercicio 9 - Tipos de Datos Simples
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.

def run():
    inversion = int(input("Ingrese por favor cuanto dinero quiere invertir: $ "))
    interes_anual = float(input("Ingrese por favor cuál es el interés anual: "))
    tiempo = int(input("Ingrese por favor cuántos años desea dejar el dinero: "))
    capital = inversion * ( interes_anual / 100 + 1 )** tiempo
    print(" El capital obtenido es: $" + str(float(round(capital,2))))
if __name__ == "__main__":
    run()
