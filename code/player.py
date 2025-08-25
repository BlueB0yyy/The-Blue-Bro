#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import BG_WIDTH, BG_HEIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, sprite: str, seq: int):
        super().__init__(name, position, sprite, seq)
        self.speed = 10

        self.gravity = 1
        self.jump_strength = 20
        self.vel_y = 0
        self.on_ground = False

    def apply_gravity(self, tiles):
        # aplica gravidade sempre
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # chão (exemplo: no fundo da tela)
        if self.rect.bottom >= 760:  # altura do "chão"
            self.rect.bottom = 760
            self.vel_y = 0
            self.on_ground = True

        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if self.vel_y > 0:  # caindo
                    self.rect.bottom = tile.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:  # batendo a cabeça
                    self.rect.top = tile.rect.bottom
                    self.vel_y = 0

    def walk(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT]:
            self.rect.centerx += self.speed
        if pressed_key[pygame.K_LEFT]:
            self.rect.centerx -= self.speed
        return True

    def run(self, ):
        pass

    def jump(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            if self.on_ground:
                self.vel_y = -self.jump_strength  # impulso pra cima
                self.on_ground = False
                self.rect.centery -= self.speed
        return True
        #increase sprite (y)

    def punch(self, ):
        pass



