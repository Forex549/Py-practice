l1 = []
l2 = []
l1.append("Luis")
l1.append(42)
l1.append("médico")
l2.append("Marcos")
l2.append(30)
l2.append("abogado")
l3 = l1 + l2
print("La lista es {}".format(l3))
l3.reverse()
print("La lista inversa es {}".format(l3))
l3.remove(42)
l3.remove(30)
print("La lista sin edades es {}".format(l3))

