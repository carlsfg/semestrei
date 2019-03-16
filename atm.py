#Time
import datetime
now = datetime.datetime.now()

#Variables
names = ["Richy", "Cecilia", "Caro", "Ulises"]
completeNames = ["Ricardo Esquivel", "Ana Cecilia Castro", "Carolina Rodriguez.","Ulises Cruz Miranda"]
password = [2222,3333,4444,5555]
saldo = [5000,4000,3000,10000]
numberUser = 0

#Display Menu
def displayMenu():
    print ("-")*30
    print ("\tATM Banco Python")
    print ("-")*30
    print now.strftime("Hoy es %A, %d, de %B de %Y y son las %H:%M")
    userLog()

#Esta funcion es para salir
def bye():
    print "Goodbye, thanks for using the Python Bank"
    exit()

#Esta funcion es para salir
def salir():
    salir = raw_input("Deseas realizar otra operacion?: (s/n)")
    if salir == "n":
        exit()
    elif salir == "s":
        main()

#Esta funcion es para consultar el saldo
def consultar():
    global saldo
    print ("-")*30
    print "Tu saldo es de: $", saldo
    print ("-")*30 
    main()

#Esta funcion es para retirar dinero
def retirar():
    global saldo
    print "Tu saldo es de: $", saldo
    retiro = int (input("Ingresa la cantidad que deseas retirar: $"))
    if retiro < saldo and retiro > 0:
        saldo = saldo - retiro
        print "tu saldo es ahora de: $", saldo
        main()
    else:
        print "Error debes ingresar una cantidad menor a", saldo, "Pero menor a cero, tonto"
        retirar()
     
#Esta funcion es para depositar dinero
def depositar():
    global saldo
    print "Tu saldo es de: $", saldo
    deposito = int (input("Ingresa la cantidad que deseas depositar: $"))
    saldo = saldo + deposito
    print ("*")*30
    print "Operacion Exitosa"
    print "Tu saldo se ha actualizado a: $", saldo
    print ("*")*30
    main()

#Main Menu
def main():
    print ("-")*30
    print "Bienvenido!"
    print "Selecciona una opcion para continuar:"
    print ("-")*30
    selection = (raw_input("1.Consultar Saldo\n2.Retirar\n3.Depositar\n4.Salir\n\nOpcion:"))
    if selection == "1":
        consultar()
    elif selection == "2":
        retirar()
    elif selection == "3":
        depositar()
    elif selection == "4":
        print "Gracias por usar el Banco Python. Adios."
        print ("-")*30
        exit()
    else:
        print "Error. Entrada invalida, intenta de nuevo porfavor."
        print ("-")*30
        main()
    
#Log
def userLog():
    global numberUser
    global saldo
    loginName = raw_input("Ingresa usuario: ")
    if loginName in names:
        numberUser = names.index(loginName)
        print "Hola", completeNames[numberUser]
        loginPass = input("Ingresa tu NIP: ")
        if loginPass == password[numberUser]:
            print "Ingreso correcto."
            saldo = saldo[numberUser]
            main()
        else:
            print "PIN incorrecto. Intenta de nuevo"
            userLog()
    else:
        print "Usuario no registrado."
        again = raw_input("Intentar de nuevo?(s/n)")
        if again == "s":
            userLog()
        elif again == "n":
            bye()
            
#Code
displayMenu()

