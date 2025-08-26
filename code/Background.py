#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.const import *
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= const.ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = const.WIN_WIDTH