#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code import score
from code.const import BG_WIDTH, BG_HEIGHT
from code.level import Level
from code.menu import Menu
from code.score import Score


class Game:
    def __init__(self):
        print('Setup Start')
        pygame.init()
        self.window = pygame.display.set_mode((BG_WIDTH,BG_HEIGHT))#pygame.FULLSCREEN)
        pygame.display.set_caption("The Blue Bro")
        print('Setup end')

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()
            match menu_return:
                case "Exit":
                    pygame.quit()
                    print('Encerrando')
                    quit()
                case "Start Game":
                    level = Level(self.window, 'Level1', score)
                    level_return = level.run()
                case "Score":
                    score.show() # implementar score com base no tempo


