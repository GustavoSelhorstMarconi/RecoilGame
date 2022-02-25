import pygame, math

class Weapon(pygame.sprite.Sprite):
  def __init__(self, player, groups):
    super().__init__(groups)
    self.image_2 = pygame.image.load('images/weapon.png').convert_alpha()
    self.image_2 = pygame.transform.rotate(self.image_2, 90)
    self.image = self.image_2
    self.rect = self.image.get_rect(midleft = player.rect.center)
    self.player = player
    self.display_surface = pygame.display.get_surface()

    # Shoot
    self.distance = pygame.math.Vector2()

    # Timer shoot
    self.can_shoot = True
    self.shoot_time = None
    self.shoot_daley = 300
  
  def movement(self):
    self.rect.center = self.player.rect.center

  def rotate(self):
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    direction_x = mouse_x - self.player.rect.centerx
    direction_y = mouse_y - self.player.rect.centery
    radians = math.atan2(direction_y, direction_x)
    degrees = math.degrees(radians)
    angle = -(degrees + 90)
    self.image = pygame.transform.rotate(self.image_2, angle)
    self.rect = self.image.get_rect(center = self.rect.center)
  
  def shoot(self):
    if pygame.mouse.get_pressed()[0] and self.can_shoot:
      self.can_shoot = False
      self.shoot_time = pygame.time.get_ticks()

      mouse_pos = pygame.mouse.get_pos()
      self.distance.x = mouse_pos[0] - self.rect.centerx
      self.distance.y = mouse_pos[1] - self.rect.centery
      
      distance = pygame.math.Vector2(self.distance.normalize())
      self.player.move_shoot(distance)
  
  def timer(self):
    current_time = pygame.time.get_ticks()

    if not self.can_shoot:
      if current_time - self.shoot_time >= self.shoot_daley:
        self.can_shoot = True

  def update(self):
    self.rotate()
    self.movement()
    self.timer()
    self.shoot()