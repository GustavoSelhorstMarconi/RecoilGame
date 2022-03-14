import pygame, math

class Weapon(pygame.sprite.Sprite):
  def __init__(self, player, groups, type_sprite):
    super().__init__(groups)
    self.image_2 = pygame.image.load('images/weapons/weapon2.png').convert_alpha()
    self.image_2 = pygame.transform.rotate(self.image_2, 90)
    self.image = self.image_2
    self.rect = self.image.get_rect(midleft = player.rect.center)
    self.player = player
    self.display_surface = pygame.display.get_surface()
    self.type = type_sprite

    # Shoot
    self.distance = pygame.math.Vector2()
    self.list_points_distance = []

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
    if pygame.mouse.get_pressed()[0] and self.can_shoot and self.player.shoot_available >= 1:
      self.can_shoot = False
      self.shoot_time = pygame.time.get_ticks()
      self.player.shoot_available -= 1
      self.player.status.change_text_shoot_available()

      mouse_pos = pygame.mouse.get_pos()
      self.distance.x = mouse_pos[0] - self.rect.centerx
      self.distance.y = mouse_pos[1] - self.rect.centery
      
      vec_distance = pygame.math.Vector2(self.distance.normalize())
      self.create_line_shoot(vec_distance, self.distance.magnitude())
      self.player.move_shoot(vec_distance)
  
  def create_line_shoot(self, vec_distance, distance):
    self.list_points_distance = []

    for i in range(int(distance)):
      self.list_points_distance.append(self.rect.center + vec_distance * i)
    
    pygame.draw.line(self.display_surface, (31, 174, 209), self.list_points_distance[0], self.list_points_distance[-1] , 5)

  def clean_shoot_points(self):
    if self.can_shoot:
      self.list_points_distance = []
  
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
    self.clean_shoot_points()