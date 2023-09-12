#Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random).Luego:
#Muestre la lista
#El usuario debe ingresar un valor. El programa debe informar cuántos valores de la lista son
#mayores a dicho valor, para eso debe utilizar una función. La función debe recibir como argumentos la lista y 
#un entero, y debe retornar la cantidad de valores de la lista mayores a dicho entero.
#Crear una función que calcule el promedio de la lista y utilizarla.
#Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne.***
import random

def main():
    lista = generar_lista(10)
    print("Lista generada:", lista)
    
    valor_ingresado = int(input("Ingresa un valor: "))
    cantidad_mayores = contar_mayores(lista, valor_ingresado)
    print("Cantidad de valores mayores a", valor_ingresado, ":", cantidad_mayores)
    
    promedio = calcular_promedio(lista)
    print("Promedio de la lista:", promedio)
    
    maximo, minimo = encontrar_maximo_minimo(lista)
    print("Valor máximo de la lista:", maximo)
    print("Valor mínimo de la lista:", minimo)


def generar_lista(num_elementos):
    lista = [random.randint(1, 20) for _ in range(num_elementos)]
    return lista

def contar_mayores(lista, valor):
    contador = 0
    for num in lista:
        if num > valor:
            contador += 1
    return contador

def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / 10
    return promedio

def encontrar_maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

if __name__ == "__main__":
    main()
