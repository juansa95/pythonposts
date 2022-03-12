#Programa que recibe número y lo transforma en binario

def run():
    numero_decimal = int(input("Escribe un numero decimal: "))
    binario =" "
    while numero_decimal > 0:
        numero_decimal = numero_decimal // 2
        residuo = numero_decimal % 2
        binario = binario +  str(residuo)
    print(binario)

if __name__ == "__main__":
    run()