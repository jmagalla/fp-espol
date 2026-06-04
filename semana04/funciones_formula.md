# Actividad de Refuerzo: Funciones y Parámetros

## Objetivo

Practicar la definición de funciones, el uso de parámetros, el retorno de valores y la invocación de funciones desde un programa principal.

---

# Cálculo del Índice de Masa Corporal (IMC)

El Índice de Masa Corporal (IMC) es una medida utilizada para relacionar el peso y la altura de una persona. Se calcula mediante la siguiente fórmula:

[
IMC = \frac{peso_{kg}}{altura_{m}^{2}}
]

Considere las siguientes equivalencias:

* 1 libra = 0.453592 kilogramos
* 1 pulgada = 0.0254 metros

---

## Parte 1: Definición de la función

Escriba una función llamada `calcular_imc(peso_libras, altura_pulgadas)` que reciba el peso en libras y la altura en pulgadas de una persona, y retorne su Índice de Masa Corporal (IMC).

### Recibe

* `peso_libras`: número real que representa el peso en libras.
* `altura_pulgadas`: número real que representa la altura en pulgadas.

### Retorna

* Un número real correspondiente al IMC calculado.

### Ejemplo

Entrada:

```python
calcular_imc(180, 72)
```

Salida:

```text
24.41
```

---

## Parte 2: Programa principal

Escriba un programa que solicite los datos de tres jugadores de béisbol.

### Jugador 1

Solicite:

* Peso en libras.
* Altura en pulgadas.

### Jugador 2

Solicite:

* Peso en libras.
* Altura en pulgadas.

### Jugador 3

Solicite:

* Peso en libras.
* Altura en pulgadas.

---

## Requisitos

1. Utilice la función `calcular_imc` para realizar todos los cálculos.
2. La función debe ser invocada exactamente tres veces.
3. Almacene cada resultado en una variable diferente.
4. Muestre el IMC de cada jugador con dos decimales.

---

## Ejemplo de ejecución

```text
Jugador 1
Peso (lb): 180
Altura (pulg): 72

Jugador 2
Peso (lb): 210
Altura (pulg): 74

Jugador 3
Peso (lb): 165
Altura (pulg): 70

IMC jugador 1: 24.41
IMC jugador 2: 26.96
IMC jugador 3: 23.67
```

---

## Entregable

Suba un archivo llamado `imc.py` que contenga:

* La definición de la función `calcular_imc`.
* El programa principal que solicite los datos de los tres jugadores.
* La impresión de los tres resultados.
