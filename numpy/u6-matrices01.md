Aquí tienes el ejercicio rediseñado y dividido en tareas para que los estudiantes puedan implementarlo paso a paso.

### Ejercicio: Control de Multas de Tránsito con NumPy

#### Objetivo:
Implementar un programa que utilice funciones para resolver cálculos de multas de tránsito en una ciudad utilizando arreglos de NumPy y listas de Python.

#### Descripción:
La ciudad será representada por una matriz de 5x5, dividida en cuadrantes y sectores. Cada celda de la matriz representa un cuadrante y cada sector agrupa varios cuadrantes. Cada cuadrante registrará el total de multas generadas en ese cuadrante. 

```
[['Norte' 'Norte' 'Norte' 'Norte' 'Norte']
 ['Oeste' 'Centro' 'Centro' 'Centro' 'Este']
 ['Oeste' 'Centro' 'Centro' 'Centro' 'Este']
 ['Oeste' 'Centro' 'Centro' 'Centro' 'Este']
 ['Sur' 'Sur' 'Sur' 'Sur' 'Sur']]
```
En el ejemplo de arriba se observa que los sectores están distribuidos de la siguiente manera:

* Norte: fila 0
* Oeste: columnas 0
* Centro: columnas 1 a 3 y filas 1 a 3
* Este: columna 4
* Sur: fila 4

### Tareas:

#### Tarea 1: Generación de la Matriz de Multas
1. Implementar una función `generaMatriz(listaMultas)` que reciba una lista de listas y retorne una matriz de NumPy de 5x5.
    - Cada lista dentro de la lista principal tiene 3 elementos `[fila, columna, multa]`.
    - `fila` y `columna` indican la posición del cuadrante en la matriz y `multa` es el valor de la multa en ese cuadrante.
    - La función debe construir y devolver una nueva matriz de NumPy con el valor agregado de las multas generadas para cada cuadrante.

Ejemplo de entrada:
```python
listaMultas = [
    [0, 0, 120], [1, 2, 330], [3, 4, 123],
    [4, 2, 62], [0, 0, 50], [4, 4, 89],
    [0, 3, 25], [2, 0, 43], [3, 2, 21],
    [0, 0, 120]
]
```

Ejemplo de salida:
```python
array([[290,   0,   0,  25,   0],
       [  0,   0, 330,   0,   0],
       [ 43,   0,   0,   0,   0],
       [  0,   0,  21,   0, 123],
       [  0,   0,  62,   0,  89]])
```

#### Tarea 2: Identificación del Sector con Más Multas
2. Implementar una función `sectorTop(matriz_multas, matriz_sectores)` que reciba la matriz de multas generada en la Tarea 1 y la matriz de sectores que se indica en la descripción. La función debe retornar una lista con el nombre del sector con el valor total de multas más alto y dicho valor.


Ejemplo de entrada:
```python
matriz = np.array(
    [[290,   0,   0,  25,   0],
    [  0,   0, 330,   0,   0],
    [ 43,   0,   0,   0,   0],
    [  0,   0,  21,   0, 123],
    [  0,   0,  62,   0,  89]], 
    [['Norte', 'Norte', 'Norte', 'Norte', 'Norte'],
    ['Oeste', 'Centro', 'Centro', 'Centro', 'Este'],
    ['Oeste', 'Centro', 'Centro', 'Centro', 'Este'],
    ['Oeste', 'Centro', 'Centro', 'Centro', 'Este'],
    ['Sur', 'Sur', 'Sur', 'Sur', 'Sur']]
    )
```

Ejemplo de salida:
```python
['Centro', 394]
```

#### Tarea 3: Programa Principal
3. Crear un programa principal que realice las siguientes acciones:
    - Llame a la función `generaMatriz(listaMultas)` con una lista de multas y obtenga la matriz de multas.
    - Llame a la función `sectorTop(matriz)` con la matriz de multas generada.
    - Muestre el nombre del sector con mayores multas y el valor total de las multas.

Asegúrate de probar las funciones con diferentes listas de multas para verificar que funcionen correctamente.