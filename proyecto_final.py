
def contar_vocales():
    texto = input("Ingrese una cadena de texto: ").lower()
    vocales = 'aeiou'
    cantidad = sum(1 for letra in texto if letra in vocales)
    print(f"Número de vocales: {cantidad}")

def es_primo():
    numero = int(input("Ingrese un número: "))
    if numero < 2:
        print("No es primo.")
        return
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print("No es primo.")
            return
    print("Es primo.")

def imprimir_impares():
    print("Números impares del 1 al 50:")
    for i in range(1, 51):
        if i % 2 != 0:
            print(i, end=' ')
    print()

def cuadrados_lista():
    cuadrados = [i ** 2 for i in range(1, 11)]
    print("Cuadrados del 1 al 10:", cuadrados)

def sumar_lista():
    numeros = input("Ingrese números separados por comas: ")
    lista = [float(n.strip()) for n in numeros.split(',')]
    print("Suma de los elementos:", sum(lista))

def maximo_en_tupla():
    datos = input("Ingrese números separados por comas (para tupla): ")
    tupla = tuple(float(n.strip()) for n in datos.split(','))
    print("Valor máximo en la tupla:", max(tupla))

def contar_elementos_while():
    datos = input("Ingrese elementos separados por comas: ")
    lista = datos.split(',')
    i = 0
    while i < len(lista):
        i += 1
    print("Cantidad de elementos en la lista:", i)

def categorizar_edad():
    edad = int(input("Ingrese su edad: "))
    if edad < 13:
        categoria = "Niño"
    elif edad < 18:
        categoria = "Adolescente"
    elif edad < 60:
        categoria = "Adulto"
    else:
        categoria = "Adulto mayor"
    print("Categoría:", categoria)

def ordenar_burbuja():
    datos = input("Ingrese números separados por comas: ")
    lista = [float(n.strip()) for n in datos.split(',')]
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("Lista ordenada:", lista)

def menu_principal():
    while True:
        print("\n=== Menú de Ejercicios ===")
        print("1. Contar vocales en una cadena")
        print("2. Verificar si un número es primo")
        print("3. Imprimir los números impares del 1 al 50")
        print("4. Crear una lista con los cuadrados del 1 al 10")
        print("5. Sumar los elementos de una lista")
        print("6. Encontrar el valor máximo en una tupla")
        print("7. Contar elementos en una lista usando while")
        print("8. Categorizar edad")
        print("9. Ordenar una lista de números (burbuja)")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            contar_vocales()
        elif opcion == "2":
            es_primo()
        elif opcion == "3":
            imprimir_impares()
        elif opcion == "4":
            cuadrados_lista()
        elif opcion == "5":
            sumar_lista()
        elif opcion == "6":
            maximo_en_tupla()
        elif opcion == "7":
            contar_elementos_while()
        elif opcion == "8":
            categorizar_edad()
        elif opcion == "9":
            ordenar_burbuja()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
