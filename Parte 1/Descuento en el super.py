monto_compra = float(input("Ingrese el monto de la compra: "))
minimoparadescuento = 3500
porcentaje_descuento = 10

# Calcular el importe final
if monto_compra > minimoparadescuento:
    descuento = monto_compra * (porcentaje_descuento / 100)
    importe_final = monto_compra - descuento
else:
    importe_final = monto_compra

print(f"El importe final a pagar es: ${importe_final:.2f}")