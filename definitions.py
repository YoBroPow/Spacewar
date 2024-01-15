import pygame

width = 1280
height = 720
screen= pygame.display.set_mode ((width,height))
clock = pygame.time.Clock()
running = True
dt = clock.tick() / 1000
