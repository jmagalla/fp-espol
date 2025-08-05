
# 🧠 Taller: Vectores NumPy y Funciones

## 🎯 Objetivo
Utilizar **vectores NumPy** para resolver un problema aplicado al análisis del estado físico de personas, a través del cálculo del IMC.

---

## 📘 Descripción

El programa debe calcular el **Índice de Masa Corporal (IMC)** para un conjunto de personas, y determinar cuántas se encuentran en las siguientes categorías:

- Bajo peso
- Peso saludable
- Sobrepeso
- Obesidad

---

## 📂 Archivos

Utiliza los siguientes archivos de texto:

- [`pesos.txt`](pesos.txt): contiene 1700 valores con los **pesos en libras** de personas.
- [`alturas.txt`](alturas.txt): contiene 1700 valores con las **alturas en pulgadas** de personas.

---

## 🧮 Actividades a realizar

1. **Carga de datos**

   - Carga los archivos `pesos.txt` y `alturas.txt` usando `np.loadtxt` y almacena los datos en vectores NumPy:
     - `pesos_libras`: vector con los pesos.
     - `alturas_pulgadas`: vector con las alturas.

2. **Conversión de unidades y cálculo de IMC**

   - Define una función `calcular_BMI_vectorizado(pesos_libras, alturas_pulgadas)` que:
     - Convierta las alturas de pulgadas a **metros** (1 pulgada = 0.0254 m).
     - Convierta los pesos de libras a **kilogramos** (1 libra = 0.453592 kg).
     - Calcule el IMC usando la fórmula:

       ```python
       BMI = peso_kg / (altura_m ** 2)
       ```

     - Retorne un vector con los valores de IMC.

3. **Clasificación por categorías**

   - A partir del vector de IMC, usa indexación booleana para contar cuántas personas están en cada una de las siguientes categorías:
     - Bajo peso: IMC < 18.5
     - Normal: 18.5 ≤ IMC < 25
     - Sobrepeso: 25 ≤ IMC < 30
     - Obesidad: IMC ≥ 30

4. **Visualización con asteriscos**

   - Muestra el resultado como un histograma textual, usando un asterisco por cada 100 personas. Usa redondeo tradicional:
     - Por ejemplo: 340 personas = 3 asteriscos, 351 personas = 4 asteriscos.

   - **Ejemplo de salida esperada:**
     ```
     bajo          ***
     normal        ******
     sobrepeso     ****
     obesidad      *****
     ```

---

## 🧪 Archivos de entrada

Descárgalos aquí:

- [pesos.txt](pesos.txt)
- [alturas.txt](alturas.txt)
