# Turns
# 1) Determine turn order
# 2) Buy power plant
# 3) Buy Raw Materials
# 4) Build
# 5) Bureaucracy
import maps
import player
import materials

board = maps.usa()
players = [player.Player("Steven"), player.Player("Steve-bot")]
m = materials.Materials()
