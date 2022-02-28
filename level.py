import pygame, sys
import random
from player import Player
from settings import *
from weapon import Weapon
from enemy import Enemy

class Level():
  def __init__(self):
    self.display_surface = pygame.display.get_surface()
    self.visible_sprites = pygame.sprite.Group()
    self.collision_sprites = pygame.sprite.Group()

    # Player
    self.player = Player((screen_width / 2, screen_height / 2), self.visible_sprites, self.collision_sprites, 'Player')
    self.weapon = Weapon(self.player, self.visible_sprites, 'Weapon')

    # Status level
    self.status = 'Level_1'
    self.level = 1

    # Enemy
    self.create_enemy()
  
  def check_kill(self):
    if self.player.rect.midtop[1] >= screen_height or self.player.hp <= 0:
      self.status = 'Death'
      self.visible_sprites.empty()
      self.collision_sprites.empty()
  
  def create_enemy(self):
    if self.status == 'Level_1' and not self.collision_sprites:
      for i in range(5):
        pos = (random.randint(0, screen_width), random.randint(0, screen_height))
        Enemy(pos, [self.visible_sprites, self.collision_sprites], 'Enemy')

  def check_level(self):
    if not self.collision_sprites:
      self.level += 1
      if not str(self.level) in self.status:
        self.status = self.status[:-1]
        self.status += str(self.level)
  
  def run(self):
    if 'Level' in self.status:
      self.visible_sprites.update()
      self.visible_sprites.draw(self.display_surface)
      self.create_enemy()
      self.check_level()
      self.check_kill()

    elif self.status == 'Death':
      keys = pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
        self.player = Player((screen_width / 2, screen_height / 2), self.visible_sprites, self.collision_sprites, 'Player')
        self.weapon = Weapon(self.player, self.visible_sprites, 'Weapon')
        self.status = 'Level_1'