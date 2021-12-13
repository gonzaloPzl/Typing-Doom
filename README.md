# Typing Doom

La idea del video juego es hacer algo parecido a **tipping of the dead**

[https://www.youtube.com/watch?v=Zs3M6oDcPlU](https://www.youtube.com/watch?v=Zs3M6oDcPlU)

La cámara va a ser fija y van a ir apareciendo enemigos con un cartel con la palabra que van a tener que ir deletreando, una vez que esten adelante del todo te van a ir haciendo daño si no podes completar la palabra palabra. A medida que vas completando la palabra se ejecutan disparos pero para terminar de matar al enemigo la palabra tiene que estar escrita al 100.

- Es importante que todo sea escrito con upper(), de esta forma no se van a distinguir mayúsculas de minúsculas

### Assets

**Musica del juego:**

- Tipo 8 bits: [https://opengameart.org/content/nes-shooter-music-5-tracks-3-jingles](https://opengameart.org/content/nes-shooter-music-5-tracks-3-jingles)

**Efectos especiales:**

- Disparo: [https://opengameart.org/content/light-machine-gun](https://opengameart.org/content/light-machine-gun)
- [https://www.youtube.com/watch?v=7MA5h4gAPmM](https://www.youtube.com/watch?v=7MA5h4gAPmM)

### Como hacer el juego?

Primero se van a guardar 3 listas con palabras:

- Una lista con palabras cortas
- Una lista con palabras largas
- Una lista con oraciones compuestas por 2 palabras

Una vez que se arranque el juego van a ir saliendo los enemigos y para derrotarlos tendremos que escribir la palabra que tengan escritas cada enemigo.

**Como se determina la palabra del enemigo?**

La palabra se va a determinar con una función que maneje probabilidades, la lista con palabras cortas tendrá una mayor probabilidad, luego la lista con oraciones una menor y por ultimo la lista con palabras difíciles. Una vez se determine que lista se va a utilizar se hace otro random para devolver alguna palabra de toda la lista.

**Derrotar al enemigo**

Nosotros escribiremos la palabra para poder derrotar al enemigo. Si el enemigo se nos acerca hasta la pantalla nos hará daño cada 3 segundos, la vida sera una variable que tenga el valor de 100 y los ataques nos quitaran 20.

**Contador de asesinatos**

Tendremos un contador de la cantidad de enemigos que iremos derrotando

**Dificultad progresiva**

La dificultad progresiva la vamos a hacer con la cantidad de enemigos eliminados, mientras mas enemigos eliminemos mayores van a ser las probabilidades de que toquen palabras compuestas y difíciles.

# README.md

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