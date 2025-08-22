#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import BG_WIDTH, BG_HEIGHT, COLOR_BLUE, SPRITE_COORDINATES, SPRITE_DIMENSIONS, SPRITE_LIMIT, \
    SPRITE_DIFFERENCE, MENU_CHAR, MENU_OPTION, COLOR_YELLOW, COLOR_WHITE
from code.player import Player
import time


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.transform.scale(pygame.image.load('./asset/Level1/Background/Day/Background.png').convert_alpha(),(BG_WIDTH, BG_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)
        #self.rect.center = window.get_rect().center

    def run(self, ):
        option = 0
        pygame.mixer_music.load('./asset/Sound/Game/Tense.wav')
        pygame.mixer_music.play(-1)
        # Inicializa o Player
        player1 = Player('Player', (50,300), "Ability_Use")
        #Começa com o x da 1ª imagem
        x = player1.xy[0]
        while True:
            # Limpar a imagem da sprite anterior
            player1.sprite.fill((0, 0, 0, 0))
            # metodo para desenhar a imagem do BG (vem da superfície e DESENHA no retângulo)
            self.window.blit(source=self.surf, dest=self.rect)
            # atenção! Deve ser desenhado DEPOIS da tela (senão fica sobreposto)
            self.text_menu(150, "The Blue", COLOR_BLUE, (BG_WIDTH / 4, 80))
            self.text_menu(150, "Bro", COLOR_BLUE, (BG_WIDTH / 4, 220))

            #Player_animation
            #Se o x for maior que o limite da imagem (última animação)
            if x > player1.sprite_limit:
                #volta pro começo
                x = SPRITE_COORDINATES[player1.name][player1.sprite_set]["x"]
            else:
                #Desenha a próxima imagem (soma do w da image + diferença)
                x += player1.dimensions[0] + player1.sprite_diff
                time.sleep(0.05)

            #atualiza valor de x da classe para o novo x dinâmico
            player1.xy[0] = x
            #Atualiza a sprite impressa
            player1.sprite.blit(player1.surf, self.rect, (player1.xy[0], player1.xy[1],player1.dimensions[0],player1.dimensions[1]))
            #Aumenta o tamanho da imagem
            blue1 = pygame.transform.scale(player1.sprite, (MENU_CHAR[0], MENU_CHAR[1]))
            self.window.blit(source=blue1, dest=player1.rect)

            for opt in range(len(MENU_OPTION)):
                if opt == option:
                    self.text_menu(100, MENU_OPTION[opt], COLOR_YELLOW, (BG_WIDTH - (BG_WIDTH / 4), 400 + 130 * opt))
                else:
                    self.text_menu(100, MENU_OPTION[opt], COLOR_WHITE, (BG_WIDTH - (BG_WIDTH / 4), 400 + 130 * opt))

            pygame.display.flip()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print('Encerrando')
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if option < len(MENU_OPTION) - 1:
                            option += 1
                        else:
                            option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if option > 0:
                            option -= 1
                        else:
                            option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[option]


    def text_menu(self, size:int, text:str, color:tuple, pos: tuple):
        font: Font = pygame.font.SysFont("Comic Sans",size=size)
        text_surf: Surface = font.render(text, True, color)
        text_rect: Rect = text_surf.get_rect(center=pos)
        self.window.blit(source=text_surf, dest=text_rect)


