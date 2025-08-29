#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import *
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, sprite, index, tipo):
        super().__init__(name, position, sprite, index, tipo)

    def move(self, dx):
        self.rect.x -= dx * BG_SPEED[self.index]

    def draw(self, surface, camera):
        # largura total da tela (a janela)
        screen_width = surface.get_width()

        # posição inicial já considerando a câmera
        start_x = - (camera.offset.x * BG_SPEED[self.index]) % BG_WIDTH

        # desenha quantas cópias forem necessárias para cobrir a tela
        x = start_x - BG_WIDTH
        while x < screen_width:
            surface.blit(self.surf, (x, self.rect.y))
            x += BG_WIDTH