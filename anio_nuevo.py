# Programa que haga conteo hasta que se aaño nuevo"

def cuenta_regresiva(num):
    num = num - 1

    if num >= 0:
        print(num)
        cuenta_regresiva(num)
    else:
        print("Feliz año nuevo")
cuenta_regresiva(15)