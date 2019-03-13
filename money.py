import json
x = input("Ingresa la cantidad:")
renta = x*0.25
servicios = x*0.15
comida = x*0.3
tareas = x*0.2
diversion = x*0.1
print "Renta", "$", renta
print "Servicios","$", servicios
print "Comida","$", comida
print "Tareas","$", tareas
print "Diversion","$", diversion

# a Python object (dict):
x = {
  "rent": renta,
  "servicios": servicios,
  "comida": comida,
  "tareas": tareas,
  "diversion": diversion,
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

