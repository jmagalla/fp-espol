# u2: Ejercicios con con Cadenas, Listas y Funciones

## Ejercicio 1

Escriba una función de nombre `cambiar_pal(palabra, caracter)` que recibe dos cadenas. La primera es la `palabra` a cambiar y la segunda es el `caracter` de reemplazo. La función debe retornar la palabra cambiada de la siguiente manera: dada la primera letra de la `palabra` cambiar las siguientes letras que coincidan con la primera por el `caracter` de reemplazo. Ejemplos de la llamada a la función: 

```
cambiar_pal("babero bonito", "+") -> "ba+ero +onito"
cambiar_pal("coca cola", "#") -> "co#a #ola"
cambiar_pal("ardilla", "$") -> "ardill$"
```

## Ejercicio 2

Escriba una función `mezclar_palabras(a, b)` que recibe dos cadenas `a` y `b`. La función debe retornar una sola cadena concatenando `a` y `b` separadas por un espacio, pero intercambie los primeros caracteres de cada cadena. Ejemplos de la llamada a la función:

```
mezclar_palabras("mix", "pod") -> "pox mid"
mezclar_palabras("dog", "dinner") -> "dig donner"
```

## Ejercicio 3

Escriba una función `long_max(lista)` que recibe una `lista` de 3 cadenas. La función debe retornar la longitud de la cadena más larga. Pista: use las funciones de las cadenas y no utilice lazos de repetición.
```
long_max(["novia", "telemaco", "penelope"]) -> 6
long_max(["tesista", "calamitoso", "pesadez") -> 10
long_max(["magallanes", "villafuerte", "zambrano"]) -> 11 
```

## Ejercicio 4

Escriba una función `producto_escalar(v1, v2)` que recibe dos listas. Cada lista tiene 3 enteros y representa a un vector en `R3(x, y, z)`. 

La función debe retornar el resultado del producto escalar entre los dos vectores. Use la siguiente fórmula:

![Fórmula del producto escalar](images/f1_producto_escalar.png)

Ejemplo de la llamada a la función:

```
producto_escalar([1, 4, -1], [-1, 6, 3]) -> 20
producto_escalar([3, -3, -2], [2, 4, 0]) -> -6
```