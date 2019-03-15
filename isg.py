n1 = int(input("Ingresa un numero entero positivo: "))
while n1>0:
    print ("-")*30
    print "Ingresa un numero menor a", n1
    n2 = int(input("Numero:"))
    if n1 > n2:
        print ("_")*30
        print "Bien, sigue:"
    else:
        print ("_")*30
        print "No, asi no. Bye"
        print "Tus numeros son:", n1, "y", n2
        start = raw_input("Quieres salir (si/no): ")
        if start == "si":
            exit()