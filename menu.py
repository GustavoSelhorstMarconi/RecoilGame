import pygame

class Item:
  def __init__(self, left, top, width, height, text, index):
    self.display_surface = pygame.display.get_surface()
    self.rect = pygame.Rect(left, top, width, height)
    self.index = index
    self.font = pygame.font.Font(None, 20)
    self.text_surf = self.font.render(text, True, (0, 0, 0))
    
    self.selected = False
    self.selectedColor = (255, 0, 0)
    self.deselectedColor = (80, 80, 80)
    self.color = self.deselectedColor

  def draw_rect(self):
    if self.selected:
      self.color = self.selectedColor
    else:
      self.color = self.deselectedColor
    pygame.draw.rect(self.display_surface, self.color, self.rect)
  
  def display_text(self):
    self.display_surface.blit(self.text_surf, (self.rect.centerx - self.text_surf.get_width() / 2, self.rect.centery - self.text_surf.get_height() / 2))