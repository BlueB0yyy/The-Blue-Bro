#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, sprite: str, seq: int, tipo):
        super().__init__(name, position, sprite, seq, tipo)
        self.type = type
        self.direction = 1  # 1 = direita, -1 = esquerda
        self.speed = 2
        self.range = 100  # quanto pode andar
        self.start_x = position[0]

    def walk(self, ):
        self.rect.x += self.speed * self.direction

        # verifica se saiu do range
        if abs(self.rect.x - self.start_x) > self.range:
            self.direction *= -1

