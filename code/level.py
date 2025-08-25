#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player
from code.terrain import Terrain


class Level:
    def __init__(self, window, name):
        self.window = window # janela (global)
        self.name = name # nome do nível

        self.entity_list: list[Entity] = [] #lista de ENTIDADES
        self.tiles: list[Terrain] = [] #lista de TERRENOS
        self.tile_map = EntityFactory.load_level(self.name)  #lista de INDEX de elementos

        #print(self.entity_list)

    def run(self, ):
        pygame.mixer_music.load('./asset/Sound/Game/Menu.wav')
        pygame.mixer_music.play(-1)


        #frame rate
        clock = pygame.time.Clock()

        #Entidades e terrenos
        level_obj = EntityFactory.draw_level(self.tile_map, self.name)
        #print(len(level_obj))


        #Carrega os objetos dentro do level_object
        for line in range(len(level_obj)):
            for column in range(len(level_obj[line])):

                #Determina o objeto
                obj = level_obj[line][column]

                #Se for entidade
                if isinstance(obj, Entity):
                    self.entity_list.append(obj)
                    #print(self.entity_list)

                #Se for terreno
                elif isinstance(obj, Terrain):
                    self.tiles.append(obj)
                    # print(obj.rect)
                    # print(obj.surf)

                #Se for ar
                else:
                    pass

        player_index = 0
        enemy_index = 0
        timer_animacao = 0
        cooldown_animacao = 150
        sent=True
        anda = False
        pula = False

        while True:

            delay = clock.tick(60)
            timer_animacao += delay

            if timer_animacao >= cooldown_animacao:
                 timer_animacao = 0
                 if sent:
                    player_index += 1
                 else:
                    player_index -= 1

            self.window.fill((0, 0, 0))

            #print(len(self.tiles))
            for ls in range(len(self.tiles)):
                drawn_tile = self.tiles[ls]
                #print(len(self.tiles))
                self.window.blit(drawn_tile.surf, drawn_tile.rect)


            for ent in self.entity_list:
                if isinstance(ent,Player):
                    anda = ent.walk()
                    pula = ent.jump()
                    ent.apply_gravity(self.tiles)
                    if anda:
                        player_index = 0
                        player_index = ent.upd(ent.name, ent.position, "Walk", player_index)
                    if pula:
                        player_index = 0
                        player_index = ent.upd(ent.name,ent.position,"Jump",player_index)
                    else:
                        player_index = ent.upd(ent.name, ent.position, ent.sprite, player_index)
                else:
                    enemy_index = ent.upd(ent.name,ent.position,ent.sprite,enemy_index)
                self.window.blit(source=ent.surf,dest = ent.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print('Encerrando')
                    quit()

