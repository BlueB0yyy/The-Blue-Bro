from pygame.examples.grid import TILE_SIZE


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
COLOR_RED = (255,0,0)

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
        },
        "Casting Spell":{
            "x":43,
            "y":1
        }
    },
    "Enemies": {}
}

SPRITE_DIMENSIONS = {
    "Player": {
        "Ability_Use":{
            "w": 56,
            "h": 58
            },
        "Casting Spell": {
            "w": 30,
            "h": 127
        }
        },
    "Enemies": {}
}

SPRITE_DIFFERENCE = {
    "Player": {
        "Ability_Use": 72,
        "Casting Spell":98
    },
    "Enemies": {}
}

SPRITE_LIMIT = {
    "Player": {
        "Ability_Use": 1182,
        "Casting Spell": 1227
    },
    "Enemies": {}
}

# T

TILE_SIZE = 54
#18 de altura, 32 de largura

#altura do personagem = 8cm
#extensão do mapa = 10x número de tiles (atualmeente, 480)
