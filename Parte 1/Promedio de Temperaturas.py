temperaturas = []
for i in range(5):
    temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
    temperaturas.append(temperatura)

promedio = sum(temperaturas) / len(temperaturas)

print(f"La temperatura promedio de la semana es: {promedio:.2f}")
