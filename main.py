import pygame
import sys
from worlds import worlds, get_world
from spritesheet import Spritesheet
from enemy import Enemy

# Iniciamos pygame
pygame.init()
# Constantes
window_size = (1280, 720)
FPS = 30
font_avaible = (168,1,9)
font_disable = (226,226,226)

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
my_font = pygame.font.Font("fonts/DooM.ttf", 25) # Fuente enemigo
my_font = pygame.font.Font("fonts/DooM.ttf", 30) # Fuente hud

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
palabra_random = "VV"
text_enemy = my_font.render(palabra_random,0, font_disable)
text_hud = my_font.render(palabra_random,0, font_disable)

enemigo_sprite = Spritesheet('assets/sprites/spritesheet.png')

############### E★N★E★M★I★G★O #############
enemigo = [enemigo_sprite.parse_sprite('iz.png'),enemigo_sprite.parse_sprite('centro.png'),enemigo_sprite.parse_sprite('dr.png'), enemigo_sprite.parse_sprite('hurt-0.png'),enemigo_sprite.parse_sprite('hurt-1.png'),enemigo_sprite.parse_sprite('hurt-2.png'),enemigo_sprite.parse_sprite('hurt-3.png'),enemigo_sprite.parse_sprite('hurt-4.png'),enemigo_sprite.parse_sprite('hurt-5.png')]
#############################################

enemigo_animation = Enemy("gonzalo", 1)

enemigo_vel_x = 1.7
enemigo_vel_y = 2
nuevo_enemigo = enemigo_animation.animation(1)
pos_enemigo_x = nuevo_enemigo[1]
pos_enemigo_y = nuevo_enemigo[2]
pos_letras_y = nuevo_enemigo[3]

letras = []
##### Convertir palabra en lista #####
def palabra_a_lista(palabra):
  lista = []
  for letra in palabra:
    lista.append(letra.upper())
  return lista

lista_palabra = palabra_a_lista(palabra_random)
print(lista_palabra)

while True:
  # El loop que detecta todos los eventos

  for event in pygame.event.get():
    # print(event)
    if event.type == pygame.QUIT:
      sys.exit()

    if len(lista_palabra) > 0:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a and lista_palabra[0] == "A":
          lista_palabra.pop(0)
        if event.key == pygame.K_b and lista_palabra[0] == "B":
          lista_palabra.pop(0)
        if event.key == pygame.K_c and lista_palabra[0] == "C":
          lista_palabra.pop(0)
        if event.key == pygame.K_d and lista_palabra[0] == "D":
          lista_palabra.pop(0)
        if event.key == pygame.K_e and lista_palabra[0] == "E":
          lista_palabra.pop(0)
        if event.key == pygame.K_f and lista_palabra[0] == "F":
          lista_palabra.pop(0)
        if event.key == pygame.K_g and lista_palabra[0] == "G":
          lista_palabra.pop(0)
        if event.key == pygame.K_h and lista_palabra[0] == "H":
          lista_palabra.pop(0)
        if event.key == pygame.K_i and lista_palabra[0] == "I":
          lista_palabra.pop(0)
        if event.key == pygame.K_j and lista_palabra[0] == "J":
          lista_palabra.pop(0)
        if event.key == pygame.K_k and lista_palabra[0] == "K":
          lista_palabra.pop(0)
        if event.key == pygame.K_l and lista_palabra[0] == "L":
          lista_palabra.pop(0)
        if event.key == pygame.K_m and lista_palabra[0] == "M":
          lista_palabra.pop(0)
        if event.key == pygame.K_n and lista_palabra[0] == "N":
          lista_palabra.pop(0)
        if event.key == pygame.K_o and lista_palabra[0] == "O":
          lista_palabra.pop(0)
        if event.key == pygame.K_p and lista_palabra[0] == "P":
          lista_palabra.pop(0)
        if event.key == pygame.K_q and lista_palabra[0] == "Q":
          lista_palabra.pop(0)
        if event.key == pygame.K_r and lista_palabra[0] == "R":
          lista_palabra.pop(0)
        if event.key == pygame.K_s and lista_palabra[0] == "S":
          lista_palabra.pop(0)
        if event.key == pygame.K_u and lista_palabra[0] == "U":
          lista_palabra.pop(0)
        if event.key == pygame.K_t and lista_palabra[0] == "T":
          lista_palabra.pop(0)
        if event.key == pygame.K_v and lista_palabra[0] == "V":
          lista_palabra.pop(0)
        if event.key == pygame.K_w and lista_palabra[0] == "W":
          lista_palabra.pop(0)
        if event.key == pygame.K_x and lista_palabra[0] == "X":
          lista_palabra.pop(0)
        if event.key == pygame.K_y and lista_palabra[0] == "Y":
          lista_palabra.pop(0)
        if event.key == pygame.K_z and lista_palabra[0] == "Z":
          lista_palabra.pop(0)

    ##### CUANDO SE VENCE AL ENEMIGO #####
    # if len(lista_palabra) == 0:
    #   print("El mounstro fue destruido")
    #   print("Nuevo mounstro creado")
    ######################################
        


    pos_cursor = pygame.mouse.get_pos()
    pos_cursor_x = pos_cursor[0]
    pos_cursor_y = pos_cursor[1]
  


  ###########################################
  if pos_enemigo_x > 180:
    pos_enemigo_x -= enemigo_vel_x
  if pos_enemigo_y < 350 and pos_enemigo_x < 250:
    pos_enemigo_y += enemigo_vel_y
  # print("Posicion enemigo x: {0} \nPosicion enemigo y: {1}".format(pos_enemigo_x,pos_enemigo_y))
  pos_letras_y = pos_enemigo_y - 50
  ###########################################

  # cargamos el escenario
  screen.blit(stage, [0,0])
  # screen.blit(enemigo[3],[400,230])
  screen.blit(enemigo[nuevo_enemigo[0]], [pos_enemigo_x,pos_enemigo_y])
  # screen.blit(enemigo[nuevo_enemigo[0]], [280,240])
  screen.blit(text_enemy,[pos_enemigo_x,pos_letras_y])
  screen.blit(domo,[398,0])
  screen.blit(door, [532, 0]) # Puerta abierta y =-250, puerta cerrada y=0
  screen.blit(hud,[0,597])
  screen.blit(text_hud,[550,650])
  screen.blit(cursor,[pos_cursor_x,pos_cursor_y])

  # Este comando es para que se actualice la pantalla en cada bucle, por eso se pone al final
  pygame.display.flip()
  # limitamos la cantidad de fotogramas por segundo 
  clock.tick(FPS)

