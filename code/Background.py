#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import *
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, sprite, index, tipo):
        super().__init__(name, position, sprite, index, tipo)

    def move(self, dx):
        self.rect.x += dx * BG_SPEED[self.index]

    def draw(self, surface, camera):
        surface_width = surface.get_width()
        x_pos = self.rect.x
        #print(x_pos)

        # desenha enquanto a imagem não cobre toda a tela
        while x_pos < surface_width:
            surface.blit(self.surf, (x_pos, self.rect.y))
            x_pos += self.surf.get_width()