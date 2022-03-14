import pygame

class Status:
  def __init__(self, player):
    self.player = player
    self.display_surface = pygame.display.get_surface()

    # Text shoot available
    self.font = pygame.font.Font(None, 30)
    self.text_shoot_available_surf = self.font.render(f'Shoot available: {str(self.player.shoot_available)}', 1, (0, 0, 189))
    self.text_shoot_available_rect = self.text_shoot_available_surf.get_rect(topleft = (50, 25))

    # Life
    self.life = pygame.image.load('images/support/life.png').convert_alpha()

  def change_text_shoot_available(self):
    self.text_shoot_available_surf = self.font.render(f'Shoot available: {str(self.player.shoot_available)}', 1, (0, 0, 189))
    self.text_shoot_available_rect = self.text_shoot_available_surf.get_rect(topleft = (25, 60))

  def display_shoot_available(self):
    self.display_surface.blit(self.text_shoot_available_surf, self.text_shoot_available_rect)

  def display_life(self):
    for i in range(self.player.hp):
      self.display_surface.blit(self.life, (25 + 25 * i, 25))