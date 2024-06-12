# Proyecto: Asignación Óptima de Villas Deportivas

Este repositorio contiene el código y la documentación para el proyecto final del curso de Análisis y Diseño de Algoritmos I de la Universidad del Valle, Sede Tuluá. El proyecto tiene como objetivo aplicar diferentes conceptos aprendidos durante el desarrollo del período académico mediante la implementación de una herramienta que asigna de manera óptima las villas deportivas para alojar a las selecciones participantes en un evento deportivo.

## Objetivo

El propósito de este proyecto es aplicar los conocimientos adquiridos durante el curso para resolver un problema práctico, consolidando así los objetivos de formación del curso.

## Descripción del Proyecto

Para la celebración de unas justas deportivas mundiales, se requiere la construcción de villas deportivas para alojar a las diferentes selecciones participantes, teniendo en cuenta las siguientes restricciones:

- Varias selecciones deben hospedarse en la misma villa deportiva por cuestiones de logística.
- No es posible hospedar en una misma villa dos o más selecciones de países que no tengan relaciones diplomáticas amistosas.
- No es posible asignar una villa a una sola selección a menos que sea estrictamente necesario.

## Formato de Entrada

La entrada se suministra a través de una matriz cuadrada (M) de 1’s y 0’s en un archivo de texto plano. La matriz representa las relaciones diplomáticas entre los países, donde:

- `M[i, j] = 1` si los países i y j no tienen relaciones amistosas.
- `M[i, j] = 0` en caso contrario.

## Formato de Salida

La salida es una matriz (S) de n x m (filas y columnas) donde n representa las villas a construir y m las diferentes selecciones. En la matriz S:

- `S[i, j] = 1` si en la villa i se aloja la selección j.
- `S[i, j] = 0` en caso contrario.

## Requisitos

- Python 3.x
- NumPy
- Tkinter
- Pillow

## Estructura del Código

El código principal del proyecto se encuentra en el archivo `interfaz.py`. A continuación, se describen las funciones principales:

1. **leer_matrices_desde_archivo(archivo):** Lee las matrices de entrada desde un archivo de texto.
2. **escribir_matriz_en_archivo(archivo, matriz):** Escribe una matriz en un archivo de texto.
3. **verificar_conflicto(villa, seleccion, matriz):** Verifica si hay un conflicto al asignar una selección a una villa.
4. **asignar_villas(matriz):** Asigna las selecciones a las villas minimizando el número de villas necesarias.
5. **construir_matriz_salida(villas, num_selecciones):** Construye la matriz de salida a partir de las villas asignadas.
6. **imprimir_salida(matriz_salida):** Imprime la matriz de salida en la consola.
7. **limpiar_archivos():** Limpia los archivos de entrada y salida.
8. **generar_salida():** Genera la salida leyendo las matrices de entrada, asignando las villas y escribiendo los resultados en un archivo de salida.

## Ejecución del Proyecto

Para ejecutar el proyecto, asegúrese de que los archivos de entrada estén en el mismo directorio que el código. Luego, simplemente ejecute el archivo `interfaz.py`:



## Interfaz inicio
![gif](https://github.com/jessvilla1975/Villas-Deportivas/assets/114515509/2d8018a7-b4ee-4782-bf26-6e93c416eef2)

## Interfaz ingreso matriz
![image](https://github.com/jessvilla1975/Villas-Deportivas/assets/114515509/1dc9985b-4a77-4da6-b93c-6ec6d2a66d96)
![image](https://github.com/jessvilla1975/Villas-Deportivas/assets/114515509/01c7e887-cbfb-4ba5-98f0-b47c04351aa9)
![image](https://github.com/jessvilla1975/Villas-Deportivas/assets/114515509/21d40239-f707-4a99-a11e-18697d8c89c1)



```bash
python interfaz.py
