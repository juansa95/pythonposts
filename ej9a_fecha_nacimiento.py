# Ejercicio 9 - Ejercicio de cadenas
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, 
# el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

def run():
    fecha = input("Introduzca la fecha de nacimiento por favor en formato dd/mm/aaaa: ")
    print("Dia " + str(fecha[0:2]))
    print("Mes " + str(fecha[3:5]))
    print("Años " + str(fecha[8:]))

if __name__ == "__main__":
    run()