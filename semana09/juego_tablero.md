# Solución propuesta

```python
import random as rd

############################################################
# 1. Configuración inicial
############################################################
# 1.1 Inicializar las variables del juego
puntaje = 0
posicion = 0

# 1.2 Crear el tablero de 30 casillas vacías
tablero = [""] * 30

# 1.3 Crear los comodines
comodines = ["Gema", "Bandido", "Camino", "Atajo"]*2


# 1.4 Seleccionar ocho posiciones aleatorias del tablero
posiciones = list(range(30))
pos_comodines = rd.sample(posiciones, 8)

# 1.5 Colocar los comodines en el tablero
for pos in pos_comodines:
    tablero[pos] = comodines.pop()

############################################################
# 2. Mecánica del juego
############################################################
while True:

    # 2.1 Lanzar el dado y avanzar
    dado = rd.randint(1, 6)
    posicion += dado

    # 2.2 Verificar si llegó al final del tablero
    if posicion >= 30:
        break

    # 2.3 Aplicar el efecto del comodín
    if tablero[posicion] == "Gema":
        puntaje += 10000

    elif tablero[posicion] == "Bandido":
        puntaje -= 5000

    elif tablero[posicion] == "Camino":
        puntaje -= 1000

    elif tablero[posicion] == "Atajo":
        puntaje += 500

    # 2.4 Mostrar el estado del juego
    print(f"Obtuvo {dado} en el dado.")
    print(f"Se encuentra en la casilla {posicion}.")

    if tablero[posicion] != "":
        print(f"Cayó en un {tablero[posicion]}.")

    print(f"Su puntaje es {puntaje} puntos.")
    print()

############################################################
# 3. Verificar el resultado del juego
############################################################
if puntaje >= 10000:
    print(f"¡Ha ganado con {puntaje} puntos!")
else:
    print(f"Ha perdido. Terminó con {puntaje} puntos.")
```

---

# Explicación de la solución

La solución se divide en **tres grandes etapas**, siguiendo el enfoque **Top-Down**.

## 1. Configuración inicial

Antes de comenzar el juego se realizan todas las tareas que ocurren una sola vez:

- Inicializar el puntaje y la posición del jugador.
- Crear el tablero de 30 casillas.
- Crear los ocho comodines.
- Seleccionar ocho posiciones aleatorias sin repetir.
- Colocar los comodines en el tablero.

---

## 2. Mecánica del juego

El juego se desarrolla mediante un ciclo `while True`, donde cada iteración representa **un turno**.

En cada turno se realizan las siguientes acciones:

1. Lanzar el dado.
2. Avanzar el jugador.
3. Verificar si llegó al final del tablero.
4. Aplicar el efecto del comodín.
5. Mostrar el estado actual del juego.

Cuando el jugador llega o supera la última casilla (`posicion >= 30`), el ciclo termina mediante la instrucción `break`.

---

## 3. Resultado final

Al terminar el recorrido del tablero se verifica el puntaje obtenido.

- Si el jugador acumuló **10 000 puntos o más**, gana la partida.
- En caso contrario, pierde el juego.