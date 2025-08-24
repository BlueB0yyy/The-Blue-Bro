#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player
from code.terrain import Terrain


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.tiles: list[Terrain] = []
        #self.entity_list.extend(EntityFactory.load_level(self.name))  #Arquivo .csv carregado em lista)
        self.tile_map = EntityFactory.load_level(self.name)
        #print(self.entity_list)
        self.size = None

        for obj in EntityFactory.draw_level(self.tile_map, self.name):
            if isinstance(obj, Entity):
                self.entity_list.append(obj)
            else:
                self.tiles.append(obj)

    def run(self, ):
        pygame.mixer_music.load('./asset/Sound/Game/Menu.wav')
        pygame.mixer_music.play(-1)

        index_animation = 0

        clock = pygame.time.Clock()

        timer_animacao = 0
        cooldown_animacao = 50

        for ent in range(len(self.entity_list)):
            for element in range(len(self.entity_list[ent])):
                entity = self.entity_list[ent][element]
                if isinstance(entity, Player):
                    ent_list = entity.load_frames(entity.rect, (50, 300))
                    # self.window.blit(source=ent_list[index_animation],
                    #dest = entity.rect)
                else:
                    self.window.blit(source=self.entity_list[ent][element].surf,
                                     dest=self.entity_list[ent][element].rect)

        while True:
            if timer_animacao >= cooldown_animacao:
                timer_animacao = 0
                index_animation = (index_animation + 1) % len(ent_list)

            self.window.blit(source=ent_list[index_animation],dest = ent_list.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print('Encerrando')
                    quit()
