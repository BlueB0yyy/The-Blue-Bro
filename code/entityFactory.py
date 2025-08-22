#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from code.const import TILE_SIZE
from code.terrain import Terrain


class EntityFactory:

    @staticmethod
    def load_level(level_name):
        file_path = './asset/'+level_name+"/"+level_name+".csv"
        tile_map = []

        with open(file_path,'r') as f:
            for row in csv.reader(f): #para cada linha
                tile_map.append(list(map(int,row))) #faz um append da linha em formato int
        return tile_map

    @staticmethod
    def draw_level(tile_map, level):
        entity_list = []
        for line in range(0,len(tile_map)):
            #print(tile_map[line])
            #print(line) 18 (de 0 a 17)
            entity_list.append([])  #TESTAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            for column in range(0,len(tile_map[line])):
                print(column) #320 (de 0 a 319)
                obj = tile_map[line][column]
                print(obj)
                if column == -1: #player
                    pass
                if column == 0: #enemy
                    pass
                if 1 >= column <= 96:#tile
                    entity_list[line].append(Terrain(level, "Tile", column, (line*TILE_SIZE, column*TILE_SIZE))) #Adiciona um terreno na lista de entidades (TESTAR!!!!!!!!!!!!!!!!!!!)
                if 97 >= column <= 100: #bench
                    pass
                if 101 >= column <= 121: #bush
                    pass
                if 122 >= column <= 130: #fence
                    pass
                if column == 131: #fountain
                    pass
                if 132 >= column <= 146: #grass
                    pass
                if 147 >= column <= 152: #leaf
                    pass
                if column == 153: #box
                    pass
                if 154 >= column <= 155: #garbage can
                    pass
                if 156 >= column <= 157: #ladder
                    pass
                if 158 >= column <= 160: #ramp
                    pass
                if 161 >= column <= 164: #skate
                    pass
                if 165 >= column <= 168: #tree
                    pass
                if 169 >= column <= 174: #stone
                    pass
        return entity_list
