#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import BG_WIDTH, BG_HEIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, sprite_set: str):
        super().__init__(name, position, sprite_set)

        #idle_frames = self.load_frames()
        #self.set_animation(sprite_set, idle_frames, cooldown=200)

    def load_menu(self, outer_rect):
        frames = []
        for i in range(self.xy[0],self.sprite_limit,self.dimensions[0] + self.sprite_diff): # vai do 1º frame até o último
            frame_surface = pygame.Surface(self.dimensions,pygame.SRCALPHA).convert_alpha()
            frame_surface.set_colorkey((0, 0, 0))
            # print(i)
            frame_surface.blit(
                self.surf,
                outer_rect,
                (i, self.xy[1], self.dimensions[0],self.dimensions[1]))
            frames.append(frame_surface)
        return frames



















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
        self.load_frames()
        #aplicar dano se o inimigo estiver na área

    def handle_input(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
            self.play_animation("Casting Spell")
        else:
            self.play_animation("idle")

    # def idle_animation(self, x, y, w, h, menu_rect):
    #     sprite = pygame.Surface((w,h))
    #     sprite.set_colorkey((0,0,0))
    #     #sprite.blit(self.surf, menu_rect, (x,y,w,h))
    #     return sprite
