import pygame
from settings import *

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups, collision_sprites, type_sprite):
    super().__init__(groups)
    self.image = pygame.Surface((64, 64))
    self.image.fill('red')
    self.rect = self.image.get_rect(center = pos)
    self.direction = pygame.math.Vector2()
    self.collision_sprites = collision_sprites
    self.type = type_sprite

    # Status
    self.hp = 1

    # Movement
    self.speed_x = 5
    self.speed_y = 7
    self.gravity = 0.1
  
  def fall(self):
    self.direction.y += self.gravity

  def movement(self):
    self.rect.center += self.direction
  
  def move_shoot(self, distance):
    self.direction.x = distance.x * -self.speed_x
    self.direction.y = distance.y * -self.speed_y
  
  def detect_screen(self):
    if self.rect.midleft[0] >= screen_width:
      self.rect.midright = (0, self.rect.centery)
    elif self.rect.midright[0] < 0 - self.image.get_width():
      self.rect.midleft = (screen_width, self.rect.centery)
    
    if self.rect.midtop[1] <= 0:
      self.rect.midtop = (self.rect.centerx, 0)
      self.direction.y *= -1
  
  def collision_detect(self):
    for sprite in self.collision_sprites.sprites():
      if self.rect.colliderect(sprite):
        self.hp -= 1
  
  def update(self):
    self.fall()
    self.movement()
    self.detect_screen()
    self.collision_detect()