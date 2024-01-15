import definitions
import pygame
import boundaries
import random

spawn1x = definitions.width/(32/31)
spawn1y = definitions.height/16
#spawn1 coordinate calculation

spawn2x = definitions.width/32
spawn2y = definitions.height/16
#spawn 2 coordinate calculation

spawn3x = definitions.width/32
spawn3y = definitions.height/(16/15)
#spawn 3 coordinate calculation

spawn4x = definitions.width/(32/31)
spawn4y = definitions.height/(16/15)
#spawn 4 coordinate calculation

spawn1 = pygame.Vector2(spawn1x, spawn1y)
spawn2 = pygame.Vector2(spawn2x, spawn2y)
spawn3 = pygame.Vector2(spawn3x, spawn3y)
spawn4 = pygame.Vector2(spawn4x, spawn4y)
spawnList = (spawn1, spawn2, spawn3, spawn4)
spawn = random.choice(spawnList)
#player spawn array

class Player():
    pos1 = pygame.Vector2(0,0)
    def __init__(spawn):
        pygame.draw.circle(definitions.screen,"yellow",Player.pos1,20)
        Player.pos1 = spawn
