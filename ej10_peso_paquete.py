# Ejercicio 10 - Tipos de Datos Simples
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística 
# les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
# y calcule el peso total del paquete que será enviado.

def run():
    peso_payaso = 112
    peso_muneca = 75
    cant_payaso = int(input("Ingrese por favor el numero de payasos a comprar: "))
    cant_muneca = int(input("Ingrese por favor el numero de munecas a comprar: "))
    total_payaso = peso_payaso * cant_payaso
    total_muneca = peso_muneca * cant_muneca

    print("En el ultimo pedido se vendieron " + str(cant_payaso) + " payasos y " + str(cant_muneca) + " muñecas. El peso total del pesiso es: " + str(total_payaso + total_muneca) + " g")
if __name__ == "__main__":
    run()