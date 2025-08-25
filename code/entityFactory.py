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
        # print(tile_map)
        return tile_map


# X É COLUNA, Y É LINHA!


    @staticmethod
    def draw_level(tile_map, level):
        '''
        Metodo principalmente usado para criar objetos com uma posição de uma lista (atualmente - 24/08) a lista é dividida entre entidades e tiles
        :param tile_map:  mapa de tiles, adquirido no metodo load_level
        :param level: De qual nível carregar tiles
        :return: Lista de todas as entidades (air seria espaço vazio - usa pass depois)
        '''
        entity_list = []
        #print(len(tile_map))           18
        #print(len(tile_map[0]))            320
        for column in range(0,len(tile_map)):  #18 linhas
            #print(tile_map[line])
            #print(line) 18 (de 0 a 17)
            entity_list.append([])  #TESTAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            for line in range(0,len(tile_map[column])):
                #print(column) #320 (de 0 a 319)
                obj = tile_map[column][line] #referência do número em cada bloco do tile_map
                #print(obj)
                if obj == -2: #ar
                    entity_list[column].append('air')
                if obj == -1: #player
                    entity_list[column].append(Player("Player", (line*TILE_SIZE, column*TILE_SIZE), "Idle",0))
                if obj == 0: #enemy
                    pass
                if 1 <= obj <= 96:#tile
                    #print(column)
                    entity_list[column].append(Terrain(level, "Tile", obj, (line*TILE_SIZE, column*TILE_SIZE))) #Adiciona um terreno na lista de entidades (TESTAR!!!!!!!!!!!!!!!!!!!)
                    # print(entity_list[column][line].surf)
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
        # for line in entity_list:      18
        #     print(line, end='\n')
        #     for column in line
        # print(len(entity_list))
        # print(len(entity_list[0]))
        # print(len(entity_list[0][0]))
        # print(entity_list[0][0])
        return entity_list

# O blit do cenário só precisa ocorrer 1 vez (pra terreno)
# O blit das entidades tem que ocorrer em loop