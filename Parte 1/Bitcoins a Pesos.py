cantidad_btc = float(input("Ingrese la cantidad de Bitcoins: "))

tasa_conversion = float(input("Ingrese la tasa de conversión a dia de hoy(1 BTC a ARS): "))

equivale_pesos = cantidad_btc * tasa_conversion

print(f"{cantidad_btc} Bitcoins equivalen a {equivale_pesos} Pesos Argentinos.")