import pygame
import sys
from worlds import worlds, get_world
from spritesheet import Spritesheet
from enemy import Enemy
from random import randint

# Iniciamos pygame
pygame.init()
# Constantes
window_size = (1280, 720)
FPS = 60
font_avaible = (168,1,9)
font_disable = (226,226,226)
GAME_OVER= False

#### Puntaje ####
palabras_acertadas = []

# Creando la ventana
screen = pygame.display.set_mode(window_size)
# Controlamos los fps
clock = pygame.time.Clock()
# El nombre de la ventana
pygame.display.set_caption("Doom: Typing")
# Icono del juego
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)
# Incluimos la fuente
font_enemy = pygame.font.Font("fonts/DooM.ttf", 20) # Fuente enemigo
font_hud = pygame.font.Font("fonts/DooM.ttf", 35) # Fuente hud
font_score = pygame.font.Font("fonts/DooM.ttf", 45) # Fuente score
font_game_over = pygame.font.Font("fonts/DooM.ttf", 100) # Fuente game over
font_score_game_over = pygame.font.Font("fonts/DooM.ttf", 50) # Fuente game over

# Cargamos imagenes
hud = pygame.image.load("assets/hud.png").convert()
stage = pygame.image.load("assets/stage.png").convert()
door = pygame.image.load("assets/stage--door.png").convert()
domo = pygame.image.load("assets/stage--domo.png")
cursor = pygame.image.load("assets/cursor.png")

# Para cambiar la visibilidad del mouse
pygame.mouse.set_visible(0)

#Texto en pantalla
# palabra_random = get_world(worlds)
palabra_random = get_world()
text_enemy = font_enemy.render(palabra_random,0, font_disable)
text_hud = font_hud.render(palabra_random,0, font_disable)
text_score = font_score.render(str(len(palabras_acertadas)),0, (207,2,6))
text_game_over = font_game_over.render("GAME OVER",0, (207,2,6))
text_score_game_over = font_score_game_over.render("Tu score fue :",0, font_disable)
text_continue = font_hud.render("Presione ESPACIO para continuar",0,font_disable)

enemigo_sprite = Spritesheet('assets/sprites/spritesheet.png')

############### E★N★E★M★I★G★O #############
enemigo = [enemigo_sprite.parse_sprite('iz.png'),enemigo_sprite.parse_sprite('centro.png'),enemigo_sprite.parse_sprite('dr.png'), enemigo_sprite.parse_sprite('hurt-0.png'),enemigo_sprite.parse_sprite('hurt-1.png'),enemigo_sprite.parse_sprite('hurt-2.png'),enemigo_sprite.parse_sprite('hurt-3.png'),enemigo_sprite.parse_sprite('hurt-4.png'),enemigo_sprite.parse_sprite('hurt-5.png')]
#############################################

enemigo_animation = Enemy("gonzalo", 1)

enemigo_vel_x = 2.5 # normal 2
enemigo_vel_y = 2.5 # normal 2
nuevo_enemigo = enemigo_animation.animation(1)
pos_enemigo_x = nuevo_enemigo[1]
pos_enemigo_y = nuevo_enemigo[2]
pos_letras_y = nuevo_enemigo[3]

##### Sonido teclas #####
sound_tecla = pygame.mixer.Sound("assets/sounds/tecla.wav")
#### Sonidos enemigo ####
caco_1 = pygame.mixer.Sound("assets/sounds/caco_1.wav")
caco_2 = pygame.mixer.Sound("assets/sounds/caco_2.wav")
caco_3 = pygame.mixer.Sound("assets/sounds/caco_3.wav")
caco_4 = pygame.mixer.Sound("assets/sounds/caco_4.wav")
caco_5 = pygame.mixer.Sound("assets/sounds/caco_5.wav")
caco_sounds = [caco_1,caco_2,caco_3,caco_4,caco_5]
##### Sonidos personaje #####
doomguy_1 = pygame.mixer.Sound("assets/sounds/doomguy_1.wav")
doomguy_2 = pygame.mixer.Sound("assets/sounds/doomguy_2.wav")
doomguy_3 = pygame.mixer.Sound("assets/sounds/doomguy_3.wav")
doomguy_4 = pygame.mixer.Sound("assets/sounds/doomguy_4.wav")
doomguy_5 = pygame.mixer.Sound("assets/sounds/doomguy_5.wav")
doomguy_continue = pygame.mixer.Sound("assets/sounds/doomguy_continue.wav")
doomguy_sounds = [doomguy_1,doomguy_2,doomguy_3,doomguy_4,doomguy_5,doomguy_continue]
#### soundtrack ####
pygame.mixer.music.load("assets/sounds/soundtrack.wav")
pygame.mixer.music.play(-1)
##### funcion sonidos random #####
def get_random_sound(sounds):
  random_sound = sounds[randint(0,len(sounds) - 1)]
  return random_sound
# letras = []
##### Convertir palabra en lista #####
def palabra_a_lista(palabra):
  lista = []
  for letra in palabra:
    lista.append(letra.upper())
  return lista

lista_palabra = palabra_a_lista(palabra_random)

## Grupo de Sprites  ##
enemigos = pygame.sprite.Group()

### Sprites ###

while True:
  # El loop que detecta todos los eventos
  # soundtrack.play()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    if len(lista_palabra) > 0:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a and lista_palabra[0] == "A":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_b and lista_palabra[0] == "B":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_c and lista_palabra[0] == "C":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_d and lista_palabra[0] == "D":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_e and lista_palabra[0] == "E":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_f and lista_palabra[0] == "F":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_g and lista_palabra[0] == "G":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_h and lista_palabra[0] == "H":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_i and lista_palabra[0] == "I":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_j and lista_palabra[0] == "J":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_k and lista_palabra[0] == "K":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_l and lista_palabra[0] == "L":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_m and lista_palabra[0] == "M":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_n and lista_palabra[0] == "N":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_o and lista_palabra[0] == "O":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_p and lista_palabra[0] == "P":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_q and lista_palabra[0] == "Q":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_r and lista_palabra[0] == "R":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_s and lista_palabra[0] == "S":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_u and lista_palabra[0] == "U":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_t and lista_palabra[0] == "T":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_v and lista_palabra[0] == "V":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_w and lista_palabra[0] == "W":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_x and lista_palabra[0] == "X":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_y and lista_palabra[0] == "Y":
          lista_palabra.pop(0)
          sound_tecla.play()
        if event.key == pygame.K_z and lista_palabra[0] == "Z":
          lista_palabra.pop(0)
          sound_tecla.play()
    if GAME_OVER == True:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          doomguy_continue.play()
          pos_enemigo_x = 400
          pos_enemigo_y = 230

    ##### Sonidos aleatorios del personaje #####
    if len(palabras_acertadas) > 0:
      if len(palabras_acertadas) % 5 == 0 or len(palabras_acertadas) % 3 == 0:
        doomguy_sound = get_random_sound(doomguy_sounds)
        doomguy_sound.play()
        palabras_acertadas.append(" ")
        if len(palabras_acertadas) % 5 == 0 or len(palabras_acertadas) % 3 == 0:
          palabras_acertadas.append(" ")


    ##### CUANDO SE VENCE AL ENEMIGO #####
    if len(lista_palabra) == 0:
      if " " in palabras_acertadas:
        palabras_acertadas.remove(" ")
      if " " in palabras_acertadas:
        palabras_acertadas.remove(" ")
      caco = get_random_sound(caco_sounds)
      caco.play()
      palabras_acertadas.append(palabra_random)
      palabra_random = get_world()
      lista_palabra = palabra_a_lista(palabra_random)
      pos_enemigo_x = 400
      pos_enemigo_y = 230

    text_enemy = font_enemy.render(palabra_random,0, font_disable)
    text_hud = font_hud.render(palabra_random,0, font_disable)
    text_score = font_score.render(str(len(palabras_acertadas)),0,(207,2,6))
    ######################################

    pos_cursor = pygame.mouse.get_pos()
    pos_cursor_x = pos_cursor[0]
    pos_cursor_y = pos_cursor[1]

  ###########################################
  if pos_enemigo_x > 180 :
    pos_enemigo_x -= enemigo_vel_x
  if pos_enemigo_y < 500 and pos_enemigo_x < 250:
    pos_enemigo_y += enemigo_vel_y
  
  pos_letras_y = pos_enemigo_y - 50
  ###########################################

  ##### DIFICULTAD #####
  if len(palabras_acertadas) > 5:
    enemigo_vel_x = 3 # normal 2
    enemigo_vel_y = 3 # normal 2
  if len(palabras_acertadas) > 10:
    enemigo_vel_x = 3.5
    enemigo_vel_x = 3.5
  if len(palabras_acertadas) > 15:
    enemigo_vel_x = 4
    enemigo_vel_x = 4

  # cargamos el escenario
  screen.blit(stage, [0,0])
  screen.blit(door, [532, 0]) # Puerta abierta y =-250, puerta cerrada y=0
  if pos_enemigo_y == 500:
    enemigo_vel_x = 2.5 # normal 2
    enemigo_vel_y = 2.5
    GAME_OVER = True
    screen.blit(text_game_over,[130, 200])
    screen.blit(text_score_game_over,[250, 395])
    screen.blit(text_score,[740, 400])
    screen.blit(text_continue,[200, 600])
    palabras_acertadas.clear()
  else:
    # screen.blit(enemigo[3],[400,230])
    if len(lista_palabra) > 0:
      screen.blit(enemigo[nuevo_enemigo[0]], [pos_enemigo_x,pos_enemigo_y])
    # screen.blit(enemigo[nuevo_enemigo[0]], [280,240])
    if len(lista_palabra) > 0:
      screen.blit(text_enemy,[pos_enemigo_x,pos_letras_y])
    screen.blit(domo,[398,0])
    
    screen.blit(hud,[0,597])
    screen.blit(text_hud,[550,650])
    screen.blit(text_score,[960,618])
    screen.blit(cursor,[pos_cursor_x,pos_cursor_y])

  # Este comando es para que se actualice la pantalla en cada bucle, por eso se pone al final
  pygame.display.flip()
  # limitamos la cantidad de fotogramas por segundo 
  clock.tick(FPS)

