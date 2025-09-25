# Ejercicio: Transformación de palabras con índices

Escribe un programa en Python que transforme una palabra de **exactamente 5 letras** siguiendo una regla de sustitución de letras.

Para ello, se usa la siguiente correspondencia de letras:

```
Original :  abcdefghijklmnñopqrstuvwxyz
Sustituta:  nflqtkourcyavjdhweiñmxgpzbs
```

---

## Instrucciones (transformación en varias instrucciones)

1. Lee la palabra original (debe tener exactamente 5 letras).
2. Verifica que la longitud de la palabra sea 5; si no, muestra un mensaje de error.
3. Para la primera letra:
   - Busca su índice en la cadena `alfabeto`.
   - Obtén la letra correspondiente en `sustituta` usando ese índice.
   - Guarda esa letra como `letra1`.
4. Repite el paso 3 para la segunda letra y guárdala como `letra2`.
5. Repite el paso 3 para la tercera letra y guárdala como `letra3`.
6. Repite el paso 3 para la cuarta letra y guárdala como `letra4`.
7. Repite el paso 3 para la quinta letra y guárdala como `letra5`.
8. Concatena `letra1 + letra2 + letra3 + letra4 + letra5` para formar la `nueva_palabra`.
9. Muestra la `nueva_palabra`.

---

## Código fuente (sin bucles, usando índices paso a paso)

```python
# correspondencia
alfabeto  = "abcdefghijklmnñopqrstuvwxyz"
sustituta = "nflqtkourcyavjdhweiñmxgpzbs"

# 1) Entrada de palabra
palabra_original = input("Ingrese una palabra de exactamente 5 letras: ").strip().lower()

# 2) Validar longitud
if len(palabra_original) != 5:
    ## Complete aquí el código
else:
    ## Complete aquí el código
    nueva_palabra = ""

    # 9) Mostrar
    print("Palabra transformada:", nueva_palabra)
```

---

## Actividad de refuerzo

1. Modifica el programa para que funcione con palabras de 3 letras en lugar de 5.

2. Explica en tu cuaderno el paso a paso de la transformación de la palabra "sol":

* ¿Qué índice ocupa la s en el alfabeto original?

* ¿Qué letra corresponde en la cadena sustituta?

* Repite para o y l.

* Escribe la palabra resultante.