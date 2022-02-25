import pygame, sys
from level import Level
from settings import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  screen.fill((230, 230, 230))
  level.run()

  pygame.display.update()
  clock.tick(60)