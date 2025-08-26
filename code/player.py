#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import BG_WIDTH, BG_HEIGHT, PLAYER_SPEED
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, sprite: str, seq: int):
        super().__init__(name, position, sprite, seq)
        self.speed = PLAYER_SPEED # Velocidade de movimento do jogador
        self.facing_right = True

        self.gravity = 1 #gravidade agindo sobre o jogador
        self.jump_strength = 20 # força de pulo (influenciado por gravidade)
        self.vel_y = 0 #
        self.on_ground = False
        self.is_jumping = False

    def apply_gravity(self, tiles):
        # aplica gravidade sempre
        self.vel_y += self.gravity # Empurra o jogador pra baixo
        self.rect.y += self.vel_y #Cola o rect nessa velocidade

        self.on_ground = False

        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if self.vel_y > 0 and self.rect.bottom <= tile.rect.bottom:
                    if self.vel_y > 0:  # caindo
                        self.rect.bottom = tile.rect.top
                        self.vel_y = 0
                        self.on_ground = True
                    elif self.vel_y < 0:  # batendo a cabeça
                        self.rect.top = tile.rect.bottom
                        self.vel_y = 0

    def walk(self, level_width):
        pressed_key = pygame.key.get_pressed() #Tecla
        moved = False #Não se moveu
        mult = 1
        if pressed_key[pygame.K_RIGHT] and self.rect.right < level_width: # Se apertar botão direito
            if pressed_key[pygame.K_SPACE]:
                mult = 2
            self.rect.centerx += self.speed * mult #Aumenta centerx
            self.facing_right = True # Vira para a direita
            moved = True #moveu
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            if pressed_key[pygame.K_SPACE]:
                mult = 2
            self.rect.centerx -= self.speed * mult
            self.facing_right = False
            moved = True
        return moved

    def jump(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.on_ground:
            self.vel_y = -self.jump_strength
            self.on_ground = False
            self.is_jumping = True  # começou o pulo
            return True
        return False

    def punch(self, ):
        pressed = pygame.key.get_pressed()
        action = False
        if pressed[pygame.K_z]:
            action = True
        return action



