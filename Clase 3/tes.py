nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")

union = nombre + " " + apellido

tamaño = len(union)

print("El nombre completo en mayuscula es {} y tiene {} caracteres".format(union.upper(),tamaño))

if len(nombre) > len(apellido):
    print("El nombre es mas grande que el apellido")
elif len(nombre) < len(apellido):
    print("El nombre es mas corto que el apellido")
else:
    print("El apellido y el nombre tienen el mismo tamaño")