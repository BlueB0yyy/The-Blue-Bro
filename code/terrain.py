#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import TILE_SIZE


class Terrain:
    def __init__(self, level, name, seq, position):
        self.name = name
        # print(name)
        self.surf = pygame.image.load("./asset/" + level + "/" + name + "/"+str(seq)+".png").convert_alpha()  # pre-load da 1ª imagem
        self.surf = pygame.transform.scale(self.surf, (TILE_SIZE,TILE_SIZE))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def draw(self, window):
        window.blit(self.surf, self.rect)