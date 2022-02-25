import pygame
from settings import *

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups):
    super().__init__(groups)
    self.image = pygame.Surface((64, 64))
    self.image.fill('red')
    self.rect = self.image.get_rect(center = pos)
    self.direction = pygame.math.Vector2()

    # Fall
    self.gravity = 0.1
  
  def fall(self):
    self.direction.y += self.gravity

  def movement(self):
    self.rect.center += self.direction
  
  def move_shoot(self, distance):
    self.direction.x = distance.x * -5
    self.direction.y = distance.y * -7
  
  def detect_screen(self):
    if self.rect.midleft[0] >= screen_width:
      self.rect.midright = (0, self.rect.centery)
    elif self.rect.midright[0] < 0 - self.image.get_width():
      self.rect.midleft = (screen_width, self.rect.centery)
  
  def update(self):
    self.fall()
    self.movement()
    self.detect_screen()