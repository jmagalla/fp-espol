### Ejercicio: Procesador de Lista de Números

**Objetivo:** Escribe un programa en Python que realice varias operaciones en una lista de números utilizando instrucciones iterativas y contadores.

#### Pasos:

1. **Crear la Lista:**
   - Inicializa una lista de enteros, `numeros`, con al menos 15 elementos. Puedes usar una mezcla de números positivos y negativos.

2. **Contar Números Positivos y Negativos:**
   - Escribe una función `contar_positivos_y_negativos` que tome la lista `numeros` como argumento y devuelva dos enteros, `contador_positivos` es el número de números positivos en la lista, y `contador_negativos` es el número de números negativos en la lista.

3. **Suma de Todos los Números:**
   - Escribe una función `suma_de_numeros` que tome la lista `numeros` como argumento y devuelva la suma de todos los números en la lista.

4. **Suma de Números Positivos:**
   - Escribe una función `suma_de_positivos` que tome la lista `numeros` como argumento y devuelva la suma de todos los números positivos en la lista.

5. **Suma de Números Negativos:**
   - Escribe una función `suma_de_negativos` que tome la lista `numeros` como argumento y devuelva la suma de todos los números negativos en la lista.

6. **Encontrar el Número Máximo y Mínimo:**
   - Escribe una función `encontrar_max_y_min` que tome la lista `numeros` como argumento y devuelva dos numeros: `numero_maximo` es el número más grande en la lista y `numero_minimo` es el número más pequeño en la lista.

7. **Programa Principal:**
   - En la parte principal de tu programa, llama a las funciones anteriores e imprime sus resultados. Utiliza declaraciones `print` claras y descriptivas.

### Plantilla de Solución

```python
def contar_positivos_y_negativos(numeros):
    contador_positivos = 0
    contador_negativos = 0
    return contador_positivos, contador_negativos

def suma_de_numeros(numeros):
    suma_total = 0
    return suma_total

def suma_de_positivos(numeros):
    suma_positivos = 0
    return suma_positivos

def suma_de_negativos(numeros):
    suma_negativos = 0
    return suma_negativos

def encontrar_max_y_min(numeros):
    numero_maximo = 0
    numero_minimo = 0
    return numero_maximo, numero_minimo

##### Programa Principal ######
# Inicializa una lista de números
numeros = [12, -4, 5, -2, 0, 13, 7, -9, 3, -8, 6, -1, 14, 11, -3]

# Contar positivos y negativos
contador_positivos, contador_negativos = contar_positivos_y_negativos(numeros)
print(f"Número de números positivos: {contador_positivos}")
print(f"Número de números negativos: {contador_negativos}")

# Suma de todos los números
suma_total = suma_de_numeros(numeros)
print(f"Suma de todos los números: {suma_total}")

# Suma de números positivos
suma_positivos = suma_de_positivos(numeros)
print(f"Suma de números positivos: {suma_positivos}")

# Suma de números negativos
suma_negativos = suma_de_negativos(numeros)
print(f"Suma de números negativos: {suma_negativos}")

# Encontrar número máximo y mínimo
numero_maximo, numero_minimo = encontrar_max_y_min(numeros)
print(f"Número máximo: {numero_maximo}")
print(f"Número mínimo: {numero_minimo}")

```

### Instrucciones para los Estudiantes:

1. Copia la plantilla de solución en tu entorno de Python.
2. Implementa cada función según las instrucciones.
3. Asegúrate de que tu programa se ejecute sin errores y produzca la salida correcta.
4. Prueba tu programa con diferentes listas de números para verificar su exactitud.
5. Envía tu código y la salida para revisión.

Este ejercicio te ayudará a entender cómo usar bucles, condicionales y contadores en Python para procesar listas de números de manera efectiva.

  # Instructions  

  ** this file should contain student lesson instructions **

  _ students will see these instructions in a read-only workspace tab _

  ## Steps
  1. 
  2. 
  3. 

  Use [Markdown](https://gist.github.com/cuonggt/9b7d08a597b167299f0d) to format your instructions.

  For example, here is a code block in python3
```python
def hello_world():
  print("hello world!")
```

  