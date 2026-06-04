# Ejercicio: Batalla Pokemons diccionarios

## Objetivo general
En este ejercicio se busca reforzar el uso de **listas**, **diccionarios** y **funciones** en Python. A partir de listas de cadenas, el estudiante deberá transformar la información en diccionarios y aplicar reglas simples para calcular el **puntaje efectivo** de un Pokémon frente a otro.

## Descripción de las listas de datos

### Lista de Pokémons
La siguiente lista contiene información básica de algunos Pokémon. Cada cadena representa un Pokémon y tiene el formato:

`id|nombre|tipo|puntaje`

```python
base_pokemons = [
    "1|Bulbasaur|GRASS|49",
    "2|Ivysaur|GRASS|62",
    "3|Charmander|FIRE|52",
    "4|Squirtle|WATER|48"
]
```

### Lista de reglas de tipos
Cada línea identifica **un tipo de Pokémon** y, a continuación, los **tipos de Pokémon contra los que su puntaje de ataque se duplica**.

Formato de cada cadena:

`tipo|tipos_que_duplica`

Los tipos contra los que se duplica el puntaje están separados por el carácter `/`.

Ejemplo:

La cadena:

```
GRASS|WATER/ROCK
```

indica que un Pokémon de tipo **GRASS** duplica su puntaje de ataque cuando se enfrenta a Pokémon de tipo **WATER** o **ROCK**.

```python
tipos_pokemons = [
    "GRASS|WATER/ROCK",
    "FIRE|GRASS",
    "WATER|FIRE"
]
```

## 1. Diccionario simple (id → nombre)
Implemente la función `crearDiccionarioNombres(lista)` que reciba la lista `base_pokemons` y retorne un diccionario donde:

- La clave sea el **id del Pokémon** (entero)
- El valor sea el **nombre del Pokémon** (cadena)

Diccionario esperado:

```python
{1: "Bulbasaur", 2: "Ivysaur", 3: "Charmander", 4: "Squirtle"}
```

## 2. Diccionario con lista simple como valor
Implemente la función `crearDiccionarioPokemons(lista)` que transforme la lista `base_pokemons` en un diccionario donde:

- La clave sea el **id del Pokémon**
- El valor sea una lista con `[nombre, tipo, puntaje]`

Diccionario esperado:

```python
{
  1: ["Bulbasaur", "GRASS", 49],
  2: ["Ivysaur", "GRASS", 62],
  3: ["Charmander", "FIRE", 52],
  4: ["Squirtle", "WATER", 48]
}
```

## 3. Diccionario de tipos que duplican puntaje
Implemente la función `crearDiccionarioTipos(lista)` que transforme la lista `tipos_pokemons` en un diccionario donde:

- La clave sea el **tipo de Pokémon**
- El valor sea una **lista simple** con los tipos de Pokémon contra los que el puntaje se duplica

Diccionario esperado:

```python
{
  "GRASS": ["WATER", "ROCK"],
  "FIRE": ["GRASS"],
  "WATER": ["FIRE"]
}
```

## 4. Calcular puntaje efectivo
Implemente la función:

```python
calcularPuntajeEfectivo(id_atacante, id_defensor, dic_pokemons, dicTipos)
```

La función debe:

1. Obtener el **tipo** y el **puntaje base** del Pokémon atacante
2. Obtener el **tipo** del Pokémon defensor
3. Verificar si el tipo del defensor está en la lista de tipos que duplican el puntaje del atacante
4. Si se cumple la condición anterior, el puntaje efectivo será el doble del puntaje base
5. En caso contrario, el puntaje efectivo será el puntaje base
6. Retornar el puntaje efectivo

## 5. Programa principal: simulación de batalla Pokémon
Implemente un **programa principal** que utilice las funciones desarrolladas anteriormente para simular una batalla Pokémon.

En el programa principal se debe:

1. Definir las listas `base_pokemons` y `tipos_pokemons`
2. Crear los diccionarios necesarios usando las funciones implementadas
3. Seleccionar **dos Pokémon distintos al azar**
4. Calcular el puntaje efectivo de cada Pokémon
5. Comparar los puntajes efectivos y determinar el ganador
6. Mostrar el resultado de la simulación en pantalla

Es responsabilidad del estudiante **definir correctamente el orden de las llamadas a las funciones** para que la simulación funcione correctamente.

Extracto esperado del programa principal:

```python
# Programa principal
base_pokemons = [
    "1|Bulbasaur|GRASS|49",
    "2|Ivysaur|GRASS|62",
    "3|Charmander|FIRE|52",
    "4|Squirtle|WATER|48"
]

tipos_pokemons = [
    "GRASS|WATER/ROCK",
    "FIRE|GRASS",
    "WATER|FIRE"
]

# A partir de aquí deben llamarse las funciones implementadas
# para resolver la simulación de la batalla
```

Ejemplo de salida esperada:

```text
Pokémon 1: Bulbasaur (GRASS) - Puntaje efectivo: 98
Pokémon 2: Squirtle (WATER) - Puntaje efectivo: 48
Ganador: Bulbasaur
```


