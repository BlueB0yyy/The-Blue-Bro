#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

import pygame

from code.const import SPRITE_COORDINATES, SPRITE_DIMENSIONS, SPRITE_DIFFERENCE, SPRITE_LIMIT


class Entity(ABC):
    def __init__(self, name: str, position: tuple, sprite_set:str):
        self.name = name #nome da entidade
        self.sprite_set = sprite_set  # Para alteração dependendo do botão pressionado

        self.surf = pygame.image.load("./asset/"+name+"/"+sprite_set+".png").convert_alpha() #1ª imagem

        self.rect = self.surf.get_rect(left=position[0], top=position[1]) #Onde vai ser desenhado (posição na tela)

        self.sprite_diff = SPRITE_DIFFERENCE[self.name][self.sprite_set] #espaço entre sprites
        self.sprite_limit = SPRITE_LIMIT[self.name][self.sprite_set] #limite do sprite (último pixel com imagem)
        self.xy = [
            SPRITE_COORDINATES[self.name][self.sprite_set]["x"],
            SPRITE_COORDINATES[self.name][self.sprite_set]["y"]
        ] #coordenadas iniciais (x esquerda, y topo)
        self.dimensions = (
            SPRITE_DIMENSIONS[self.name][self.sprite_set]["w"],
            SPRITE_DIMENSIONS[self.name][self.sprite_set]["h"]
        ) #coordenadas finais (w direita, h baixo)

        self.animations = {}
        self.animacao_atual = None
        self.index = 0
        self.timer = 0
        self.cooldown = 120  # ms por frame




    def upd(self, name: str, position: tuple, sprite_set:str):
        '''
        Atualiza todas as partes da entidade conforme uma ação seja executada (principalmente as animações de jogador\
        que poderão alterar conforme o botão apertado)
        :param name: Nome da entidade
        :param position: Posição do jogador na tela
        :param sprite_set: Sprite a ser trocado no update
        Só atualiza a entidade, não retorna nada
        '''

        self.name = name  # nome da entidade
        self.sprite_set = sprite_set  # Para alteração dependendo do botão pressionado

        self.surf = pygame.image.load("./asset/" + name + "/" + sprite_set + ".png").convert_alpha()  # 1ª imagem

        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # Onde vai ser desenhado (posição na tela)

        self.sprite_diff = SPRITE_DIFFERENCE[self.name][self.sprite_set]  # espaço entre sprites
        self.sprite_limit = SPRITE_LIMIT[self.name][self.sprite_set]  # limite do sprite (último pixel com imagem)
        self.xy = [
            SPRITE_COORDINATES[self.name][self.sprite_set]["x"],
            SPRITE_COORDINATES[self.name][self.sprite_set]["y"]
        ]  # coordenadas iniciais (x esquerda, y topo)
        self.dimensions = (
            SPRITE_DIMENSIONS[self.name][self.sprite_set]["w"],
            SPRITE_DIMENSIONS[self.name][self.sprite_set]["h"]
        )  # coordenadas finais (w direita, h baixo)

        self.animations = {}
        self.animacao_atual = None
        self.index = 0
        self.timer = 0
        self.cooldown = 120  # ms por frame

    def load_frames(self, outer_rect, position: tuple):
        frames = []
        for i in range(self.xy[0],self.sprite_limit,self.dimensions[0] + self.sprite_diff): # vai do 1º frame até o último
            frame_surface = pygame.Surface(self.dimensions,pygame.SRCALPHA).convert_alpha()
            frame_surface.set_colorkey((0, 0, 0))
            # print(i)
            frame_surface.blit(
                self.surf,
                (0,0),
                (i, self.xy[1], self.dimensions[0],self.dimensions[1]))
            frames.append(frame_surface)
        return frames

    def set_animation(self, name, frames, cooldown: int = None):
        self.animations[name] = {
            "frames": frames,
            "cooldown": cooldown,
        }

    def play_animation(self, name):
        if self.animacao_atual != name and name in self.animations:
            self.animacao_atual = name
            self.index = 0
            self.timer = 0
            self.cooldown = self.animations[name]["cooldown"]

    def update(self, dt):
        if self.animacao_atual is None:
            return
        self.timer += dt
        if self.timer >= self.cooldown:
            self.timer = 0
            self.index = (self.index + 1) % len(self.animations[self.animacao_atual]["frames"])

    def get_frame(self):
        if self.animacao_atual is None:
            return None
        return self.animations[self.animacao_atual]["frames"][self.index]

    def draw(self, surface):
        frame = self.get_frame()
        if frame:
            surface.blit(frame, self.rect.topleft)

    def walk(self, ):
        pass


