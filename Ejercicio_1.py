#Cual es su nombre
nombre = input('¿Cuál es su nombre?\n')

#Saludar al usuario
print('Hola ' + nombre)

#Preguntar salario
salario = float(input('¿Cual es su salario?\n'))

#Preguntar tasa
tasa = float(input('Ingrese la tasa retefuente\n'))

#Calcular salario neto
salario_neto = salario * (100 -tasa) /100

#Preguntar salario
salario2 = float(input('¿Cual es su salario?\n'))

#Preguntar tasa
tasa2 = float(input('Ingrese la tasa retefuente\n'))

#Calcular salario neto
salario_neto2 = salario* (100 -tasa2) /100

#Preguntar salario
salario3 = float(input('¿Cual es su salario?\n'))

#Preguntar tasa
tasa3 = float(input('Ingrese la tasa retefuente\n'))

#Calcular salario neto
salario_neto3 = salario* (100 -tasa3) /100

print(nombre + ' Su ingreso total es', salario_neto+salario_neto2+salario_neto3)
