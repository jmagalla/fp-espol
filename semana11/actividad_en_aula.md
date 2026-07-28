# Actividad en aula: Diccionarios en Python

**Modalidad:** Trabajo en grupos (2–3 estudiantes)  
**Duración:** 60 minutos

## Objetivo general

Aplicar el uso de diccionarios para resolver problemas de búsqueda, conteo, acumulación y organización de información mediante funciones.

## Resultados de aprendizaje

Al finalizar la actividad el estudiante será capaz de:

- Identificar cuándo utilizar una búsqueda directa mediante una clave.
- Diferenciar una búsqueda directa de una búsqueda secuencial.
- Utilizar un diccionario como contador.
- Utilizar un diccionario como acumulador.
- Manipular diccionarios cuyos valores son listas.
- Implementar funciones que reciben y retornan diccionarios.

---

# Contexto

Una biblioteca comunitaria desea desarrollar un pequeño sistema para administrar sus socios y registrar los préstamos de libros realizados durante el día.

Cada parte de esta actividad representa una necesidad diferente del sistema. Analice el problema antes de escribir la solución.

---

# Parte 1. Administración de socios

La biblioteca almacena la información de sus socios utilizando el siguiente diccionario.

```python
socios = {
    101:["Ana",20],
    205:["Luis",19],
    310:["Carla",23],
    415:["Mario",21]
}
```

Cada clave representa el número de socio y cada valor contiene el nombre y la edad del socio.

### Actividades

a) Implemente la función `buscar_socio(id_socio, socios)` que retorne el nombre y la edad del socio correspondiente al ID recibido. Si el socio no existe, retorne un mensaje indicando que no fue encontrado.
b) Implemente la función `socio_mayor(socios)` que retorne el ID y el nombre del socio de mayor edad.
c) Implemente la función `edad_total(socios)` que retorne la suma de las edades de todos los socios.
d) Implemente la función `agregar_socio(entrada, socios)` donde la variable `entrada` tiene el siguiente formato:

```text
520 Pedro 18
```

La función deberá agregar el nuevo socio al diccionario.

---

# Parte 2. Registro de préstamos

Durante el día se registran los préstamos realizados mediante la siguiente lista.

```python
prestamos = [
    "101-2",
    "205-1",
    "101-3",
    "310-2",
    "205-4",
    "101-1",
    "415-2",
    "310-1"
]
```

Cada elemento representa:

```text
idSocio-cantidadLibros
```

### Actividades

a) Implemente la función `total_prestamos(prestamos)` que construya un diccionario donde la clave sea el ID del socio y el valor sea el total de libros prestados.

Ejemplo del resultado esperado:

```python
{
    101:6,
    205:5,
    310:3,
    415:2
}
```

b) Implemente la función `mayor_prestamo(diccionario)` que retorne el ID del socio que retiró la mayor cantidad de libros y el total correspondiente.

---

# Parte 3. Encuesta de satisfacción

Al devolver un libro, cada socio responde una encuesta de satisfacción.

```python
respuestas = [
    "Excelente",
    "Bueno",
    "Bueno",
    "Regular",
    "Excelente",
    "Bueno",
    "Excelente",
    "Malo",
    "Bueno",
    "Regular",
    "Excelente"
]
```

### Actividades

a) Implemente la función `contar_respuestas(respuestas)` que construya un diccionario con la frecuencia de cada respuesta.

Ejemplo:

```python
{
    "Excelente":4,
    "Bueno":4,
    "Regular":2,
    "Malo":1
}
```

b) Implemente la función `respuesta_frecuente(diccionario)` que retorne la respuesta que aparece más veces y su frecuencia.

---

# Parte 4. Traductor de géneros

La biblioteca utiliza los siguientes nombres para clasificar los géneros de los libros.

```python
generos = {
    "novela":"Novel",
    "cuento":"Story",
    "poesia":"Poetry",
    "historia":"History",
    "ciencia":"Science"
}
```

### Actividades

Implemente la función:

```python
traducir_genero(genero, modo, generos)
```

donde:

- `modo = 1` traduce de español a inglés.
- `modo = 2` traduce de inglés a español.

Si la traducción no existe, la función deberá retornar el mensaje:

```text
"La traducción no está disponible."
```

> **Importante:** Analice cuidadosamente qué tipo de búsqueda debe realizar en cada modo de traducción.

---

# Parte 5. Clasificación de libros por autor

La biblioteca desea registrar los libros disponibles por autor.

Cada vez que llega un nuevo libro se registra mediante una cadena con el siguiente formato:

```python
libros = [
    "Cervantes-Don Quijote",
    "García Márquez-Cien años de soledad",
    "Cervantes-Novelas ejemplares",
    "Borges-El Aleph",
    "García Márquez-El coronel no tiene quien le escriba",
    "Borges-Ficciones"
]
```

### Actividades

a) Implemente la función `agrupar_libros(libros)` que construya un diccionario donde la clave sea el autor y el valor sea una lista con los títulos escritos por dicho autor.

Ejemplo:

```python
{
    "Cervantes":[
        "Don Quijote",
        "Novelas ejemplares"
    ],
    "Borges":[
        "El Aleph",
        "Ficciones"
    ]
}
```

b) Implemente la función `mostrar_autor(nombre_autor, diccionario)` que muestre todos los libros escritos por el autor recibido como parámetro. Si el autor no existe, deberá indicarlo mediante un mensaje.

---

# Parte 6. Análisis y reflexión

Responda de manera breve las siguientes preguntas.

a) En la Parte 1, ¿por qué resulta más conveniente utilizar un diccionario que una lista para buscar un socio mediante su ID?
b) En la Parte 4, ¿por qué el modo 1 puede resolverse mediante una búsqueda directa y el modo 2 requiere recorrer el diccionario?
c) Compare las soluciones de las Partes 2 y 3. Aunque ambas utilizan diccionarios, ¿qué representa el valor almacenado en cada una?
d) En la Parte 5, ¿por qué el valor del diccionario es una lista y no una cadena?
e) Mencione una situación de la vida real en la que utilizaría:
- un diccionario como contador;
- un diccionario como acumulador;
- un diccionario cuyos valores sean listas.

---

# Entregables

Cada grupo deberá entregar:

- Las funciones implementadas para cada una de las partes.
- Las respuestas de la sección de análisis y reflexión.
- Los algoritmos deben escribirse utilizando únicamente los conceptos estudiados en clase (funciones, listas, cadenas, diccionarios, estructuras de decisión y repetición). No utilice listas de listas, listas de tuplas ni módulos adicionales.