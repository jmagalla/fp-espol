
# Procesamiento de Pedidos desde Archivos

Una empresa de entregas desea automatizar el procesamiento de pedidos. Los datos están almacenados en un archivo de texto, donde cada línea representa un pedido con el siguiente formato:

```
estado;id-monto
```

Por ejemplo:

```
pendiente;1001-15.50
pendiente;1006-22.00
en camino;1002-25.00
entregado;1003-30.00
entregado;1005-45.25
```

## Tu tarea

Debes crear un programa que lea los datos desde un archivo, los organice en un diccionario por estado, calcule el monto total de pedidos por estado y guarde un resumen en un nuevo archivo de texto.

### Requisitos del programa

Implementa las siguientes funciones:

1. `def cargar_datos(nombre_archivo):`  
   - Recibe el nombre del archivo de entrada.
   - Lee el contenido y construye un diccionario donde la clave es el estado y el valor es una lista de cadenas con el formato `id-monto`.

2. `def presentar_totales(dic_pedidos):`  
   - Recibe el diccionario generado.
   - Retorna un **nuevo diccionario**, donde cada clave es un estado de pedido y su valor asociado es el **monto total** acumulado (tipo `float`).
   - Ejemplo del diccionario retornado:
     ```python
     {
         "pendiente": 57.06,
         "en camino": 25.00,
         "entregado": 75.25
     }
     ```

3. `def escribir_resumen(nombre_archivo, dic_resumen):`  
   - Recibe el nombre del archivo de salida y un diccionario con el resumen de montos por estado.
   - Escribe el contenido en el archivo, una línea por estado con el siguiente formato:
     ```
     Estado: <estado> - Monto total: <monto>
     ```

4. Programa principal:  
   - Solicita al usuario el nombre del archivo de entrada.
   - Llama a `cargar_datos`.
   - Usa `presentar_totales` para obtener el resumen de montos.
   - Solicita el nombre del archivo de salida.
   - Usa `escribir_resumen` para guardar el resultado.

## Ejemplo de salida esperada en el archivo generado

```
Estado: pendiente - Monto total: 57.06
Estado: en camino - Monto total: 25.00
Estado: entregado - Monto total: 75.25
```
