# Typing Doom

![portada.png](Typing%20Doom%20b5931fae171d484e9a90a5e1f0b5fb9e/portada.png)

### Sprite system

El sistema de sprites se hizo a través de la compresión de los sprites dentro de una misma imagen con el objetivo de ahorrar espacio y consumo de ram.

**Sprites del enemigo:**

![spritesheet.png](Typing%20Doom%20b5931fae171d484e9a90a5e1f0b5fb9e/spritesheet.png)

Los sprites se parsean y luego se guardan dentro de una lista ya separados y listos para ser llamados por su numero de indice. Para poder realizar el parseo se utiliza un archivo **.json** (*spritesheets.json*) que dentro tiene la información de la ubicación en el eje x e y donde se encuentra el sprite junto con su tamaño para así poder ser devueltos por la función **get_sprite.**

### Animación del enemigo

La animación del enemigo se realiza a través de una función de la clase **enemy** que nos devuelve el sprite que se requiere, y la coordenada x e y.

![enemigo-sprites.gif](Typing%20Doom%20b5931fae171d484e9a90a5e1f0b5fb9e/enemigo-sprites.gif)

Estas coordenadas se van a ir aumentando por una variable hasta que la coordenada Y llegue a 500