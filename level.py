import pygame, sys
from player import Player
from settings import *
from weapon import Weapon

class Level():
  def __init__(self):
    self.display_surface = pygame.display.get_surface()
    self.visible_sprites = pygame.sprite.Group()

    self.player = Player((screen_width / 2, screen_height / 2), self.visible_sprites)
    self.weapon = Weapon(self.player, self.visible_sprites)

    self.status = 'Level'
  
  def check_kill(self):
    if self.player.rect.midtop[1] >= screen_height:
      self.status = 'Death'
      self.player.kill()
      self.weapon.kill()
  
  def run(self):
    if self.status == 'Level':
      if self.player:
        self.visible_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        self.check_kill()       

    elif self.status == 'Death':
      keys = pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
        self.player = Player((screen_width / 2, screen_height / 2), self.visible_sprites)
        self.weapon = Weapon(self.player, self.visible_sprites)
        self.status = 'Level'