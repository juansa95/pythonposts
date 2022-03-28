#Ejercicio 6 - Tipos de Datos Simples
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y 
# lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el 
# índice de masa corporal calculado redondeado con dos decimales.

def run():
    peso = float(input(" Ingrese su peso en kg por favor: "))
    estatura = float(input(" Ingrese su estatura en cm por favor: "))
    indice_masa_corporal = peso / (estatura/100 * estatura/100)
    print ("Su Indice de mas corporal imc es : " + str(round(indice_masa_corporal,2)))
if __name__ == "__main__":
    run()
