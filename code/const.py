from pygame.examples.grid import TILE_SIZE

#tabela de referência de id_list
# 0 = Player
# 1 = Enemy
# 2 > = Tiles

# Adicionar aspect ratio e resolução fixos pode ser mais interessante que ter ele fixo



# B

BG_WIDTH = 1728
BG_HEIGHT = 972



# C
COLOR_BLUE = (0,0,255)
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# E

ENT_SIZE = [
    2*TILE_SIZE, #Ocupa 2 tiles
]

# M

MENU_CHAR = (600, 675)
MENU_OPTION = [
    "Start Game",
    "Options",
    "Exit"
    ]

# R

RESOLUTION = [
    "1280x720",
]

# S

SPRITE_COORDINATES = {
    "Player": {
        "Ability_Use":{
            "x": 31,
            "y": 69
        }
    },
    "Enemies": {}
}

SPRITE_DIMENSIONS = {
    "Player": {
        "Ability_Use":{
            "w": 56,
            "h": 58
        }
    },
    "Enemies": {}
}

SPRITE_DIFFERENCE = {
    "Player": {
        "Ability_Use": 72
    },
    "Enemies": {}
}

SPRITE_LIMIT = {
    "Player": {
        "Ability_Use": 1182
    },
    "Enemies": {}
}

# T

TILE_SIZE = 36

#altura do personagem = 8cm
#extensão do mapa = 10x número de tiles (atualmeente, 480)
