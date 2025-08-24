#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

import pygame

from code.const import SPRITE_COORDINATES, SPRITE_DIMENSIONS, SPRITE_DIFFERENCE, SPRITE_LIMIT, TILE_SIZE


class Entity(ABC):
    def __init__(self, name: str, position: tuple, sprite_set:str):
        self.name = name #nome da entidade

        self.surf = pygame.image.load("./asset/"+name+"/"+sprite_set+".png").convert_alpha() #1ª imagem

        self.rect = self.surf.get_rect(left=position[0], top=position[1]) #Onde vai ser desenhado (posição na tela)

        self.mask = pygame.mask.from_surface(self.surf)

        self.mask_image = self.mask.to_surface()

        self.sprite_set = sprite_set #Para alteração dependendo do botão pressionado

        self.sprite_diff = SPRITE_DIFFERENCE[self.name][self.sprite_set] #espaço entre sprites

        self.sprite_limit = SPRITE_LIMIT[self.name][self.sprite_set] #limite do sprite (último pixel com imagem)

        self.xy = [SPRITE_COORDINATES[self.name][self.sprite_set]["x"],SPRITE_COORDINATES[self.name][self.sprite_set]["y"] ] #coordenadas iniciais (x esquerda, y topo)

        self.dimensions = (SPRITE_DIMENSIONS[self.name][self.sprite_set]["w"],SPRITE_DIMENSIONS[self.name][self.sprite_set]["h"]) #coordenadas finais (w direita, h baixo)

        self.frame_surface = []

        self.frame_surf_rect = []

        self.animations = {}

        self.animacao_atual = None
        self.index = 0
        self.timer = 0
        self.cooldown = 100  # ms por frame

    def load_frames(self, outer_rect, position: tuple):
        frames = []
        rects = []
        for i in range(self.xy[0],self.sprite_limit,self.dimensions[0] + self.sprite_diff): # vai do 1º frame até o último
            frame_surface = pygame.Surface(self.dimensions,pygame.SRCALPHA).convert_alpha()
            frame_surface.set_colorkey((0, 0, 0))
            # print(i)
            frame_surface.blit(self.surf, outer_rect, (i, self.xy[1], self.dimensions[0],self.dimensions[1]))
            frames.append(frame_surface)
            frame_rect = frame_surface.get_rect(left=position[0], top=position[1])
            rects.append(frame_rect)
        self.frame_surf_rect = rects
        self.frame_surface = frames
        return frames

    def set_animation(self, name, frames):
        self.animations[name] = frames

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.cooldown:
            self.timer = 0
            self.index = (self.index + 1) % len(self.animations[self.animacao_atual])

    def get_frame(self):
        return self.animations[self.animacao_atual][self.index]

    def walk(self, ):
        pass
