# Lectura autónoma: Diccionarios en Python

**Asignatura:** Fundamentos de Programación  
**Tema:** Colecciones — Diccionarios  

---

## Objetivo de la lectura

Esta lectura introduce el uso de los diccionarios en Python como una estructura que permite relacionar información mediante pares **clave–valor**.

Al finalizar la lectura, el estudiante será capaz de:

- Explicar qué es un diccionario.
- Identificar un par **clave–valor**.
- Comprender para qué sirve un diccionario.
- Diferenciar una lista de un diccionario.
- Utilizar una clave como criterio de búsqueda.
- Identificar cuándo una búsqueda se realiza directamente por clave y cuándo requiere una búsqueda secuencial por los valores.
- Agregar, actualizar y eliminar elementos de un diccionario.
- Recorrer las claves, los valores y los pares de un diccionario.
- Utilizar un diccionario como contador.
- Utilizar un diccionario como acumulador.
- Almacenar una lista de valores asociada a una clave.
- Resumir elementos repetidos de una lista mediante un diccionario.

---

# 1. ¿Por qué necesitamos otra colección?

Hasta ahora hemos trabajado principalmente con listas.

Por ejemplo:

```python
estudiantes = ["Ana", "Luis", "Carlos"]
```

Las listas son útiles cuando queremos almacenar varios elementos y acceder a ellos mediante su posición.

```python
print(estudiantes[0])
```

Salida:

```text
Ana
```

Sin embargo, considera el siguiente problema.

Queremos guardar la edad de cada estudiante:

| Estudiante | Edad |
|---|---:|
| Ana | 20 |
| Luis | 18 |
| Carlos | 19 |

Podríamos utilizar dos listas:

```python
nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 18, 19]
```

Pero para obtener la edad de Luis tendríamos que:

1. Buscar la posición de `"Luis"` en la lista `nombres`.
2. Utilizar esa misma posición en la lista `edades`.

Este problema puede resolverse de manera más directa utilizando un **diccionario**.

---

# 2. ¿Qué es un diccionario?

Un diccionario es una colección que permite relacionar dos piezas de información.

Cada elemento de un diccionario está formado por un par:

```text
clave : valor
```

Por ejemplo:

```text
"Ana" : 20
"Luis" : 18
"Carlos" : 19
```

En Python, el diccionario se escribe utilizando llaves:

```python
edades = {
    "Ana": 20,
    "Luis": 18,
    "Carlos": 19
}
```

En este ejemplo:

- `"Ana"`, `"Luis"` y `"Carlos"` son las **claves**.
- `20`, `18` y `19` son los **valores**.

---

# 3. ¿Qué es un par clave–valor?

Cada elemento de un diccionario tiene dos partes relacionadas.

```text
clave : valor
```

La clave identifica el dato y el valor contiene la información asociada.

Ejemplos:

| Clave | Valor |
|---|---|
| `"Ecuador"` | `"Quito"` |
| `"P001"` | `"Teclado"` |
| `"Ana"` | `20` |
| `"ESP"` | `15` |

Un diccionario podría representar las capitales de varios países:

```python
capitales = {
    "Ecuador": "Quito",
    "Perú": "Lima",
    "Chile": "Santiago"
}
```

En este caso:

- el país es la clave;
- la capital es el valor.

---

# 4. La clave como criterio de búsqueda

La clave es el dato que se utiliza para localizar información dentro del diccionario.

En diferentes aplicaciones se pueden usar relaciones como las siguientes:

| Clave | Valor |
|---|---|
| Cédula | Nombre de la persona |
| Código | Nombre del producto |
| Placa | Propietario del vehículo |
| Usuario | Información de la cuenta |
| Equipo | Puntaje |
| País | Capital |

Una buena clave debe identificar claramente el elemento que se desea consultar.

## Características importantes de las claves

- No pueden repetirse dentro del mismo diccionario.
- Se utilizan como criterio de búsqueda.
- Pueden ser cadenas, números u otros tipos inmutables.
- No representan posiciones.

Por ejemplo:

```python
puntajes = {
    "Ecuador": 7,
    "Brasil": 9,
    "Argentina": 6
}
```

Aquí `"Ecuador"` es una clave, no una posición.

---

# 5. Diferencias entre una lista y un diccionario

Una lista organiza sus elementos por posición.

```python
estudiantes = ["Ana", "Luis", "Carlos"]
```

Para obtener a Luis:

```python
print(estudiantes[1])
```

Un diccionario organiza sus elementos por clave.

```python
edades = {
    "Ana": 20,
    "Luis": 18,
    "Carlos": 19
}
```

Para obtener la edad de Luis:

```python
print(edades["Luis"])
```

## Comparación

| Lista | Diccionario |
|---|---|
| Acceso mediante índice | Acceso mediante clave |
| El índice suele ser un número | La clave puede ser una cadena o un número |
| Es adecuada para mantener una secuencia | Es adecuado para relacionar información |
| Responde: “¿qué hay en esta posición?” | Responde: “¿qué valor corresponde a esta clave?” |

---

# 6. Buscar información en un diccionario

Supongamos el siguiente diccionario:

```python
edades = {
    "Ana": 20,
    "Luis": 18,
    "Carlos": 19
}
```

## 6.1. Acceso directo por clave

Cuando conocemos la clave, podemos obtener directamente el valor asociado.

```python
print(edades["Luis"])
```

Salida:

```text
18
```

En este caso no necesitamos recorrer todos los elementos.

La clave `"Luis"` nos permite acceder directamente al valor `18`.

---

## 6.2. Verificar si una clave existe con `in`

El operador `in` permite verificar si una clave existe en el diccionario.

```python
if "Luis" in edades:
    print("El estudiante está registrado")
```

Salida:

```text
El estudiante está registrado
```

La expresión:

```python
"Luis" in edades
```

significa:

> ¿La clave `"Luis"` existe en el diccionario?

## Importante

Cuando `in` se aplica directamente a un diccionario, busca entre las **claves**, no entre los valores.

```python
print(18 in edades)
```

Salida:

```text
False
```

Aunque `18` existe como valor, no existe como clave.

---

## 6.3. Buscar un valor

Supongamos que queremos responder:

> ¿Existe algún estudiante que tenga 18 años?

Podemos utilizar:

```python
if 18 in edades.values():
    print("Existe un estudiante de 18 años")
```

Salida:

```text
Existe un estudiante de 18 años
```

En este caso se revisan los valores del diccionario.

---

## 6.4. Búsqueda secuencial por los valores

También podemos recorrer los valores uno por uno.

```python
encontrado = False

for edad in edades.values():
    if edad == 18:
        encontrado = True

print(encontrado)
```

Salida:

```text
True
```

Esta es una búsqueda secuencial porque el programa debe revisar los valores hasta encontrar el dato buscado.

---

## 6.5. Encontrar la clave asociada a un valor

Ahora consideremos la pregunta:

> ¿Qué estudiante tiene 18 años?

Para responderla, debemos recorrer las claves y revisar sus valores.

```python
for nombre in edades:
    if edades[nombre] == 18:
        print(nombre)
```

Salida:

```text
Luis
```

## Comparación de búsquedas

| Pregunta | Tipo de búsqueda |
|---|---|
| ¿Está registrada la clave `"Luis"`? | Directa por clave |
| ¿Cuál es la edad de `"Luis"`? | Directa por clave |
| ¿Existe una edad igual a `18`? | Búsqueda por valores |
| ¿Quién tiene `18` años? | Búsqueda secuencial por los valores |

### Idea clave

Los diccionarios están diseñados para buscar información mediante una clave.

Cuando el criterio de búsqueda está en los valores, generalmente es necesario recorrer el diccionario.

---

# 7. ¿Qué ocurre si la clave no existe?

Si intentamos acceder a una clave que no existe, Python genera un error.

```python
print(edades["Pedro"])
```

Salida:

```text
KeyError: 'Pedro'
```

Por esta razón, es conveniente verificar primero si la clave existe.

```python
if "Pedro" in edades:
    print(edades["Pedro"])
else:
    print("Pedro no está registrado")
```

---

# 8. Agregar, actualizar y eliminar elementos

## 8.1. Agregar un elemento

Para agregar un nuevo par clave–valor:

```python
edades["Pedro"] = 21
```

Ahora el diccionario contiene:

```python
{
    "Ana": 20,
    "Luis": 18,
    "Carlos": 19,
    "Pedro": 21
}
```

---

## 8.2. Actualizar un elemento

Si la clave ya existe, la asignación actualiza el valor.

```python
edades["Ana"] = 22
```

El valor asociado a `"Ana"` cambia de `20` a `22`.

### Importante

La misma instrucción puede agregar o actualizar:

```python
diccionario[clave] = valor
```

- Si la clave no existe, se agrega.
- Si la clave existe, se actualiza.

---

## 8.3. Eliminar un elemento

Para eliminar un par clave–valor:

```python
del edades["Pedro"]
```

---

# 9. Operaciones básicas con diccionarios

Supongamos:

```python
edades = {
    "Ana": 20,
    "Luis": 18,
    "Carlos": 19
}
```

## Cantidad de elementos

```python
print(len(edades))
```

Salida:

```text
3
```

## Obtener las claves

```python
print(edades.keys())
```

## Obtener los valores

```python
print(edades.values())
```

## Obtener los pares clave–valor

```python
print(edades.items())
```

---

# 10. Recorrer un diccionario

## 10.1. Recorrer las claves

```python
for nombre in edades:
    print(nombre)
```

Salida:

```text
Ana
Luis
Carlos
```

---

## 10.2. Recorrer los valores

```python
for edad in edades.values():
    print(edad)
```

---

## 10.3. Recorrer las claves y consultar sus valores

```python
for nombre in edades:
    print(nombre, edades[nombre])
```

Posible salida:

```text
Ana 20
Luis 18
Carlos 19
```

---

# 11. Diccionario como contador

Uno de los usos más importantes de los diccionarios es contar elementos repetidos.

Supongamos la siguiente lista:

```python
equipos = [
    "Ecuador",
    "Brasil",
    "Ecuador",
    "España",
    "Brasil",
    "Brasil"
]
```

Queremos obtener el siguiente resumen:

```python
{
    "Ecuador": 2,
    "Brasil": 3,
    "España": 1
}
```

Podemos construirlo de la siguiente manera:

```python
contador = {}

for equipo in equipos:
    if equipo in contador:
        contador[equipo] += 1
    else:
        contador[equipo] = 1
```

## ¿Qué ocurre en cada iteración?

- Si el equipo ya es una clave, aumentamos su contador.
- Si el equipo todavía no existe, lo agregamos con valor `1`.

En este problema:

- la clave representa el elemento que se está contando;
- el valor representa la cantidad de apariciones.

---

# 12. Diccionario como acumulador

Un diccionario también puede utilizarse para acumular cantidades asociadas a una misma clave.

Consideremos una lista de ventas.

Cada lista interna contiene:

1. el nombre del vendedor;
2. el valor de una venta.

```python
ventas = [
    ["Ana", 10],
    ["Luis", 5],
    ["Ana", 20],
    ["Luis", 15],
    ["Carlos", 8]
]
```

Queremos obtener:

```python
{
    "Ana": 30,
    "Luis": 20,
    "Carlos": 8
}
```

Código:

```python
totales = {}

for venta in ventas:
    vendedor = venta[0]
    monto = venta[1]

    if vendedor in totales:
        totales[vendedor] += monto
    else:
        totales[vendedor] = monto
```

En este problema:

- la clave es el nombre del vendedor;
- el valor es el total acumulado;
- si el vendedor ya existe, se suma el monto;
- si no existe, se agrega con el primer monto registrado.

---

# 13. Diferencia entre contador y acumulador

Aunque ambos patrones son similares, no realizan exactamente la misma tarea.

## Contador

Aumenta normalmente de uno en uno.

```python
contador[elemento] += 1
```

Ejemplo:

```text
¿Cuántas veces aparece cada palabra?
```

## Acumulador

Suma cantidades que pueden ser diferentes.

```python
totales[clave] += cantidad
```

Ejemplo:

```text
¿Cuánto vendió en total cada vendedor?
```

## Comparación

| Patrón | Clave | Valor |
|---|---|---|
| Contador | Elemento repetido | Cantidad de apariciones |
| Acumulador | Categoría o identificador | Total acumulado |

---

# 14. Diccionario cuyo valor es una lista

Los valores de un diccionario pueden ser listas.

Por ejemplo:

```python
notas = {
    "Ana": [18, 20, 19],
    "Luis": [15, 17],
    "Carlos": [20, 18]
}
```

En este diccionario:

- cada clave representa un estudiante;
- cada valor es una lista con sus notas.

Para obtener las notas de Ana:

```python
print(notas["Ana"])
```

Salida:

```text
[18, 20, 19]
```

Para obtener la primera nota de Ana:

```python
print(notas["Ana"][0])
```

Salida:

```text
18
```

---

# 15. Agregar elementos a una lista almacenada en un diccionario

Supongamos:

```python
notas = {
    "Ana": [18, 20],
    "Luis": [15, 17]
}
```

Para agregar una nueva nota a Ana:

```python
notas["Ana"].append(19)
```

El resultado será:

```python
{
    "Ana": [18, 20, 19],
    "Luis": [15, 17]
}
```

## Agregar una nueva clave con una lista

```python
notas["Carlos"] = [20]
```

---

# 16. Problemas de búsqueda cuando el valor es una lista

Consideremos:

```python
materias = {
    "Ana": ["Programación", "Matemáticas"],
    "Luis": ["Física", "Programación"],
    "Carlos": ["Química"]
}
```

## Buscar directamente las materias de Ana

```python
print(materias["Ana"])
```

Esta es una búsqueda directa por clave.

## Buscar quién está registrado en Programación

```python
for estudiante in materias:
    if "Programación" in materias[estudiante]:
        print(estudiante)
```

Posible salida:

```text
Ana
Luis
```

Esta es una búsqueda secuencial porque `"Programación"` se encuentra dentro de las listas almacenadas como valores.

---

# 17. Resumir elementos repetidos de una lista

Los diccionarios permiten resumir grandes cantidades de información.

Lista original:

```python
lenguajes = [
    "Python",
    "Java",
    "Python",
    "C++",
    "Java",
    "Python"
]
```

Resumen:

```python
{
    "Python": 3,
    "Java": 2,
    "C++": 1
}
```

Código:

```python
resumen = {}

for lenguaje in lenguajes:
    if lenguaje in resumen:
        resumen[lenguaje] += 1
    else:
        resumen[lenguaje] = 1
```

Este patrón se utiliza para:

- contar palabras de un texto;
- contar votos;
- resumir goles por selección;
- contar productos vendidos;
- identificar categorías repetidas;
- construir tablas de frecuencia.

---

# 18. ¿Cuándo utilizar un diccionario?

Conviene utilizar un diccionario cuando:

- necesitamos buscar información mediante una clave;
- cada elemento tiene un identificador;
- deseamos relacionar dos piezas de información;
- queremos contar elementos repetidos;
- necesitamos acumular cantidades por categoría;
- queremos agrupar varios valores bajo una misma clave;
- necesitamos resumir información.

## Ejemplos de aplicaciones

- Agenda: nombre → teléfono.
- Inventario: código → cantidad disponible.
- Campeonato: equipo → puntaje.
- Registro académico: estudiante → lista de notas.
- Conteo de palabras: palabra → cantidad de apariciones.
- Ventas: vendedor → total vendido.

---

# 19. Buenas prácticas

## Utilizar nombres descriptivos

```python
edades_estudiantes = {}
```

Es preferible a:

```python
d = {}
```

## Elegir una clave adecuada

La clave debe representar el criterio que se utilizará para buscar.

## Verificar antes de acceder

```python
if clave in diccionario:
    print(diccionario[clave])
```

## Recordar que las claves no se repiten

Si se asigna un nuevo valor a una clave existente, el valor anterior se reemplaza.

```python
puntajes = {"Ana": 15}
puntajes["Ana"] = 20
```

Resultado:

```python
{"Ana": 20}
```

---

# 20. Ideas clave de la lectura

- Un diccionario almacena pares **clave–valor**.
- La clave se utiliza como criterio de búsqueda.
- Las claves no se repiten.
- Los valores sí pueden repetirse.
- Una clave no representa una posición.
- `clave in diccionario` verifica si la clave existe.
- La búsqueda por clave es directa.
- La búsqueda por valores generalmente requiere recorrer el diccionario.
- Una asignación puede agregar o actualizar un elemento.
- Un diccionario puede funcionar como contador.
- Un diccionario puede funcionar como acumulador.
- El valor de un diccionario puede ser una lista.
- Los diccionarios permiten resumir elementos repetidos.

---

# 21. Preguntas de reflexión

Responde las siguientes preguntas después de completar la lectura.

## Pregunta 1

Explica con tus propias palabras la diferencia entre una lista y un diccionario.

---

## Pregunta 2

En el siguiente diccionario, identifica las claves y los valores:

```python
capitales = {
    "Ecuador": "Quito",
    "Perú": "Lima",
    "Chile": "Santiago"
}
```

---

## Pregunta 3

¿Por qué un número de cédula puede ser una buena clave para un diccionario?

---

## Pregunta 4

¿Qué verifica la siguiente expresión?

```python
"Luis" in edades
```

---

## Pregunta 5

¿La siguiente expresión busca en las claves o en los valores?

```python
18 in edades.values()
```

---

## Pregunta 6

Observa el siguiente diccionario:

```python
productos = {
    "P001": "Teclado",
    "P002": "Mouse",
    "P003": "Monitor"
}
```

Indica qué tipo de búsqueda se realiza en cada caso:

### a.

```python
"P002" in productos
```

### b.

```python
"Mouse" in productos.values()
```

### c.

Encontrar el código correspondiente al producto `"Monitor"`.

---

## Pregunta 7

Observa la lista:

```python
lenguajes = [
    "Python",
    "Java",
    "Python",
    "C++",
    "Java",
    "Python"
]
```

Sin escribir código, indica cómo quedaría el diccionario que resume la cantidad de veces que aparece cada lenguaje.

---

## Pregunta 8

Observa:

```python
notas = {
    "Ana": [18, 20, 19],
    "Luis": [15, 17]
}
```

¿Qué representa cada clave?  
¿Qué representa cada lista?

---

## Pregunta 9

Explica la diferencia entre utilizar un diccionario como contador y utilizarlo como acumulador.

---

# 22. Actividad de identificación

Dado el siguiente diccionario:

```python
puntajes = {
    "Ana": 18,
    "Luis": 15,
    "Carlos": 20
}
```

Completa la tabla:

| Pregunta | ¿Se busca por clave o por valor? | ¿Es directa o secuencial? |
|---|---|---|
| ¿Está `"Ana"` registrada? |  |  |
| ¿Cuál es el puntaje de `"Carlos"`? |  |  |
| ¿Existe un puntaje igual a `15`? |  |  |
| ¿Quién obtuvo `20` puntos? |  |  |

---

# 23. Mini retos conceptuales

## Reto 1: agenda

Dado:

```python
telefonos = {
    "Ana": "0991111111",
    "Luis": "0982222222"
}
```

Escribe la instrucción necesaria para:

1. Consultar el teléfono de Luis.
2. Agregar el teléfono de Carlos.
3. Actualizar el teléfono de Ana.
4. Verificar si Pedro está registrado.

---

## Reto 2: contador

Construye manualmente el diccionario que resume la siguiente lista:

```python
equipos = [
    "Ecuador",
    "Brasil",
    "Ecuador",
    "Argentina",
    "Brasil",
    "Ecuador"
]
```

---

## Reto 3: acumulador

Considera:

```python
ventas = [
    ["Ana", 10],
    ["Luis", 5],
    ["Ana", 20]
]
```

¿Cuál debería ser el contenido final del diccionario `totales`?

---

## Reto 4: valores que son listas

Dado:

```python
cursos = {
    "Programación": ["Ana", "Luis"],
    "Matemáticas": ["Carlos", "Ana"]
}
```

Responde:

1. ¿Cuál es la clave para consultar los estudiantes de Programación?
2. ¿Qué tipo de dato es el valor asociado a `"Programación"`?
3. ¿Cómo agregarías a Pedro a la lista de Programación?

---

# 24. Para la próxima clase

Durante la clase se resolverán problemas en los que se utilizarán diccionarios para:

- contar elementos repetidos;
- acumular cantidades;
- construir resúmenes;
- buscar información por clave;
- buscar información recorriendo valores;
- manejar listas almacenadas como valores;
- representar puntajes, ventas, notas y resultados.

Antes de asistir a clase, asegúrate de comprender especialmente las siguientes ideas:

1. Qué representa una clave.
2. Qué representa un valor.
3. Cómo funciona el operador `in`.
4. Cuándo la búsqueda es directa.
5. Cuándo es necesario recorrer el diccionario.
6. La diferencia entre contador y acumulador.
