#Programa que recibe dos catetos y calcula la hipotenusa

def run():
    cateto_a= int(input("Ingrese cateto a porfavor: "))
    cateto_b= int(input("Ingrese cateto b porfavor: "))
    hipotenusa = (cateto_a ** 2 + cateto_b ** 2)**(1/2)
    print( "La hipotenusa es: " + str(hipotenusa))

if __name__ == "__main__":
    run()