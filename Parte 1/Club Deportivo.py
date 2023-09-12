nombre = input("Ingrese el nombre del socio: ")
edad = int(input("Ingrese la edad del socio: "))

if 13 <= edad <= 15:
    categoria = "infantiles"
elif 15 < edad <= 17:
    categoria = "cadetes"
elif 17 < edad <= 19:
    categoria = "juveniles"
else:
    categoria = "mayores"

print(f"{nombre} pertenece a la categoría de {categoria}.")