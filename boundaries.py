
import definitions
import player_spawns
def boundaries():
        if player_spawns.Player.pos1.x > definitions.width + 40:
            player_spawns.Player.pos1.x = 0 - 40
        if player_spawns.Player.pos1.x < 0 - 40: 
            player_spawns.Player.pos1.x = definitions.width + 40 
        if player_spawns.Player.pos1.y > definitions.height + 40:
            player_spawns.Player.pos1.y = 0 - 40
        if player_spawns.Player.pos1.y < 0 - 40:
            player_spawns.Player.pos1.y = definitions.height

    #teleports player when out of bounds