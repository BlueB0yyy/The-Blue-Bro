#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Camera import Camera
from code.const import TILE_SIZE, COLOR_GREEN
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player
from code.terrain import Terrain


class Level:
    def __init__(self, window, name, score: int):
        self.window = window # janela (global)
        self.name = name # nome do nível

        self.entity_list: list[Entity] = [] #lista de ENTIDADES
        self.tiles: list[Terrain] = [] #lista de TERRENOS
        self.tile_map = EntityFactory.load_level(self.name)  #lista de INDEX de elementos
        self.bg = EntityFactory.create_bg(self.name) #Criação do Bg

        #print(self.entity_list)

    def run(self, ):
        pygame.mixer_music.load('./asset/Sound/Game/Menu.wav')
        pygame.mixer_music.play(-1)

        time_start = pygame.time.get_ticks()


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

            # todo melhorar tempo e incrementar no score
            tempo = (pygame.time.get_ticks() - time_start)

            # Armazenamento apenas para exibição (replicar na exibição do score depois)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # (TESTAR!!!!!!!!!!!!!!)
            ms = tempo // 10 #??????????????????
            sec = tempo // 1000
            min = sec // 60


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


                    # Todo fazer o tempo não contar score se o player tiver morrido (senão vira jogo de quem morre mais rápido)
                    ent.score = f'{min}:{sec}:{ms}'

                    self.text_level(30, f'Player1 - Health: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 25))
                    
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

                    # Diferença no eixo X
                    dx_player = ent.rect.x - ent.prev_x
                    print(f'rect_x = {ent.rect_x}')
                    print(f'prev_x = {ent.prev_x}')
                    print(f'dx_player' = {dx_player})
                    

                    #Parallax (TODO fix parallax aqui)
                    for img in self.bg:
                        img.move(dx_player)

                elif isinstance(ent, Enemy):
                    #Caminhada do inimigo (TODO implementar ou com range ou com detecção de cenário)
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

            #Verificador de colisões entre entidades (TODO fazer funfar)
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print('Encerrando')
                    quit()

    def text_level(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

