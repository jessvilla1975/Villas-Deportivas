import numpy as np


def leer_matrices_desde_archivo(archivo):
    matrices = []
    with open(archivo, 'r') as f:
        matriz_actual = []
        for linea in f:
            linea = linea.strip()
            if linea == '':
                if matriz_actual:
                    matrices.append(matriz_actual)
                    matriz_actual = []
            else:
                fila = [int(x) for x in linea.split()]
                matriz_actual.append(fila)
        if matriz_actual:
            matrices.append(matriz_actual)
    return matrices

def escribir_matriz_en_archivo(archivo, matriz):
    with open(archivo, 'a') as f:
        # Escribir la matriz
        for fila in matriz:
            linea = ' '.join(str(x) for x in fila)
            f.write(linea + '\n')
        f.write('\n')

def verificar_conflicto(villa, seleccion, matriz):
    for i in villa:
        if matriz[i][seleccion] == 1 or matriz[seleccion][i] == 1:
            return True
    return False

def asignar_villas(matriz):
    num_selecciones = len(matriz)
    villas = []

    for seleccion in range(num_selecciones):
        asignada = False
        for villa in villas:
            if not verificar_conflicto(villa, seleccion, matriz):
                villa.append(seleccion)
                asignada = True
                break
        if not asignada:
            villas.append([seleccion])

    return villas

def construir_matriz_salida(villas, num_selecciones):
    num_villas = len(villas)
    matriz_salida = [[0] * num_selecciones for _ in range(num_villas)]

    for i in range(num_villas):
        villa = villas[i]
        for seleccion in villa:
            matriz_salida[i][seleccion] = 1

    return matriz_salida

def imprimir_salida(matriz_salida):
    for fila in matriz_salida:
        print(fila)
    return ""

def limpiar_archivos():
    with open("entrada.txt", "w") as f:
        f.write("")
    
    with open("salida.txt", "w") as f:
        f.write("")

def generar_salida():
    archivo_entrada = 'entrada.txt'
    archivo_salida = 'salida.txt'

    matrices_entrada = leer_matrices_desde_archivo(archivo_entrada)

    for i, entrada in enumerate(matrices_entrada):
        villas = asignar_villas(entrada)
        matriz_salida = construir_matriz_salida(villas, len(entrada))

        # Escribir la matriz en el archivo de salida
        escribir_matriz_en_archivo(archivo_salida, matriz_salida)

        # Escribir las villas en el archivo de salida
        with open(archivo_salida, 'a') as f:
            for j, villa in enumerate(villas):
                indices = [str(k + 1) for k in villa]
                f.write(f"Villa {j + 1} = [{', '.join(indices)}]\n")
            f.write('\n')

        print(f"Matriz de salida para entrada {i + 1}:")
        imprimir_salida(matriz_salida)
        print()

generar_salida() 