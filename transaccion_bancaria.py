# Tenemos un banco de cliente, cuenta de cliente, y cliente tiene saldo en su cuenta y quiere hacer transferencia a banco de destino, a una cuenta de destino.
# Con hoirarios de tranferencia 0-24 h, quiero transferiri $1M, pero hay condiciones
# cliente debe ser verificado (True o falso), destino verificado, saldo > monto a transferir + costo transacción
# Parametros de transacción, banco a banco iguual = 0 y si banco son diferentes costo 100USD
# Solo s epueden hacer transferencias de 9 a 12 o 15 a 20

def run():
    def banco_destino():
        banco_destino = str(input("Ingrese el nombre del banco de destino: "))
        return True
    def cuenta_destino(): 
        cuenta_destino = int(input("Ingrese numero de cuenta de cliente: "))
        return True

    banco_cliente = str(input("Ingrese el nombre del banco del cliente: "))
    cuenta_cliente = int(input("Ingrese numero de cuenta de cliente: "))
    saldo = int(input("Ingrese el dinero que tiene en su cuenta bancaria: $"))
    transf = int(input("Cuanto dinero quieres transferir: $"))
    valor_transaccion = 0
  
    hora_transf = int(input("Ingrese la hora de la transferencia de 0 a 24 horas: "))
    if hora_transf >= 9 and hora_transf <= 12 or hora_transf >= 15 and hora_transf <= 20:
        print(" Horario permitido de transferencia")
        if banco_destino() == True and cuenta_destino() == True:
            print(" Cliente destino y cuenta destino verificados")
            if banco_cliente == banco_destino:
                valor_transaccion = 0
                if saldo > (valor_transaccion + transf):
                    saldo = saldo - valor_transaccion - transf
                    print( "Se ha transferido $" + str(transf) + " a la cuenta cliente # " + str(cuenta_cliente) + "." + " y te queda un saldo de: $" + str(saldo))
                else:
                    print (" No se tiene el saldo suficiente")
            else:
                valor_transaccion = 100
                if saldo > (valor_transaccion + transf):
                    saldo = saldo - valor_transaccion - transf
                    print( "Se ha transferido $" + str(transf) + " a la cuenta cliente # " + str(cuenta_cliente)+ "." + " y te queda un saldo de: $" + str(saldo))
                else:
                    print (" No se tiene el saldo suficiente")
        else:
            print ("Cliente destino o cuenta destino no verificados")
    else:
        print ("Transferencia afuera del horario permitido")
            
if __name__ == "__main__":
    run()