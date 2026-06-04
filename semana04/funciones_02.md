# Ejercicio 2

Escriba una función `transforma(s)` que reciba una cadena `s` y retorne una nueva cadena formada por la concatenación de los dos primeros caracteres y los dos últimos caracteres de la cadena.

Suponer que la cadena tiene al menos 2 caracteres.

### Recibe

* `s`: una cadena de caracteres.

### Retorna

* Una cadena formada por los dos primeros y los dos últimos caracteres de `s`.

### Ejemplo

```python
transforma("Sprite")
```

retorna

```text
Spte
```

## Programa principal

Escriba un programa que:

1. Solicite tres palabras al usuario.
2. Invoque la función `transforma` una vez para cada palabra.
3. Almacene cada resultado en una variable diferente.
4. Muestre los tres resultados obtenidos.

### Ejemplo de ejecución

```text
Ingrese palabra 1: Sprite
Ingrese palabra 2: Python
Ingrese palabra 3: Computadora

Resultado 1: Spte
Resultado 2: Pyon
Resultado 3: Cora
```

---

# Ejercicio 3

Escriba una función `corregir(s)` que reciba una cadena `s` y retorne una nueva cadena donde todas las ocurrencias del primer carácter sean reemplazadas por el símbolo `*`, excepto la primera ocurrencia.

### Recibe

* `s`: una cadena de caracteres.

### Retorna

* Una nueva cadena con las modificaciones indicadas.

### Ejemplo

```python
corregir("babble")
```

retorna

```text
ba**le
```

## Programa principal

Escriba un programa que:

1. Solicite tres palabras al usuario.
2. Invoque la función `corregir` para cada palabra.
3. Almacene los resultados en tres variables.
4. Muestre los tres resultados obtenidos.

### Ejemplo de ejecución

```text
Ingrese palabra 1: babble
Ingrese palabra 2: abracadabra
Ingrese palabra 3: programar

Resultado 1: ba**le
Resultado 2: abr*c*d*br*
Resultado 3: program*r
```

---

# Ejercicio 4

Escriba una función `mezclar(a, b)` que reciba dos cadenas `a` y `b` y retorne una nueva cadena formada por ambas palabras separadas por un espacio, intercambiando los dos primeros caracteres de cada palabra.

Puede asumir que ambas cadenas tienen al menos 2 caracteres.

### Recibe

* `a`: primera cadena.
* `b`: segunda cadena.

### Retorna

* Una nueva cadena con los dos primeros caracteres intercambiados.

### Ejemplos

```python
mezclar("mix", "pod")
```

retorna

```text
pox mid
```

```python
mezclar("dog", "dinner")
```

retorna

```text
dig donner
```

## Programa principal

Escriba un programa que:

1. Solicite tres pares de palabras al usuario.
2. Invoque la función `mezclar` para cada par de palabras.
3. Almacene cada resultado en una variable diferente.
4. Muestre los tres resultados obtenidos.

### Ejemplo de ejecución

```text
Par 1
Ingrese palabra A: mix
Ingrese palabra B: pod

Par 2
Ingrese palabra A: dog
Ingrese palabra B: dinner

Par 3
Ingrese palabra A: casa
Ingrese palabra B: perro

Resultado 1: pox mid
Resultado 2: dig donner
Resultado 3: pesa carro
```
