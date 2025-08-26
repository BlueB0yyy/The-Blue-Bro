import pygame

from code.const import BG_WIDTH


class Camera:
    def __init__(self, map_width, map_height):
        self.offset = pygame.Vector2(0, 0)
        self.map_width = map_width
        self.map_height = map_height

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)

    def update(self, target_rect):
        # apenas eixo X
        self.offset.x = target_rect.centerx - BG_WIDTH // 2

        # limite para não sair do mapa
        self.offset.x = max(0, min(self.offset.x, self.map_width - BG_WIDTH))