#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import os

from code.Background import Background
from code.const import TILE_SIZE, BG_WIDTH
from code.enemy import Enemy
from code.player import Player
from code.terrain import Terrain

from random import choice

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
        enemy_list = ["Plant", "Skeleton"]
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
                    entity_list[column].append(Player("Player", (line*TILE_SIZE, column*TILE_SIZE-100), "Idle",0, 'Blue'))
                if obj == 0: #enemy
                    entity_list[column].append(Enemy("Enemy", (line * TILE_SIZE, column * TILE_SIZE-85), "Walk", 0, choice(enemy_list)))
                if 1 <= obj <= 96:#tile
                    #print(column)
                    entity_list[column].append(Terrain(level, "Tile", obj, (line*TILE_SIZE, column*TILE_SIZE))) #Adiciona um terreno na lista de entidades (TESTAR!!!!!!!!!!!!!!!!!!!)
                    # print(entity_list[column][line].surf)
        return entity_list

# O blit do cenário só precisa ocorrer 1 vez (pra terreno)
# O blit das entidades tem que ocorrer em loop

    @staticmethod
    def create_bg(level_name):
        list_bg = []
        #Todos os formatos de level vão até 5
        for i in range(5):
            list_bg.append(Background(level_name, (0, 0), "Day", i, 'Background'))
        return list_bg
