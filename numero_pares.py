#Numeros pares del 1 al 50

def run():
    contador = 0
    for contador in range (50):
        contador = contador +1
        if contador % 2 == 0: 
            print(contador)
if __name__ == "__main__":
    run()