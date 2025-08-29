#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SCORE
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, sprite: str, seq: int, tipo: str):
        super().__init__(name, position, sprite, seq, tipo)
        self.direction = 1  # 1 = direita, -1 = esquerda
        self.speed = 2
        self.range = 100  # quanto pode andar
        self.start_x = position[0]

    def walk(self, ):
        
        # rect aumenta/diminui pelo speed pela direção (que pode ser negativa = andar pra trás)
        self.rect.x += self.speed * self.direction

        # verifica se saiu do range
        if abs(self.rect.x - self.start_x) > self.range:
            # muda de direção 
            self.direction *= -1
            self.facing_right = False
        self.facing_right = self.direction > 0
  
        # testar com o enemy mais longe (tem que ser natural)
        # adicionar detecção de player (?) (quando ver o player, bate) (opcional)

