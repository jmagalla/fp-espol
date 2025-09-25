# u8-t1: Pandas Estadísticas de Fútbol  

  Manipular datos desde archivos en formato CSV, seleccionar y filtrar de manera sencilla tablas de datos en función de posición, valor o etiquetas.

  ## Instrucciones
  1. Lea el archivo `futstats2017.csv` e imprima las 10 primeras filas del dataframe. Para leer el archivo use el argumento `sep="|"` en la función `read_csv()`. 
  2. Use la función `info()` para mostrar el esquema del dataframe e identifique los nombres de las columnas y sus tipos de datos.
  3. Use la funcion `head()` para mostrar las 10 primeras filas y use la función `tail()` para mostrar las 10 últimas filas del dataframe.
  4. Muestre las distintas ligas de fútbol y contabilice el número de filas para cada liga, en orden descendente. Use la función `value_counts()`. Asegúrese de usar solo la columna que corresponda.
  5. Muestre los distintos clubes y contabilice el número de jugadores por cada club, esto es similar al anterior, es decir contabilizar filas.
  6. Agregue una nueva columna de nombre Tot, la cual debe ser calculada usada la siguiente fórmula `Tot=(Vel*0.25)+(Sho*0.15)+(Pas*0.15)+(Dri*0.10)+(Def*0.25)+(Phy*0.10)`.
  7. Solicite al usuario el nombre de una liga de fútbol y muestre los mejores 15 jugadores de acuerdo a la columna `Tot`.
  8. Con el resultado anterior, seleccione las columnas `Jugador`, `Club`, y `Tot` y muestre el resultado ordenado por `Tot` de mayor a menor.
  9. Con el resultado ordenado, guarde a un archivo Excel de nombre `resultado1.xlsx`. Use la función `to_excel()`. Luego vuelva a guardar el resultado a un archivo de nombre `resultado12.xlsx` pero ahora incluya el argumento `index=0`.
  10. Solicite al usuario un de una liga de fútbol y muestre los mejores 10 jugadores del acuerdo a la columna `Def`.
  11. Solicite al usuario un año y de acuerdo a eso muestre las ligas de futbol distintas para ese año. Vea que los años que puede ingresar el usuario son 2014, 2015, 2016, y 2017. 
  12. Luego solicite al usuario una liga de Futbol y muestre los 15 mejores jugadores de esa liga de acuerdo al `Rank`.
  13. Muestre los mejores 10 jugadores de los 4 años, de acuerdo al `Rank` promedio de cada jugador por año, el reporte se debe mostrar así:

```
                2014          2015         2016        2017
      1         Xavi        Bruyne       Bruyne       Totti
      2       Inesta       Rakitić        Pirlo     Gerrard
      3    Rodriguez         Kroos         Özil      Alonso
      4     Fàbregas        Inesta       Inesta       Messi
      5  Eden Hazard      Fàbregas        Messi        Isco
```