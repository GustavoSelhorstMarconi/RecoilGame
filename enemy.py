import pygame

class Enemy(pygame.sprite.Sprite):
  def __init__(self, pos, groups, type_sprite, player, speed, change_text_kill):
    super().__init__(groups)
    self.image = pygame.Surface((20, 20))
    self.rect = self.image.get_rect(center = pos)
    self.type = type_sprite
    self.player = player
    self.change_text_kill = change_text_kill
    self.visible_sprites = groups[0]
    
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
              return

  def find_direction(self):
    self.direction.x = self.player.rect.centerx - self.rect.centerx
    self.direction.y = self.player.rect.centery - self.rect.centery

  def movement(self):
    self.find_direction()
    self.rect.center += self.direction.normalize() * self.speed
  
  def update(self):
    self.movement()
    self.check_kill()