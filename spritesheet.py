import pygame
from pygame import sprite
import json

class Spritesheet:
  def __init__(self, filename):
      self.filename = filename
      self.sprite_sheet = pygame.image.load(filename).convert()
      # Convert optimiza la imagen pero le añade fondo negro
      self.meta_data = self.filename.replace('png','json')
      # reemplazamos la extension que nos viene en el nombre del archivo por json para acceder al json
      with open(self.meta_data) as f:
        self.data = json.load(f)
      #abrimos el archivo json, as f nos sirve para hacer un shortchut del archivo
      f.close()
  
  def get_sprite(self, x, y, w, h):
    # Recibimos la cordenada x e y donde se encuentra la letra y su tamaño
    sprite = pygame.Surface((w, h))
    # Indicamos lo que va a ocupar nuestra letra
    sprite.set_colorkey((0,0,0))
    #set_color nos permite retirar el fondo solido que puso el convert indicando el color en rgb
    sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
    return sprite
  
  def parse_sprite(self, name):
    sprite = self.data['frames'][name]['frame']
    # entramos en la composición de nuestro json, tenemos un objeto dentro de otro
    # Entonces entramos al objeto frames, despues el nombre que nos viene por variable y despues el objeto frame
    x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
    # Del objeto frame obtenemos la posición y el tamaño
    image = self.get_sprite(x,y,w,h)
    # Una vez obtenidos los datos vamos a retornar el sprite con la función creada anteriormente
    return image