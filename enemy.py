import pygame

class Enemy():
  def __init__(self, word, pos):
      self.pos = pos
      self.word = word

  def animation(self, pos):
    if pos == 1:
      sprite = 0
      position_x = 400
      position_y = 230
      letters_position = position_y - 50
      return sprite, position_x, position_y, letters_position
    elif pos == 2:
      pass
    elif pos == 3:
      pass



