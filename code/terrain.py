#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import TILE_SIZE


class Terrain:
    def __init__(self, level, name, seq, position):

        # nome do terreno
        self.name = name
        # print(name)

        #Imagen do terreno (equivalente a sequência do CSV)
        self.surf = pygame.image.load("./asset/" + level + "/" + name + "/"+str(seq)+".png").convert_alpha()

        # Escalar por medida do terreno (não é o tamanho original)
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE,TILE_SIZE))

        # Rect correspondente ao tamanho aumentado da Surface 
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    # Método de desenho próprio
    def draw(self, window):
        window.blit(self.surf, self.rect)