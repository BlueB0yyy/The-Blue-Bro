from pygame.examples.grid import TILE_SIZE


# B

BG_WIDTH = 1728
BG_HEIGHT = 972

# Definido só caso queira alterar futuramente (poderia ser só a seq da classe)
BG_SPEED = {
    0: 0.1,
    1: 0.3,
    2: 0.6,
    3: 0.8,
    4: 1
}

# C
COLOR_BLUE = (0,0,255)
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)
COLOR_RED = (255,0,0)

# E

ENTITY_HEALTH = {
    "Player": 100,
    "Enemy": 50,
    "Level1": 1000000
}

ENTITY_DAMAGE = {
    "Player": 100,
    "Enemy": 50,
    "Level1": 0
}

ENTITY_SCORE = {
    "Player": 0,
    "Enemy": 10,
    "Level1": 0
}

# M

MENU_CHAR = (600, 675)
MENU_OPTION = [
    "Start Game",
    "Score",
    "Exit"
    ]

# P

PLAYER_SPEED = 8

# S

SCORE_POS = {'Title': (BG_WIDTH / 2, 100),
             'EnterName': (BG_WIDTH / 2, 200),
             'Label': (BG_WIDTH / 2, 200),
             'Name': (BG_WIDTH / 2, 140),
             0: (BG_WIDTH / 2, 250),
             1: (BG_WIDTH / 2, 310),
             2: (BG_WIDTH / 2, 390),
             3: (BG_WIDTH / 2, 470),
             4: (BG_WIDTH / 2, 550),
             5: (BG_WIDTH / 2, 630),
             6: (BG_WIDTH / 2, 690),
             7: (BG_WIDTH / 2, 770),
             8: (BG_WIDTH / 2, 850),
             9: (BG_WIDTH / 2, 930),
             }


# T

TILE_SIZE = 54
#18 de altura, 32 de largura

#altura do personagem = 8cm
#extensão do mapa = 10x número de tiles (atualmeente, 480)
