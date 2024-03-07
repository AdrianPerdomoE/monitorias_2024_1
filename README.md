#List comprehensions
> **List comprehensions** nos ayuda a simplificar la creación de nuestras listas en python, donde en vez de tener varias líneas de codigo definiendo el contenido que tendra la lista, podremos establecer de forma rapida, legible y en una sola linea, como estara construida nuestra lista.
---
> Hay varias formas de utilizar **List comprehensions**, las siguientes son las más comunes:
<ul>
  <li>
      <h2><b>Declaración basica:<b/><h2/>
      <code>[numero**2 for numero in range(5)]</code>
  </li>
    <li>
      <h2><b>Declaración anidada:<b/><h2/>
      <code>[[columna for columna in range(8)] for fila in range(8)]</code>
  </li>
  <li>
      <h2><b>Declaración ciclos anidados:<b/><h2/>
      <code>[(x,y) for x in range(5) for y in range(6,11)]</code>
  </li>
  <li>
      <h2><b>Declaración con condicionales:<b/><h2/>
      <code>[numero if i!2==0 else 0 for numero in range(1,300)]</code>
  </li>
</ul>


#**Ejercicios**
>Los siguientes 8 ejercicios están ordenados por dificultad
1. **Multiplos de 3 o 5**: Genera una lista de los múltiplos de 3 o 5 en el rango del 1 al 50 usando comprensión de listas.
2. **Palabras más largas**: Dada la lista de palabras: `["Carmona","Carrusel","carro","Caro","Piel","Cafe","Miguel","Barro","Piso"]`, crea una nueva lista que contenga las palabras con más de 5 letras utilizando comprensión de listas.
3. **Números primos**: Crea una lista de los números primos hasta 1001 usando comprensión de listas.
4. **División** Crea una lista que contenga la división de los numeros del 15 al 30 entre los numeros del 2 al 5 ejm: 15/2 15/3 15/4 15/5 16/2 16/3 16/4 16/5
5. **Matriz de identidad**: Genera una matriz de identidad de 5x5 utilizando comprensión de listas.
6. **Producto cartesiano**: Dadas dos listas A= `[3,5,6,7,8]` y B=`[23,35,21,45,1]`, crea una lista de tuplas que representen todas las combinaciones posibles entre elementos de A y B utilizando comprensión de listas.
7. **Generar números de Fibonacci**: Crea una lista que contenga los primeros 15 números de la secuencia de Fibonacci
8. **Generar tabla de multiplicación pares**: Generar la tabla de multiplicación de 12 x 12, si la suma de sus digitos es par, se pone el numero, de lo contrario un 0