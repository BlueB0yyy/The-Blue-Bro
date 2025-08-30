#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Camera import Camera
from code.const import TILE_SIZE, COLOR_GREEN, BG_WIDTH, COLOR_WHITE
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player
from code.score import Score
from code.terrain import Terrain


class Level:
    def __init__(self, window, name):
        self.window = window # janela (global)
        self.name = name # nome do nível

        self.entity_list: list[Entity] = [] #lista de ENTIDADES
        self.tiles: list[Terrain] = [] #lista de TERRENOS
        self.tile_map = EntityFactory.load_level(self.name)  #lista de INDEX de elementos
        self.bg = EntityFactory.create_bg(self.name) #Criação do Bg

        #print(self.entity_list)

    def run(self, score: list):
        pygame.mixer_music.load('./asset/Sound/Game/Menu.wav')
        pygame.mixer_music.play(-1)

        #tempo do jogo
        game_time = 0
        time_stop = False
        time_controller = 0


        #frame rate
        clock = pygame.time.Clock()

        #Entidades e terrenos
        level_obj = EntityFactory.draw_level(self.tile_map, self.name)
        #print(len(level_obj))


        #Carrega os objetos dentro do level_object
        for line in range(len(level_obj)):
            for column in range(len(level_obj[line])):

                #Determina o objeto
                obj = level_obj[line][column]

                #Se for entidade
                if isinstance(obj, Entity) and obj.name != 'Level1':
                    self.entity_list.append(obj)
                    #print(self.entity_list)

                #Se for terreno
                elif isinstance(obj, Terrain):
                    self.tiles.append(obj)
                    # print(obj.rect)
                    # print(obj.surf)

                #Se for ar
                else:
                    pass

        # Da Camera
        map_width = len(level_obj[0]) * TILE_SIZE #Largura apenas de uma das linhas
        map_height = len(level_obj) * TILE_SIZE #Altura do total
        camera = Camera(map_width, map_height)  # tamanho do cenário inteiro

        while True:
            # Considera carregamento a cada 60 ticks
            delay = clock.tick(60)

            # se tiver matado um inimigo
            if time_stop:
                time_controller += delay
            else:
                game_time += delay

            # se tiver passado 10s depois de matar um inimigo
            if time_controller >= 10000:
                time_stop = False

            # Armazenamento apenas para exibição
            ms  = (game_time % 1000) // 10
            sec = (game_time // 1000) % 60
            min = (game_time // 60000)


            self.window.fill((0, 0, 0))

            #Desenho de imagens de fundo
            for img in self.bg:
                img.draw(self.window, camera)

            # #print(len(self.tiles))
            # for ls in range(len(self.tiles)):
            #     drawn_tile = self.tiles[ls]
            #     #print(len(self.tiles))
            #     self.window.blit(drawn_tile.surf, drawn_tile.rect)


            for ent in self.entity_list:

                #Métodos do player
                if isinstance(ent,Player):

                    #exibição da vida
                    ent.score_show = f"{min:02}:{sec:02}:{ms:02}"
                    self.text_level(30, f'Player1 - Health: {ent.health} | Score: {ent.score_show}', COLOR_WHITE, (10, 25))
                    
                    #Alterar aplicação para keys no level???????????????????????????????????????????????????????????????????????????? (final do arquivo)
                    pressed = pygame.key.get_pressed()
                    anda = ent.walk(map_width)
                    ent.jump()
                    soco = ent.punch()
                    ent.apply_gravity(self.tiles)

                    #VFerifica qual animação tocar
                    if not ent.on_ground: #Se o personagem não estiver no chão (caindo? Considerar)
                        sprite_set = "Jump"
                    elif anda:
                        if pressed == pygame.K_SPACE:
                            sprite_set = "Run"
                        else:
                            sprite_set = "Walk"
                    elif soco:
                        sprite_set = "Attack"
                    else:
                        sprite_set = "Idle"

                    #Update do player
                    ent.upd(ent.name, ent.position, sprite_set, "Blue", delay)

                    # atualiza câmera no player
                    dx = camera.update(ent.rect)
                    

                    #Parallax
                    for img in self.bg:
                        img.move(dx)

                    ent.score = game_time

                    if ent.rect.x >= map_width-300:
                        score[0] = ent.score
                        return True


                elif isinstance(ent, Enemy):
                    #Caminhada do inimigo
                    e_walk = ent.walk()
                    ent.apply_gravity(self.tiles)

                    #Animação sendo tocada
                    if e_walk:
                        e_sprite_set = 'Walk'
                    else:
                        e_sprite_set = "Walk"

                    #Update do Enemy
                    ent.upd(ent.name,ent.position,e_sprite_set, ent.tipo, delay)
                    
            # desenha tiles
            for tile in self.tiles:
                #Aplica o movimento de câmera aos tiles
                self.window.blit(tile.surf, camera.apply(tile.rect))

            # desenha entidades
            for ent in self.entity_list:
                #Aplica o movimento de câmera às entidades
                self.window.blit(ent.surf, camera.apply(ent.rect))

            pygame.display.flip()

            #Verificador de colisões entre entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            matou = EntityMediator.verify_health(entity_list=self.entity_list)

            if matou:
                time_stop = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print('Encerrando')
                    quit()

            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True

            if not found_player:
                return False


    def text_level(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

