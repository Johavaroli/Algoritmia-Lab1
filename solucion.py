import json
import time

ruta = "./Entrada-800.txt"

# Función que retorna el contenido del archivo proporcionado
def leer_archivo():
    archivo = open(ruta, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

# Función que convierte una cadena de caracteres a numeros (retorna una array o lista)
def convertir_str_numero(cadena):
    lineas = cadena.split("\n")
    lista_numeros = []
    for num in range(len(lineas)):
        lista_numeros.append(int(lineas[num]))
    return lista_numeros

# Función de ordenamiento burbuja con conteo de operaciones
def ordenar_burbuja(a):
    comparaciones, intercambios = 0, 0
    for recorrido in range(len(a) - 1):
        for elemento in range(len(a) - 1):
            comparaciones += 1
            if a[elemento] > a[elemento + 1]:
                intercambios += 1
                a[elemento], a[elemento + 1] = a[elemento + 1], a[elemento]
    return a, comparaciones, intercambios

# Función de ordenamiento por selección con conteo de operaciones
def ordenar_seleccion(a):
    comparaciones, intercambios = 0, 0
    for num in range(len(a)):
        min_idx = num
        for menor in range(num+1, len(a)):
            comparaciones += 1
            if a[menor] < a[min_idx]:
                min_idx = menor
        if min_idx != num:
            intercambios += 1
            a[num], a[min_idx] = a[min_idx], a[num]
    return a, comparaciones, intercambios

# Función de ordenamiento por inserción con conteo de operaciones
def ordenar_insercion(a):
    comparaciones, desplazamientos = 0, 0
    for i in range(1, len(a)):
        actual = a[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if a[j] > actual:
                a[j + 1] = a[j]
                desplazamientos += 1
            else:
                break
            j -= 1
        a[j + 1] = actual
    return a, comparaciones, desplazamientos

# Función de ordenamiento por mezcla (Merge Sort) con conteo de operaciones
def merge_sort(a):
    if len(a) <= 1:
        return a, 0
    medio = len(a) // 2
    izquierda, comp_izq = merge_sort(a[:medio])
    derecha, comp_der = merge_sort(a[medio:])
    resultado, comp_merge = merge(izquierda, derecha)
    return resultado, comp_izq + comp_der + comp_merge

def merge(izquierda, derecha):
    resultado = []
    i = 0
    j = 0
    comparaciones = 0
    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado += izquierda[i:]
    resultado += derecha[j:]
    return resultado, comparaciones

# Función de ordenamiento rápido (Quick Sort) con conteo de operaciones
def quicksort(a):
    if len(a) <= 1:
        return a, 0
    else:
        pivote = a[len(a) - 1]
        menores, iguales, mayores = [], [], []
        comparaciones = 0
        for x in a:
            comparaciones += 1
            if x < pivote:
                menores.append(x)
            elif x == pivote:
                iguales.append(x)
            else:
                mayores.append(x)
        menores_sorted, comp_menores = quicksort(menores)
        mayores_sorted, comp_mayores = quicksort(mayores)
        return menores_sorted + iguales + mayores_sorted, comparaciones + comp_menores + comp_mayores

# Función para ejecutar el ordenamiento y contar las operaciones
def ejecutar_ordenamiento(opcion, array):
    # Inicio del tiempo de ejecución
    inicio = time.time()

    # Seleccionar el algoritmo de ordenamiento
    if opcion == 1:
        lista_ordenada, comparaciones, intercambios = ordenar_burbuja(array)
        metodo = "Burbuja"
        operaciones_basicas = comparaciones + intercambios
    elif opcion == 2:
        lista_ordenada, comparaciones, intercambios = ordenar_seleccion(array)
        metodo = "Selección"
        operaciones_basicas = comparaciones + intercambios
    elif opcion == 3:
        lista_ordenada, comparaciones, desplazamientos = ordenar_insercion(array)
        metodo = "Inserción"
        operaciones_basicas = comparaciones + desplazamientos
    elif opcion == 4:
        lista_ordenada, comparaciones = merge_sort(array)
        metodo = "Mezcla (Merge Sort)"
        operaciones_basicas = comparaciones
    elif opcion == 5:
        lista_ordenada, comparaciones = quicksort(array)
        metodo = "Rápido (Quick Sort)"
        operaciones_basicas = comparaciones
    else:
        print("Ingresa un número entre 1 y 5.")
        return

    # Fin del tiempo de ejecución
    fin = time.time()
    # Duración de la ejecución
    duracion = fin - inicio

    # Mostrar resultados
    print(f"VER RESULTADOS POR {metodo}:")
    print(json.dumps(lista_ordenada, indent=4))
    print(f"El tiempo de ejecución es: {round(duracion, 2)} segundos")
    print(f"Número de operaciones básicas: {operaciones_basicas}")

# EJECUCIÓN DEL ALGORITMO
try:
    opcion = int(input("""POR FAVOR ELIGE EL TIPO DE ORDENAMIENTO QUE QUIERES EJECUTAR:
    1. Ordenamiento Burbuja
    2. Ordenamiento por Selección
    3. Ordenamiento por Inserción
    4. Ordenamiento por Mezcla (Merge Sort)
    5. Ordenamiento Rápido (Quick Sort)

    Escribe aquí tu elección: """))

    cadena = leer_archivo()
    array = convertir_str_numero(cadena)
    ejecutar_ordenamiento(opcion, array)

except ValueError:
    print("Opción no válida. Debe ser un número.")