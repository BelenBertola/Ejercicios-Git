cant_invitados = int(input("Ingrese la cantidad de invitados: "))
precioxkg = float(input("Ingrese el precio por kilogramo de carne ($): "))

cant_carne = cant_invitados * 0.7

costo_total = cant_carne * precioxkg

print(f"Franco necesita comprar {cant_carne:.2f} Kg de carne en total.")
print(f"El costo total estimado es de ${costo_total:.2f}.")