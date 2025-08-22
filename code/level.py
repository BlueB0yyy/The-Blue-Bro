#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.load_level(self.name))  #Arquivo .csv carregado em lista)
        self.size = None

    def run(self, ):
        tile_map = EntityFactory.load_level(self.name)
        print(self.entity_list)
        var = EntityFactory.draw_level(tile_map, self.name)
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
