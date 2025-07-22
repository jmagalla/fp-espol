
# 🏆 Ejercicio: Tabla de puntos de fútbol

## 🎯 Objetivo del ejercicio
Aplicar estructuras de control, listas, cadenas y diccionarios para procesar información de partidos de fútbol y calcular la puntuación acumulada de cada país.

## 📋 Descripción del problema
Se te pide escribir un programa en Python que simule el cálculo de la tabla de puntos de un torneo de fútbol. Para ello, dispondrás de dos listas:

1. Una lista con los partidos jugados, donde cada elemento es una cadena con el nombre de los países separados por un guion (`-`).  
   Ejemplo: `"ECU-SEN"` indica un partido entre Ecuador y Senegal.

2. Una lista con los resultados de esos partidos, donde cada elemento es una cadena con los goles marcados por cada país, también separados por un guion (`-`).  
   Ejemplo: `"2-0"` indica que el primer país en la lista ganó 2 a 0.

## 🧮 Reglas para asignar puntos
- Si un país gana el partido, recibe **3 puntos**.
- Si hay empate, **ambos países reciben 1 punto**.
- El país que pierde, **no recibe puntos**.

## 🧠 Tu programa debe:
1. Definir una función llamada `calcular(paises, goles)` que reciba las dos listas.
2. Procesar los datos y devolver un diccionario donde las claves sean los nombres de los países y los valores la cantidad total de puntos obtenidos.
3. Mostrar el resultado final en el programa principal.

## 🧪 Ejemplo de entrada:
```python
listeje01 = ['CAT-ECU', 'ARG-MEX', 'BRA-SUI', 'ECU-SEN']
listeje02 = ['0-2', '1-1', '4-1', '2-0']
```

## ✅ Ejemplo de salida:
```python
{'CAT': 0, 'ECU': 6, 'ARG': 1, 'MEX': 1, 'BRA': 3, 'SUI': 0, 'SEN': 0}
```

---
