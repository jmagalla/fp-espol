# Actividad: Camino a la Final del Mundial 2026

## Objetivo

Desarrollar un programa en Python que simule el recorrido de una selección de fútbol durante el Mundial 2026.

A partir de la descripción del problema, el estudiante deberá identificar y definir:

- Las variables necesarias.
- Los valores que deben acumularse.
- Las listas que requiere el programa.
- Los eventos aleatorios.
- La condición de continuación del ciclo.
- Las condiciones que provocan la finalización de la simulación.

**Tiempo estimado:** 60 minutos.

---

# Descripción de la simulación

Una selección de fútbol participa en el Mundial 2026 y debe recorrer un camino compuesto por **30 posiciones** para llegar al estadio donde se disputará la final.

La selección comienza en la posición inicial del recorrido. Durante cada turno, se lanza un dado de seis caras y la selección avanza la cantidad de posiciones obtenida.

Por ejemplo, si la selección se encuentra en la posición 5 y obtiene un 4 en el dado, avanzará hasta la posición 9.

Si el resultado del dado hace que la selección sobrepase la última posición del recorrido, deberá ubicarse directamente en la posición 30.

La selección inicia el juego con **10 puntos de energía**. Cada turno realizado consume **1 punto de energía**, debido al esfuerzo de viajar, entrenar y disputar partidos.

Durante el recorrido existen eventos especiales distribuidos en posiciones seleccionadas al azar. **Las posiciones de los eventos no pueden repetirse.**

Los eventos son los siguientes:

## Centro médico

La selección recibe atención médica y recupera **3 puntos de energía**.

## Lesión

Uno de los jugadores sufre una lesión y la selección pierde **4 puntos de energía**.

## Patrocinio

La selección recibe apoyo adicional y suma **una victoria** a su registro.

## Partido difícil

La selección debe lanzar nuevamente el dado.

- Si obtiene un valor entre **4 y 6**, gana el partido y registra una victoria.
- Si obtiene un valor entre **1 y 3**, pierde el partido y además pierde **2 puntos de energía**.

En el recorrido deben existir exactamente:

- 3 Centros médicos.
- 3 Lesiones.
- 2 Patrocinios.
- 2 Partidos difíciles.

Después de cada turno, el programa debe mostrar:

- Resultado obtenido en el dado.
- Posición actual.
- Energía restante.
- Cantidad de victorias.
- Evento ocurrido (si existe).

La simulación debe continuar mientras la selección todavía pueda avanzar hacia la final.

El juego puede terminar de dos maneras:

1. La selección llega a la posición 30.
2. La selección se queda sin energía antes de llegar a la posición 30.

Al finalizar, el programa debe indicar si la selección logró llegar a la final o si fue eliminada durante el recorrido.

También debe mostrar:

- Total de victorias obtenidas.
- Energía restante.

---

# Fases de desarrollo

## Fase 1. Análisis del problema

Antes de comenzar a programar, analicen el problema utilizando las siguientes preguntas como guía para diseñar la solución. Estas preguntas no forman parte del entregable.

1. ¿Qué datos cambian durante la simulación?
2. ¿Qué dato representa el avance de la selección?
3. ¿Qué dato debe aumentar cada vez que se obtiene una victoria?
4. ¿Qué estructura puede representar las 30 posiciones del recorrido?
5. ¿Cómo se pueden almacenar los diferentes tipos de eventos?
6. ¿Qué elementos deben generarse aleatoriamente?
7. ¿Cuáles son las dos situaciones que pueden finalizar el juego?
8. ¿Qué condición debe cumplirse para que el ciclo continúe?

El docente podrá realizar preguntas sobre esta fase durante el desarrollo de la actividad.

---

## Fase 2. Configuración inicial

Prepare los datos necesarios para iniciar el juego.

El programa debe:

- Establecer la posición inicial de la selección.
- Establecer la energía inicial.
- Inicializar el registro de victorias.
- Crear el recorrido de 30 posiciones.
- Definir los eventos.
- Ubicar los eventos en posiciones aleatorias sin repetir posiciones.

---

## Fase 3. Simulación del recorrido

Implemente el ciclo principal del juego.

En cada turno el programa debe:

1. Lanzar el dado.
2. Actualizar la posición.
3. Evitar que la posición supere el final del recorrido.
4. Reducir la energía correspondiente al turno.
5. Revisar si existe un evento en la posición alcanzada.
6. Aplicar el efecto del evento.
7. Mostrar el estado actual de la selección.

---

## Fase 4. Finalización

Cuando termine la simulación, determine la causa de finalización.

El programa debe mostrar uno de los siguientes mensajes:

```text
¡La selección llegó a la final del Mundial 2026!
```

o

```text
La selección fue eliminada antes de llegar a la final.
```

Finalmente debe mostrar:

```text
Victorias obtenidas: ...
Energía restante: ...
```

---

# Ejemplo de ejecución

```text
CAMINO A LA FINAL DEL MUNDIAL 2026

Turno 1
Resultado del dado: 4
Posición actual: 4
Energía: 9
Evento: Ninguno
Victorias: 0

Turno 2
Resultado del dado: 5
Posición actual: 9
Energía: 8
Evento: Centro médico
La selección recupera 3 puntos de energía.
Victorias: 0

Turno 3
Resultado del dado: 3
Posición actual: 12
Energía: 10
Evento: Partido difícil

Dado del partido: 5
¡La selección ganó el partido!
Victorias: 1
```

> **Nota:** La salida variará en cada ejecución debido al uso de números aleatorios.

---

# Requisitos

El programa debe incluir:

- Al menos una lista para representar el recorrido.
- Una colección con los eventos del juego.
- Generación de números aleatorios.
- Selección de posiciones sin repetición.
- Un ciclo `while`.
- Una condición compuesta en el ciclo (`and`).
- Estructuras `if`, `elif` y `else`.
- Contadores y/o acumuladores.
- Mensajes que permitan seguir la simulación.

---

# Entregable

Suba un único archivo comprimido (.zip) con el siguiente nombre:

```text
apellido_nombre_mundial2026.zip
```

El archivo comprimido debe contener únicamente los siguientes archivos:

```text
apellido_nombre_mundial2026.zip
│
├── mundial2026.py
└── captura.png
```

## Archivo `mundial2026.py`

Debe contener el programa completo y ejecutable.

El código debe conservar la siguiente estructura de fases para facilitar la revisión:

```python
###################################################
# Fundamentos de Programación
# Actividad: Camino a la Final del Mundial 2026
#
# Autor o Autores:
###################################################

import random as rd

###################################################
# FASE 1 - CONFIGURACIÓN INICIAL
###################################################

# Escriba aquí la configuración inicial del programa.



###################################################
# FASE 2 - SIMULACIÓN DEL RECORRIDO
###################################################

# Escriba aquí el ciclo principal del juego.



###################################################
# FASE 3 - RESULTADO FINAL
###################################################

# Muestre aquí el resultado de la simulación.
```

## Archivo `captura.png`

Debe contener una captura de pantalla donde se observe:

- El inicio de la ejecución.
- Varios turnos de la simulación.
- El mensaje final indicando cómo terminó el juego.

---

# Criterios de revisión

Se verificará que:

- El programa se ejecute correctamente.
- El código respete la estructura solicitada.
- Se implementen correctamente los eventos aleatorios.
- El ciclo principal utilice una condición compuesta.
- El juego pueda finalizar por cualquiera de las dos condiciones planteadas.
- La salida permita seguir claramente el desarrollo de la simulación.