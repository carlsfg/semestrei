def sum2():
    print x + y
def sum3():
    print x + y + z
def sum4():
    print x + y + z + a
def sum5():
    print x + y + z + a + b
def sum6():
    print x + y + z + a + b + c
def sum7():
    print x + y + z + a + b + c + d
def sum8():
    print x + y + z + a + b + c + d + e
def sum9():
    print x + y + z + a + b + c + d + e + f
def sum10():
    print x + y + z + a + b + c + d + e + f + g

selector = input("Selecciona el numero de variables a sumar: ")
if selector == 2:
    x = input()
    y = input()
    sum2()

elif selector == 3:
    x = input()
    y = input()
    z = input()
    sum3()

elif selector == 4:
    x = input()
    y = input()
    z = input()
    a = input()
    sum4()