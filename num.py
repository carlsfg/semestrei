n1 = int(input("Ingresa el primer numero"))
n2 = int(input("Ingresa el segundo numero"))

while n1 > n2:
    if n1 < n2:
        n2 = input("Ingresa de nuevo el segundo numero")
        
print "Tus numeros son", n1, n2
        exit()