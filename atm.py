#Time
import datetime
now = datetime.datetime.now()
import time
import sys

#Barra de progreso
def progress():
    for i in range(101):
        time.sleep(0.02)
        sys.stdout.write("...\r%d%%" % i)
        sys.stdout.flush()

#Variables
names = ["Alvaro", "Cecilia", "Caro", "Ulises"]
completeNames = ["Alvaro Martinez", "Ana Cecilia Castro", "Carolina Rodriguez.","Ulises Cruz Miranda"]
password = [2222,3333,4444,5555]
saldo = [5000.00,4000.00,3000.00,10000.00]
numberUser = 0

#Display Menu
def displayMenu():
    print ("-")*50
    print ("\tATM Banco del Emprendimiento")
    print "\t*Recuerda no usar acentos*"
    print ("-")*50
    print now.strftime("Hoy es %A, %d, de %B de %Y y son las %H:%M")
    userLog()

#Esta funcion es para terminar el programa
def bye():
    print "\nAdios. Gracias por usar el Banco del Emprendimiento"
    print ("\n") * 3
    exit()

#Esta funcion es para salir
def salir():
    salir = raw_input("Deseas realizar otra operacion?: Escribe (si/no) :")
    if salir == "no":
        bye()
    elif salir == "si":
        main()

#Esta funcion es para consultar el saldo
def consultar():
    global saldo
    print ("-")*50
    print "\t C O N S U L T A R  S A L D O"
    print ("-")*50
    print "Tu saldo es de: $", saldo, "al", now.strftime("%A, %d, de %B de %Y")
    print ("-")*50 
    salir()
    

#Esta funcion es para retirar dinero
def retirar():
    global saldo
    print ("-")*50
    print "\tR E T I R A R"
    print "Ingresa el monto que deseas retirar en multiplos de $50"
    print ("-")*50
    print "Tu saldo es de: $", saldo
    retiro = input("Retirar: $")
    if retiro <= saldo and retiro > 0 and retiro%50 == 0:
        saldo = saldo - retiro
        print ("*")*50
        print "OPERACION EXITOSA"
        print "Retira el efectivo..."
        progress()
        print ("-")*50
        print "Tu saldo se ha actualizado." 
        print "Saldo: $", saldo
        print ("*")*50
        salir()
    else:
        print ("/")*50
        print "ERROR"
        print "Entrada invalida."
        print "Ingresa una cantidad igual o menor a: $", saldo
        print "Recuerda ingresar un multiplo de $50"
        print ("/")*50
        salirRetiro = input("Deseas: 1.intentar de nuevo o 2. Salir\nOpcion: ")
        if salirRetiro == 2:
            print "Adios. Gracias por usar el Banco del Emprendimiento"
            exit()
        elif salirRetiro == 1:
            retirar()
        else:
            salir()
    
#Esta funcion es para depositar dinero
def depositar():
    global saldo
    print ("-")*50
    print "\tD E P O S I T A R"
    print "Recuerda solo ingresar multiplos de $50"
    print ("-")*50
    print "Tu saldo es de: $", saldo
    deposito = int (input("Ingresa la cantidad que deseas depositar: $"))
    if deposito%50 == 0 and deposito > 0:
        saldo = saldo + deposito
        print ("*")*50
        print "Ingresa el efectivo..."
        progress()
        print "OPERACION EXITOSA"
        print "Tu saldo se ha actualizado." 
        print "Saldo: $", saldo
        print ("*")*50
        print "\n"
        salir()
    else:
        print ("/")*50
        print "ERROR"
        print "Ingresa una cantidad correcta..."
        print ("/")*50
        print "\n"
        depositar()

#Main Menu
def main():
    print ("-")*50
    print "\tM E N U"
    print "Ingresa una selecion para continuar:"
    print ("-")*50
    selection = (raw_input("1.Consultar Saldo\n2.Retirar Dinero\n3.Depositar Dinero\n4.Salir del ATM\n\nOpcion: "))
    if selection == "1":
        consultar()
    elif selection == "2":
        retirar()
    elif selection == "3":
        depositar()
    elif selection == "4":
        bye()
    else:
        print ("/")*50
        print "ERROR." 
        print "Entrada invalida. Intenta de nuevo..."
        print ("/")*50
        print "\n"
        main()

#Log
def userLog():
    global numberUser
    global saldo
    loginName = raw_input("Ingresa tu nombre de usuario: ")
    if loginName in names:
        numberUser = names.index(loginName)
        print "Hola,", completeNames[numberUser]
        loginPass = (input("Ingresa tu NIP: "))
        if loginPass == password[numberUser]:
            print "Ingreso correcto..."
            progress()
            print "\n"
            saldo = saldo[numberUser]
            main()
        else:
            print ("/")*50
            print "ERROR"
            print "NIP Incorrecto. Intenta de nuevo"
            print ("/")*50
            userLog()
    else:
        print ("/")*50
        print "ERROR"
        print "Usuario no registrado."
        print ("/")*50
        again = raw_input("Intentar de nuevo?(si/no): ")
        if again == "si":
            userLog()
        elif again == "no":
            bye()

            
#Code
displayMenu()

