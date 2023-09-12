import random

def generar_lista_de_atletas():
    """
    Esta función genera aleatoriamente los datos de 20 atletas que participaron en una maratón.
    Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
        - nombre: el nombre del atleta
        - numero: el número con el que participó en la maratón
        - tiempo_llegada: la cantidad de segundos que tardó en llegar
    """
    lista_atletas = []
    nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
    apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')
    for i in range(1, 21):
        atleta = {
            "nombre": random.choice(nombres) + " " + random.choice(apellidos),
            "numero": i,
            "tiempo_llegada": random.random() * 120
        }
        lista_atletas.append(atleta)
    return lista_atletas

def imprimir_datos_atletas(lista_atletas):
    for atleta in lista_atletas:
        print(f"{atleta['numero']} - {atleta['nombre']}: ({atleta['tiempo_llegada']} segundos)")

def atleta_ganador(lista_atletas):
    ganador = min(lista_atletas, key=lambda x: x['tiempo_llegada'])
    return ganador['numero']

def datos_atleta(numero_atleta, lista_atletas):
    for atleta in lista_atletas:
        if atleta['numero'] == numero_atleta:
            return atleta


lista_atletas = generar_lista_de_atletas()

imprimir_datos_atletas(lista_atletas)

ganador = atleta_ganador(lista_atletas)
print(f"Atleta ganador: {ganador}")

numero_atleta = int(input("Ingrese el número del atleta que desea buscar: "))
datos = datos_atleta(numero_atleta, lista_atletas)
if datos:
    print(f"Datos del atleta {numero_atleta}: {datos}")
else:
    print(f"No se encontraron datos para el atleta con número {numero_atleta}")