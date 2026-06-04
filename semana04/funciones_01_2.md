# Ejercicio: Solución de Ecuaciones Cuadráticas

Una ecuación cuadrática tiene la forma:

![Forma de la ecuación cuadrática](img/forma_ecuacion_cuadratica.png)

Las soluciones de la ecuación se calculan mediante la fórmula:

![Fórmula general](img/formula_general.png)

Puede asumir que todas las ecuaciones ingresadas tienen soluciones reales.

---

## Parte 1: Definición de la función

Escriba una función llamada `resolver_cuadratica(a, b, c)` que reciba los coeficientes de una ecuación cuadrática y retorne las dos soluciones de la ecuación.

La función debe realizar el cálculo usando los valores recibidos en sus parámetros y debe retornar las dos soluciones usando una única instrucción `return`.

### Ejemplo

```python
x1, x2 = resolver_cuadratica(1, -11, 24)
```

Las soluciones retornadas son:

```text
x1 = 8.0
x2 = 3.0
```

---

## Parte 2: Programa principal

Escriba un programa que solicite los coeficientes de tres ecuaciones cuadráticas.

Para cada ecuación, el usuario debe ingresar los tres coeficientes en una sola línea separados por espacios.

Cada línea ingresada debe separarse para obtener los valores de `a`, `b` y `c` por separado. Luego, estos valores deben convertirse a números antes de invocar la función.

Después de invocar la función, el programa debe mostrar:

* los tres coeficientes extraídos de la línea ingresada;
* las dos soluciones calculadas por la función.

---

## Instrucciones

1. Solicite los coeficientes de tres ecuaciones cuadráticas.
2. Los tres coeficientes de cada ecuación deben ingresarse en una sola línea separados por espacios.
3. Obtenga por separado los valores de `a`, `b` y `c` a partir de cada línea ingresada.
4. Convierta los coeficientes a valores numéricos.
5. Invoque la función `resolver_cuadratica` exactamente tres veces, una vez por cada ecuación.
6. Almacene las soluciones retornadas por la función en variables.
7. Muestre los coeficientes extraídos de cada línea de entrada.
8. Muestre las dos soluciones de cada ecuación con dos decimales.
9. No utilice lazos. La función debe reutilizarse mediante tres invocaciones independientes.

---

## Ejemplo de ejecución

```text
Ecuación 1
Ingrese a, b y c: 1 -11 24

Ecuación 2
Ingrese a, b y c: 1 -5 6

Ecuación 3
Ingrese a, b y c: 1 -7 10

Coeficientes ecuación 1:
a = 1
b = -11
c = 24
x1 = 8.00
x2 = 3.00

Coeficientes ecuación 2:
a = 1
b = -5
c = 6
x1 = 3.00
x2 = 2.00

Coeficientes ecuación 3:
a = 1
b = -7
c = 10
x1 = 5.00
x2 = 2.00
```

---

## Importante

El objetivo principal del ejercicio es practicar el uso de funciones.

Por lo tanto, el cálculo de las soluciones debe escribirse una sola vez dentro de la función `resolver_cuadratica`.

Desde el programa principal, la función debe reutilizarse tres veces, enviando diferentes argumentos en cada invocación.
