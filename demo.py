def menu():
    print("Selecciona el idioma.")
    x = input("1. Ingles\n2. Espanol\n")
    if x == 1:
        print "Hello, World"
    elif x == 2:
        print "Hola, Mundo"

print "Menu"
name = input("Ingresa tu nombre")
print "Hola", name, "Esta es tu calculadora"
menu()
