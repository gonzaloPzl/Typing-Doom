# Typing Doom

# README.md

![portada.png](Typing%20Doom%20b5931fae171d484e9a90a5e1f0b5fb9e/portada.png)

### Video demo

![video.png](Typing%20Doom%20b5931fae171d484e9a90a5e1f0b5fb9e/video.png)

### Sprite system

El sistema de sprites se hizo a través de la compresión de los sprites dentro de una misma imagen con el objetivo de ahorrar espacio y consumo de ram.

**Sprites del enemigo:**

![spritesheet.png](Typing%20Doom%20b5931fae171d484e9a90a5e1f0b5fb9e/spritesheet.png)

Los sprites se parsean y luego se guardan dentro de una lista ya separados y listos para ser llamados por su numero de indice. Para poder realizar el parseo se utiliza un archivo **.json** (*spritesheets.json*) que dentro tiene la información de la ubicación en el eje x e y donde se encuentra el sprite junto con su tamaño para así poder ser devueltos por la función **get_sprite.**

### Animación del enemigo

La animación del enemigo se realiza a través de una función de la clase **enemy** que nos devuelve el sprite que se requiere, y la coordenada x e y.

![enemigo-sprites.gif](Typing%20Doom%20b5931fae171d484e9a90a5e1f0b5fb9e/enemigo-sprites.gif)

Estas coordenadas se van a ir aumentando por una variable hasta que la coordenada Y llegue a 500

### Mecánica principal del juego

El juego consiste en un shooter mecanográfico basado en Doom, es decir eliminamos enemigos mediante la escritura. Para poder lograr esta mecánica lo que se hace es servirse de un diccionario de palabras que se encuentran en el archivo **words.py,** el mismo archivo también contiene un función que nos retorna una palabra al azar de la lista.

```python
def get_world():
  random = randint(0,len(worlds) - 1)
  world = worlds[random]
  return world
```

Una vez se tiene la palabra esta se nos instancia en el hud del juego y también encima del enemigo. 

Tenemos que dividir la palabra en diferentes tecladas que se vayan presionando, entonces utilizamos la función **palabra_a_lista**

```python
def palabra_a_lista(palabra):
  lista = []
  for letra in palabra:
    lista.append(letra.upper())
  return lista
```

Lo que hace es ingresar cada letra que conforma la palabra dentro de una lista, de esta forma podemos saber cual es la letra que se tiene que ingresar primero ya que esta siempre estará en la posición 0

Ahora detectamos los eventos de presión de teclado, para eso nos servimos del for de eventos estandar en pygame

```python
for event in pygame.event.get():
	if len(lista_palabra) > 0:
		if event.key == pygame.K_a and lista_palabra[0] == "A":
          lista_palabra.pop(0)
          sound_tecla.play()
```

Como podemos ver una vez que la letra es igual al primer index de nuestra palabra  se elimina esta primera letra con el método pop(0) y se ejecuta el sonido de la tecla correcta, de esta forma la siguiente letra será la que ahora se encontrará en la posición 0.

Una vez que se vacía esta lista el juego lo detecta y da por eliminado al enemigo, respawneado otro con la ejecución de una función para la creación de otra palabra.

**dificultad**

Para generar una dificultad progresiva cada 5 enemigos derrotados se aumenta la velocidad de los mismos en 0.5 sobre la base.

```python
if len(palabras_acertadas) > 5:
    enemigo_vel_x = 2.5 # normal 2
    enemigo_vel_y = 2.5 # normal 2
  if len(palabras_acertadas) > 10:
    enemigo_vel_x = 3
    enemigo_vel_x = 3
  if len(palabras_acertadas) > 15:
    enemigo_vel_x = 3.5
    enemigo_vel_x = 3.5
```

### Sonidos

Los sonidos se encuentran en la carpeta **assets/sounds**, estan dividios en el soundtrack de fondo, los sonidos del enemigo y del personaje.

**sonido de fondo**

[Doom OST - E1M1 - At Doom's Gate](https://www.youtube.com/watch?v=BSsfjHCFosw)

El sonido de fondo que se utiliza es una canción de metal del DOOM 1, esta se pone en bucle invocando solamente estas 2 líneas de código

 

```python
pygame.mixer.music.load("assets/sounds/soundtrack.wav")
pygame.mixer.music.play(-1)
```

Lo que hace es invocar al objeto mixer, luego music y luego load para cargar el sonido, después reproduce lo que se encuentra cargado en el mixer, pasándole el parámetro -1 hacemos que se ponga en bucle

**sonido enemigos**

Hay 5 tipos diferentes de sonidos al eliminar un enemigo, esto con en fin de no generar cansancio auditivo, estos se presentan de forma aleatoria y para su implementación se detecta cuando la lista generada a partir de la palabra se encuentra vacía, de esa forma se sabe que el enemigo se derrotó, entonces es que se reproduce uno de los sonidos obtenidos con la función **get_random_sound**

```python
caco = get_random_sound(caco_sounds)
caco.play()
```

La función **get_random_sound** recibe una lista en este caso una lista de sonidos precargados y nos devuelve uno al azar, como tomo en el randint los valores del tamaño de la lista nos sirve también para el personaje principal.

**sonido de personaje**

Para el sonido del personaje también se utilizaron múltiples audios que se reproducen dependiendo el score.

Para determinar si se tiene que reproducir un audio se evalua si el score ( len(palabras_acertadas) ) es divisible por 5 o por 3 dejando de resto 0. De esta forma cada vez que el score de un resultado así se va a reproducir un audio de forma aleatoria utilizando la misma función que con el enemigo **get_random_sound**

```python
if len(palabras_acertadas) > 0:
      if len(palabras_acertadas) % 5 == 0 or len(palabras_acertadas) % 3 == 0:
        doomguy_sound = get_random_sound(doomguy_sounds)
        doomguy_sound.play()
        palabras_acertadas.append(" ")
```

A lo ultimo se agrega un espacio vacío a la lista de palabras acertadas ya que sino el bucle while de juego se seguiría ejecutando y la condición se cumpliría hasta que se acerté otra palabra por lo que se estarían reproduciendo sonidos cada vez que se detecte un evento de teclado. Para evitar eso se añade y luego se retira el espacio en blanco dentro de la lista.