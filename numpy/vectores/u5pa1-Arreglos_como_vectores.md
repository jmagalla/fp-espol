# Ejercicio: Pilotos de F1 usando Vectores Paralelos

## Objetivo:
Escribir un programa que cargue datos de pilotos de F1 y sus puntos desde un archivo de texto, y luego realice varias operaciones utilizando vectores paralelos y la indexación booleana.

## Instrucciones:

1. Identificar el archivo de texto `pilots.txt` con los nombres de los pilotos de F1.
2. Identificar el archivo de texto `points.txt` con los puntos correspondientes de los pilotos.
4. Escriba una función llamada `load_data(filename)` que reciba el nombre de un archivo como parámetro y retorne un arreglo de NumPy. La función debe leer el contenido del archivo y crear un arreglo de NumPy donde cada línea del archivo se convierta en un elemento del arreglo.
3. Escribir un programa en Python que cargue los datos desde estos archivos y realice las siguientes operaciones:
   - Filtrar pilotos con al menos un número específico de puntos.
   - Encontrar el piloto con el mayor número de puntos.
   - Ordenar los pilotos por sus puntos en orden ascendente.
   - Obtener los 3 mejores pilotos con más puntos.

## Ejemplo de las llamadas a la función para cargar los datos:

```python
import numpy as np

# Cargar datos desde archivos de texto
pilots = load_data('pilots.txt')
points = load_data('points.txt').astype(int)

```

### Notas:
- Asegúrate de que los archivos de texto estén en el mismo directorio que tu script de Python.
- Puedes cambiar los datos en los archivos de texto para probar con diferentes conjuntos de datos.

Este ejercicio ayudará a tus estudiantes a comprender cómo trabajar con vectores paralelos, realizar operaciones con vectores y manejar archivos de texto en Python.