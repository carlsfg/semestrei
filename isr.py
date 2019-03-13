#Este programa calcula tus impuestos a pagar
a = float(input("Ingresa tus ingresos 2018:\n$"))
b = float(input("Ingresa tus egresos 2018:\n$"))
c = a-b
d = c*.3
if c > 0:
    print "Tu pago es de impuestos es de $", d
else:
    print "No pagas ISR"