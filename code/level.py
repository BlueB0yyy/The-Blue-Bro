#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        #self.entity_list.extend(EntityFactory.load_level(self.name))  #Arquivo .csv carregado em lista)
        self.tile_map = EntityFactory.load_level(self.name)
        self.entity_list.extend(EntityFactory.draw_level(self.tile_map, self.name))
        print(self.entity_list)
        self.size = None

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
