import pygame

class Particle(pygame.sprite.Sprite):
  def __init__(self, pos, animation_frames, groups, particle_type):
    super().__init__(groups)
    self.frame_index = 0
    self.frames = animation_frames
    self.frame_speed = 0.25
    self.image = self.frames[self.frame_index]
    self.rect = self.image.get_rect(center = pos)
    self.type = particle_type

  def animation(self):
    self.frame_index += self.frame_speed
    
    if self.frame_index >= len(self.frames):
      self.kill()
    else:
      self.image = self.frames[int(self.frame_index)]

  def update(self):
    self.animation()