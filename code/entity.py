#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from abc import ABC

import pygame

from code.const import BG_WIDTH, BG_HEIGHT, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple, sprite:str, index:int, tipo: str):
        # nome da entidade
        self.facing_right = None
        self.name = name

        #Conjunto de sprites (string)
        self.sprite = sprite

        self.tipo = tipo

        # Posição na tela
        self.position = position

        # Índice da animação
        self.index = index

        # Quantidade de sprites (para determinar limte das animações
        self.quant_sprites = len(os.listdir(f"./asset/{name}/{tipo}/{sprite}"))
        if name == 'Level1':
            self.quant_sprites -= 1

        # Superfície da animação atual

        self.frames = []
        for image in range(self.quant_sprites):
            self.frames.append(pygame.image.load(f"./asset/{name}/{tipo}/{sprite}/{image}.png").convert_alpha())

        self.surf = pygame.image.load(f"./asset/{name}/{tipo}/{sprite}/{str(self.index)}.png").convert_alpha()  # 1ª imagem

        if name == 'Level1':
            self.surf = pygame.transform.scale(self.surf, (BG_WIDTH, BG_HEIGHT)) #Bg

        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        self.animacao_atual = None
        self.index = 0
        self.timer = 0
        self.cooldown = 120  # ms por frame


        self.gravity = 1  # gravidade agindo sobre o jogador
        self.vel_y = 0  #
        self.on_ground = False

        # CRIAR NO CONST
        self.score = ENTITY_SCORE[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.kill = None


    def upd(self, name: str, position: tuple, sprite:str, tipo: str, delay: int):
        '''
        Atualiza todas as partes da entidade conforme uma ação seja executada (principalmente as animações de jogador\
        que poderão alterar conforme o botão apertado)
        :param delay:
        :param tipo:
        :param seq:
        :param sprite:
        :param name: Nome da entidade
        :param position: Posição do jogador na tela
        :param sprite_set: Sprite a ser trocado no update
        Só atualiza a entidade, não retorna nada
        '''

        self.quant_sprites = len(os.listdir(f"./asset/{name}/{tipo}/{sprite}"))

        self.timer += delay
        if self.timer >= self.cooldown:
            self.timer = 0
            self.index += 1
            self.index = self.index % self.quant_sprites
            if self.index == self.quant_sprites:
                self.index = 0



        if self.animacao_atual != sprite:
            self.animacao_atual = sprite
            self.index = 0
            self.frames = []
            quant_sprites = len(os.listdir(f"./asset/{name}/{tipo}/{sprite}"))
            for i in range(quant_sprites):
                self.frames.append(pygame.image.load(f"./asset/{name}/{tipo}/{sprite}/{i}.png").convert_alpha())

        self.surf = self.frames[self.index]

        self.name = name

        # Conjunto de sprites (string)
        self.sprite = sprite

        self.position = position

        if name == 'Level1':
            self.surf = pygame.transform.scale(self.surf, (BG_WIDTH, BG_HEIGHT)) #Bg
            
        if name != 'Level1':
            if not self.facing_right:
                self.surf = pygame.transform.flip(self.surf, True, False)

    def apply_gravity(self, tiles):
        # aplica gravidade sempre (valor
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

