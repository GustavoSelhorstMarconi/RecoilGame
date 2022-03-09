import pygame, sys
import random
from player import Player
from settings import *
from weapon import Weapon
from enemy import Enemy
from menu import Item

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
    self.enemy_kill = 0
    self.aux_enemy_kill = None

    # Enemy
    self.create_enemy()

    # Display text level
    self.font_level_kill = pygame.font.Font(None, 30)
    self.text_level_surf = self.font_level_kill.render(self.status.replace('_', ' '), 1, (100, 100, 100))
    self.text_level_rect = self.text_level_surf.get_rect(center = (screen_width / 2, 50))

    # Display text kill
    self.text_kill_surf = self.font_level_kill.render(f'Enemies killed: {str(self.enemy_kill)}', 1, (190, 50, 50))
    self.text_kill_rect = self.text_kill_surf.get_rect(topleft = (25, screen_height - 50))

    # Menu death
    self.menu_list = []
    self.menu_text_list = ['Start', 'Exit']
    self.selected_menu_index = 0
  
  def check_kill(self):
    if self.player.rect.centery >= screen_height or self.player.hp <= 0:
      self.status = 'Death'
      self.visible_sprites.empty()
      self.collision_sprites.empty()
  
  def create_enemy(self):
    # Level 1
    if str(self.level) in self.status and not self.collision_sprites:
      amount_enemies = self.level - 1 if self.level != 1 else 1
      for i in range(random.randint(amount_enemies - 1, amount_enemies + 1)):
        pos = (random.randint(0, screen_width), random.randint(0, screen_height))
        Enemy(pos, [self.visible_sprites, self.collision_sprites], 'Enemy', self.player, 1.5 + (self.level / 10), self.change_text_kill)
        self.aux_enemy_kill = self.enemy_kill + len(self.collision_sprites.sprites())
    
    '''# Level 2
    if self.status == 'Level_2' and not self.collision_sprites:
      for i in range(6):
        pos = (random.randint(0, screen_width), random.randint(0, screen_height))
        Enemy(pos, [self.visible_sprites, self.collision_sprites], 'Enemy', self.player, 1.8)'''

  def check_level(self):
    if not self.collision_sprites.sprites() and self.enemy_kill == self.aux_enemy_kill and str(self.level) in self.status:
      self.level += 1
      self.status = self.status.replace(f'_{str(self.level - 1)}', f'_{str(self.level)}')
      self.change_text_level()

  def change_text_level(self):
    self.text_level_surf = self.font_level_kill.render(self.status.replace('_', ' '), 1, (100, 100, 100))
    self.text_level_rect = self.text_level_surf.get_rect(center = (screen_width / 2, 50))

  def change_text_kill(self):
    self.enemy_kill += 1
    self.text_kill_surf = self.font_level_kill.render(f'Enemies killed: {str(self.enemy_kill)}', 1, (190, 50, 50))
    self.text_kill_rect = self.text_kill_surf.get_rect(topleft = (25, screen_height - 50))

  def display_text(self):
    self.display_surface.blit(self.text_level_surf, self.text_level_rect)
    self.display_surface.blit(self.text_kill_surf, self.text_kill_rect)

  def reset_level(self):
    self.status = 'Level_1'
    self.change_text_level()
    self.level = 1
    self.enemy_kill = -1
    self.change_text_kill()
    self.create_enemy()

  def create_menu_death(self):
    if not self.menu_list:
      for index, text in enumerate(self.menu_text_list):
        self.menu_list.append(Item(screen_width / 2 - 100, screen_height / 2 - 100 + (75 * index), 200, 50, text, index))
   
  def display_menu_death(self):
    for menu in self.menu_list:
      menu.draw_rect()
      menu.display_text()
  
  def change_index_selected_menu(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and self.selected_menu_index == 0:
      self.selected_menu_index += 1
    if keys[pygame.K_UP] and self.selected_menu_index == 1:
      self.selected_menu_index -= 1

  def change_selected_menu(self):
    if self.menu_list:
      for index, menu in enumerate(self.menu_list):
        if index == self.selected_menu_index:
          menu.selected = True
        else:
          menu.selected = False

  def select_exit_option(self):
    keys = pygame.key.get_pressed()
    if self.menu_list:
      for menu in self.menu_list:
        if keys[pygame.K_SPACE]:
          # Start Option
          if self.menu_list[0].selected:
            self.player = Player((screen_width / 2, screen_height / 2), self.visible_sprites, self.collision_sprites, 'Player')
            self.weapon = Weapon(self.player, self.visible_sprites, 'Weapon')
            self.reset_level()
          if self.menu_list[1].selected:
          # Exit option
            pygame.quit()
            sys.exit()        
      
  def run(self):
    if 'Level' in self.status:
      self.visible_sprites.update()
      self.visible_sprites.draw(self.display_surface)
      self.display_text()
      self.check_level()
      self.create_enemy()
      self.check_kill()

    elif self.status == 'Death':
      self.create_menu_death()
      self.display_menu_death()
      self.change_index_selected_menu()
      self.change_selected_menu()
      self.select_exit_option()