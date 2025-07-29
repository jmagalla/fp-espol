
# 📦 Análisis de Pedidos por Estado

Una empresa de entregas a domicilio registra la información de sus pedidos en un diccionario. Cada **clave** del diccionario representa el **estado actual del pedido** (por ejemplo, `"pendiente"`, `"en camino"`, `"entregado"`), y su **valor asociado** es una **lista de cadenas**. Cada cadena contiene el **identificador del pedido** y el **monto en dólares**, separados por un guion (`-`).

A continuación se muestra un ejemplo del diccionario:

```python
dic_pedidos = {
    'pendiente': ['1001-15.50', '1006-22.00', '1026-19.56'],
    'en camino': ['1002-25.00', '1004-18.00'],
    'entregado': ['1003-30.00', '1005-45.25', '1007-32.10']
    ...
}
```

## 🧩 Tu tarea

Crea una función llamada `presentar_totales(dic_pedidos)` que reciba como argumento un diccionario con el formato antes descrito. La función debe **calcular y mostrar en pantalla** el **monto total acumulado** de los pedidos correspondientes a cada estado.

## 🖥️ Salida esperada

Para el diccionario anterior, la función debe mostrar en pantalla algo similar a lo siguiente:

```
Estado: pendiente
Monto total: 57.06

Estado: en camino
Monto total: 43.00

Estado: entregado
Monto total: 107.35
```

## 🧠 Pistas

- Recuerda que cada valor en el diccionario es una lista de cadenas.
- Usa el método `split('-')` para separar el identificador del monto.
- Acumula los montos usando una variable de tipo `float`.
