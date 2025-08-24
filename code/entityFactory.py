#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from code.const import TILE_SIZE
from code.player import Player
from code.terrain import Terrain


class EntityFactory:

    @staticmethod
    def load_level(level_name):
        file_path = './asset/'+level_name+"/"+level_name+".csv"
        tile_map = []

        with open(file_path,'r') as f:
            for row in csv.reader(f): #para cada linha
                tile_map.append(list(map(int,row))) #faz um append da linha em formato int
        print(tile_map)
        return tile_map

    @staticmethod
    def draw_level(tile_map, level):
        entity_list = []
        for line in range(0,len(tile_map)):
            #print(tile_map[line])
            #print(line) 18 (de 0 a 17)
            entity_list.append([])  #TESTAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            for column in range(0,len(tile_map[line])):
                #print(column) #320 (de 0 a 319)
                obj = tile_map[line][column]
                #print(obj)
                if obj == -1: #player
                    entity_list[line].append(Player("Player", (column, line), "Ability_Use"))
                if obj == 0: #enemy
                    pass
                if 1 <= obj <= 96:#tile
                    print(obj)
                    entity_list[line].append(Terrain(level, "Tile", obj, (column*TILE_SIZE, line*TILE_SIZE))) #Adiciona um terreno na lista de entidades (TESTAR!!!!!!!!!!!!!!!!!!!)
                if 97 >= obj <= 100: #bench
                    pass
                if 101 >= obj <= 121: #bush
                    pass
                if 122 >= obj <= 130: #fence
                    pass
                if obj == 131: #fountain
                    pass
                if 132 >= obj <= 146: #grass
                    pass
                if 147 >= obj <= 152: #leaf
                    pass
                if obj == 153: #box
                    pass
                if 154 >= obj <= 155: #garbage can
                    pass
                if 156 >= obj <= 157: #ladder
                    pass
                if 158 >= obj <= 160: #ramp
                    pass
                if 161 >= obj <= 164: #skate
                    pass
                if 165 >= obj <= 168: #tree
                    pass
                if 169 >= obj <= 174: #stone
                    pass
        print(entity_list)
        return entity_list
