import pygame
import random
import definitions
import boundaries
import player_spawns
pygame.init()


#declarations^^


while definitions.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            definitions.running = False 
    definitions.screen.fill("black")
    player_spawns.Player.__init__(player_spawns.spawn)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_spawns.Player.pos1.y -= 300 * dt
    if keys[pygame.K_s]:
        player_spawns.Player.pos1.y += 300 * dt
    if keys[pygame.K_a]:
        player_spawns.Player.pos1.x -= 300 * dt
    if keys[pygame.K_d]:
        player_spawns.Player.pos1.x += 300 * dt
    if keys[pygame.K_ESCAPE]:
        break
    boundaries.boundaries()    
    
    #player controls    


    pygame.display.flip()
    dt = definitions.clock.tick(60) / 1000
   

pygame.quit()