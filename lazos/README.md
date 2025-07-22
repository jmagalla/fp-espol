# TEMA 1

# Juego de Adivinar Premios

Vas a programar un pequeño juego donde el jugador debe **adivinar 3 premios seleccionados al azar** antes de quedarse sin vidas.

## 1. Lista de premios disponibles

Al inicio del programa, muestra una lista de premios predefinidos. Por ejemplo:

```python
l_premios = ["Carro", "Moto", "Televisor", "Celular", "Smartwatch", "Chocolate"]
```

## 2. Selección secreta

El programa debe seleccionar **3 premios distintos al azar** de la lista anterior. Estos serán los premios que el jugador debe adivinar.  
**No deben mostrarse al usuario.**

Puedes usar `random.sample(l_premios, 3)` para seleccionar sin repetición.

## 3. Vidas del jugador

El jugador empieza con **2 vidas**. En cada intento:

- Si el jugador **adivina uno de los premios seleccionados**, mantiene sus vidas.
- Si el jugador **falla**, pierde una vida.

## 4. Ciclo del juego

Mientras el jugador tenga **vidas disponibles** y aún no haya adivinado los **3 premios secretos**, se debe:

1. Mostrar cuántas vidas le quedan.
2. Pedir que ingrese el nombre de un premio.
3. Informar si acertó o no.
4. Actualizar el estado del juego.

> Asume que el jugador **no ingresará un premio repetido**.

## 5. Final del juego

- Si el jugador adivina los 3 premios secretos antes de quedarse sin vidas, mostrar:  
  `Ganó 🎉`
- Si se queda sin vidas antes de adivinar los 3 premios, mostrar:  
  `Perdió 😢`

## 6. Ejemplo de ejecución

```
Adivine los 3 premios seleccionados:
["Carro", "Moto", "Televisor", "Celular", "Smartwatch", "Chocolate"]

Vidas: 2
Ingrese un premio: Celular
Adivinó

Vidas: 2
Ingrese un premio: Carro
No Adivinó

Vidas: 1
Ingrese un premio: Moto
Adivinó

Vidas: 1
Ingrese un premio: SmartWatch
No Adivinó

Perdió
```
