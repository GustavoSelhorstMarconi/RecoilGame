import pygame
from settings import import_folder
from particles import Particle

class Enemy(pygame.sprite.Sprite):
  def __init__(self, pos, groups, type_sprite, player, speed, change_text_kill):
    super().__init__(groups)
    self.frame_list = import_folder('images/enemies/bat')
    self.frame_index = 0
    self.frame_speed = 0.25
    self.image = self.frame_list[self.frame_index]
    self.rect = self.image.get_rect(center = pos)
    self.type = type_sprite
    self.player = player
    self.change_text_kill = change_text_kill
    self.visible_sprites = groups[0]

    # Explosion
    self.explosion_frames = import_folder('images/explosion')
    
    # Movement
    self.speed = speed
    self.direction = pygame.math.Vector2()
  
  def check_kill(self):
    '''if pygame.mouse.get_pressed()[0]:
      mouse_pos = pygame.mouse.get_pos()
      if self.rect.collidepoint(mouse_pos):
        self.kill()
        self.change_text_kill()'''

    for sprite in self.visible_sprites.sprites():
      if sprite.type == 'Weapon':
        if sprite.list_points_distance:
          for point in sprite.list_points_distance:
            if self.rect.collidepoint(point):
              self.kill()
              self.change_text_kill()
              Particle(self.rect.center, self.explosion_frames, self.visible_sprites, 'Kill_enemie')
              return

  def find_direction(self):
    self.direction.x = self.player.rect.centerx - self.rect.centerx
    self.direction.y = self.player.rect.centery - self.rect.centery

  def movement(self):
    self.find_direction()
    self.rect.center += self.direction.normalize() * self.speed

  def animate(self):
    self.frame_index += self.frame_speed
    if self.frame_index >= len(self.frame_list):
      self.frame_index = 0

    self.image = self.frame_list[int(self.frame_index)]
    self.rect = self.image.get_rect(center = self.rect.center)
  
  def update(self):
    self.movement()
    self.animate()
    self.check_kill()