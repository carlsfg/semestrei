#Este script evalua si pasaste el curso con base a 3 de tus calificaciones
def grades():
  grade1 = float(input("Ingresa tu primera calificacion: "))
  grade2 = float(input("Ingresa tu segunda calificacion: "))
  grade3 = float(input("Ingresa tu tercera calificacion: "))
  average = ((grade1+grade2+grade3)/3)
  if average >= 90:
    print ("Aprobado")
    print ("Tu promedio es de:"), average
  else:
    print ("No aprobado")
    print ("Tu promedio es de:"), average

  
