#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

import pygame

from code.const import SPRITE_COORDINATES, SPRITE_DIMENSIONS, SPRITE_DIFFERENCE, SPRITE_LIMIT


class Entity(ABC):
    def __init__(self, name: str, position: tuple, sprite_set:str):
        self.name = name #nome da entidade
        self.surf = pygame.image.load("./asset/"+name+"/"+sprite_set+".png").convert_alpha() #pre-load da 1ª imagem
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.sprite_set = sprite_set
        self.sprite_diff = SPRITE_DIFFERENCE[self.name][self.sprite_set]
        self.sprite_limit = SPRITE_LIMIT[self.name][self.sprite_set]
        self.xy = [SPRITE_COORDINATES[self.name][self.sprite_set]["x"],SPRITE_COORDINATES[self.name][self.sprite_set]["y"] ]
        self.dimensions = (SPRITE_DIMENSIONS[self.name][self.sprite_set]["w"],SPRITE_DIMENSIONS[self.name][self.sprite_set]["h"] )

        #Só do sprite nas classes entity
        self.sprite = pygame.Surface(self.dimensions)
        self.sprite.set_colorkey((0,0,0))


    def walk(self, ):
        pass
