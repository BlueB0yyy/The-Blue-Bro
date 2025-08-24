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

        clock = pygame.time.Clock()

        level_obj = EntityFactory.draw_level(self.tile_map, self.name)
        #print(len(level_obj))

        for line in range(len(level_obj)):
            for column in range(len(level_obj[line])):
                obj = level_obj[line][column]
                if isinstance(column, Entity):
                    self.entity_list.append(obj)
                    print(self.entity_list)
                elif isinstance(obj, Terrain):
                    self.tiles.append(obj)
                    #print(self.tiles)
                else:
                    pass

        player = None
        print('teste')
        print(len(self.entity_list))
        for ent_group in range(len(self.entity_list)):
            print(self.entity_list[ent_group])
            print('teste')
            for ent in self.entity_list[ent_group]:
                print(ent)
                if isinstance(ent, Player):
                    player = ent
                    print('teste')
                    idle_frames = player.load_frames((50, 300))
                    player.set_animation("idle", idle_frames)

        # for ent in range(len(self.entity_list)):
        #     for element in range(len(self.entity_list[ent])):
        #         entity = self.entity_list[ent][element]
        #         if isinstance(entity, Player):
        #             ent_list = entity.load_frames(entity.rect, (50, 300))
        #             # self.window.blit(source=ent_list[index_animation],
        #             #dest = entity.rect)
        #         else:
        #             self.window.blit(source=self.entity_list[ent][element].surf,
        #                              dest=self.entity_list[ent][element].rect)

        while True:

            dt = clock.tick(60)  # delta time

            self.window.fill((0, 0, 0))

            #print(len(self.tiles))
            for ls in range(len(self.tiles)):
                for tile in range(ls):
                    drawn_tile = self.tiles[ls]
                    self.window.blit(drawn_tile.surf, drawn_tile.rect)

            for entity_l in range(len(self.entity_list)):
                for entity in range(entity_l):
                    ent = self.entity_list[entity_l]
                    #print(ent)
                    ent.update(dt)
                    self.window.blit(ent.get_frame(), ent.rect)

            # self.window.blit(source=ent_list[index_animation],dest = ent_list.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print('Encerrando')
                    quit()
