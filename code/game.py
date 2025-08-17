#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        print('Setup Start')
        pygame.init()
        self.window = pygame.display.set_mode(size = (WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("The Blue Bro")
        print('Setup end')

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
