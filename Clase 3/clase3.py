nombre = input("ingrese nombre y apellido del empleado: ")
distrito = input("ingrese distrito de procedencia: ")
sueldo = int(input("ingrese el sueldo:"))

sueldo_final = sueldo * 3-(0.1 * sueldo)

lista = [nombre,distrito,sueldo_final]

nombre1, distrito1, sueldo_final = lista

print("{} recibira {} soles a fin de año".format(nombre1,sueldo_final))