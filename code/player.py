#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import BG_WIDTH, BG_HEIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, sprite_set: str):
        super().__init__(name, position, sprite_set)


    def walk(self, ):
        pressed_key = pygame.key.get_pressed()
        # if pressed_key[pygame.K_RIGHT]:
        #     self.

    def run(self, ):
        pass

    def jump(self, ):
        pass
        #increase sprite (y)

    def punch(self, ):
        pass

    # def idle_animation(self, x, y, w, h, menu_rect):
    #     sprite = pygame.Surface((w,h))
    #     sprite.set_colorkey((0,0,0))
    #     #sprite.blit(self.surf, menu_rect, (x,y,w,h))
    #     return sprite
