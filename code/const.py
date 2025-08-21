from pygame.examples.grid import TILE_SIZE

#tabela de referência de id_list
# 0 = Player
# 1 = Enemy
# 2 > = Tiles

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

TILE_MAP = [ #36 (48 x 27) blocos na visão do jogador (15x48?)
    [],
    [],
    [],
    [],[],[]
]

TILE_SIZE = 36

#altura do personagem = 8cm
#extensão do mapa = 10x número de tiles (atualmeente, 480)