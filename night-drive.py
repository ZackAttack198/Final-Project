import pygame
import glob
import os
from PIL import Image
import math
import random


class Road():

    def __init__(self, y, tile_width=500, height=220,
                 road_color=(60, 60, 60), dash_color=(255, 200, 0)):
        self.y = y
        self.tile_width = tile_width
        self.height = height
        self.road_color = road_color
        self.dash_color = dash_color
    
    def draw_tile(self, surface, x):
        road_tile = pygame.Rect(x, self.y, self.tile_width, self.height)
        pygame.draw.rect(surface, self.road_color, road_tile)

        dash_width = 50
        dash_height = 20
        gap = 20

        dash_y = road_tile.centery - dash_height // 2
        dash_x = x + 10

        while dash_x < x + self.tile_width:
            pygame.draw.rect(surface, self.dash_color,
                             (dash_x, dash_y, dash_width, dash_height))
            dash_x += dash_width + gap

    def draw(self, surface):
        screen_width = surface.get_width()

        for x in range(-500, 0):
            self.draw_tile(surface, x)


class Car():

    def __init__(self):
        pass
        
        
class City():

    def __init__(self):
        pass


class Stars():

    def __init__(self):
        pass


class Firework():

    def __init__(self):
        pass


def main():
    pygame.init()
    pygame.display.set_caption("Night Drive")
    clock = pygame.time.Clock()
    dt = 0
    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h
    resolution = (width, height)
    screen = pygame.display.set_mode(resolution)
    road = Road(y=resolution[1]-220, tile_width=500, height=220)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill("black")
        road.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30)
    pygame.quit()


if __name__ == "__main__":
    main()