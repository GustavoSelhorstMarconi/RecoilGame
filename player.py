import pygame
import math
from settings import *
from status import Status

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups, collision_sprites, type_sprite):
    super().__init__(groups)
    self.image = pygame.image.load('images/player2/player0.png').convert_alpha()
    self.rect = self.image.get_rect(center = pos)
    self.direction = pygame.math.Vector2()
    self.collision_sprites = collision_sprites
    self.type = type_sprite
    self.display_surface = pygame.display.get_surface()

    # Fly magic
    self.flyMagic_surf = pygame.image.load('images/player2/flymagic.png').convert_alpha()
    self.flyMagic_rect = self.flyMagic_surf.get_rect(center = self.rect.midbottom)

    # Status
    self.hp = 3
    self.shoot_available = 0
    self.status = Status(self)

    # Vulnerability
    self.vulnerable = True
    self.vulnerable_time = None
    self.vulnerable_delay = 500

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
      if self.rect.colliderect(sprite) and self.vulnerable:
        self.vulnerable = False
        self.vulnerable_time = pygame.time.get_ticks()
        self.hp -= 1

  def timer(self):
    current_time = pygame.time.get_ticks()
    if not self.vulnerable:
      if current_time - self.vulnerable_time >= self.vulnerable_delay:
        self.vulnerable = True

  def change_shoot_available(self):
    self.shoot_available += len(self.collision_sprites.sprites()) + 3
    self.status.change_text_shoot_available()
  
  def animate(self):
    if not self.vulnerable:
      alpha = self.wave_value()
      self.image.set_alpha(alpha)
    else:
      self.image.set_alpha(255)

  def wave_value(self):
    alpha = math.sin(pygame.time.get_ticks())
    if alpha >= 0:
      return 255
    else:
      return 0
  
  def display_fly_magic(self):
    self.flyMagic_rect.center = self.rect.midbottom
    self.display_surface.blit(self.flyMagic_surf, self.flyMagic_rect)

  def update(self):
    self.fall()
    self.movement()
    self.detect_screen()
    self.collision_detect()
    self.animate()
    self.status.display_shoot_available()
    self.timer()
    self.status.display_life()
    self.display_fly_magic()