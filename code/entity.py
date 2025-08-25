#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from abc import ABC

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple, sprite:str, seq:int):
        # nome da entidade
        self.name = name

        #Conjunto de sprites (string)
        self.sprite = sprite

        self.position = position

        self.surfs = [pygame.image.load(f"./asset/{name}/{sprite}/{i}.png").convert_alpha() for i in range(3)]

        self.quant_sprites = len(os.listdir(f"./asset/{name}/{sprite}"))
        print(self.quant_sprites)

        self.surf = pygame.image.load("./asset/"+name+"/"+sprite+"/"+str(seq)+".png").convert_alpha() #1ª imagem

        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        self.animacao_atual = None
        self.index = 0
        self.timer = 0
        self.cooldown = 120  # ms por frame




    def upd(self, name: str, position: tuple, sprite:str, seq: int):
        '''
        Atualiza todas as partes da entidade conforme uma ação seja executada (principalmente as animações de jogador\
        que poderão alterar conforme o botão apertado)
        :param seq:
        :param sprite:
        :param name: Nome da entidade
        :param position: Posição do jogador na tela
        :param sprite_set: Sprite a ser trocado no update
        Só atualiza a entidade, não retorna nada
        '''

        if seq > 3:
            seq = 0

        self.name = name

        # Conjunto de sprites (string)
        self.sprite = sprite

        self.position = position

        self.surfs = [pygame.image.load(f"./asset/{name}/{sprite}/{i}.png").convert_alpha() for i in range(3)]

        self.quant_sprites = len(os.listdir(f"./asset/{name}/{sprite}"))

        self.surf = pygame.image.load(
            "./asset/" + name + "/" + sprite + "/" + str(seq) + ".png").convert_alpha()  # 1ª imagem

        return seq

    def walk(self, ):
        pass


