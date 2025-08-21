#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv


class EntityFactory:
    def __init__(self):
        pass

    def get_entity(self, entity_type):
        pass

    def load_level(self, level_name):
        file_path = './asset/'+level_name+".csv"
        tile_map = []

        with open(file_path,'r') as f:
            for row in csv.reader(f): #para cada linha
                tile_map.append(list(map(int,row))) #faz um append da linha em formato int
        return tile_map

    def create_level(self):
