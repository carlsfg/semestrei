def isPair ():
    n = int(input("Type a number"))
    if n%2==0:
        return 1
    else:
        return 0

if isPair():
    print "Hola"
else:
    print "Bye"