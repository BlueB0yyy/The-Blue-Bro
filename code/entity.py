#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple, initial_image:str):
        self.name = name #nome da entidade
        self.surf = pygame.image.load("./asset/"+name+"/"+initial_image+".png").convert_alpha() #pre-load da 1ª imagem
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.initial_image = initial_image

    def walk(self, ):
        pass
