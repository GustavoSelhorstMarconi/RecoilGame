import pygame

class Enemy(pygame.sprite.Sprite):
  def __init__(self, pos, groups, type_sprite):
    super().__init__(groups)
    self.image = pygame.Surface((15, 15))
    self.rect = self.image.get_rect(center = pos)
    self.type = type_sprite
  
  def check_kill(self):
    if pygame.mouse.get_pressed()[0]:
      mouse_pos = pygame.mouse.get_pos()
      if self.rect.collidepoint(mouse_pos):
        self.kill()
  
  def update(self):
    self.check_kill()