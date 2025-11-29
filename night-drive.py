import pygame
import glob
import os
import math
import random


class Road():

    def __init__(self, y, tile_width=500, height=220, speed=10,
                 road_color=(60, 60, 60), dash_color=(255, 200, 0)):
        self.y = y
        self.tile_width = tile_width
        self.height = height
        self.speed = speed
        self.road_color = road_color
        self.dash_color = dash_color
        self.offset = 0
    
    def draw_tile(self, surface, x):
        road_tile = pygame.Rect(x, self.y, self.tile_width, self.height)
        pygame.draw.rect(surface, self.road_color, road_tile)

        # dash settings
        dash_width = 50
        dash_height = 20
        gap = 21
        dash_y = road_tile.centery - dash_height // 2
        dash_x = x + 10

        while dash_x < x + self.tile_width:
            pygame.draw.rect(surface, self.dash_color,
                             (dash_x, dash_y, dash_width, dash_height))
            dash_x += dash_width + gap

    def draw(self, surface):
        screen_width = surface.get_width()

        for x in range(self.offset, screen_width + self.tile_width, self.tile_width):
            self.draw_tile(surface, x)

    def scroll(self):
        self.offset -= self.speed
        if self.offset <= -self.tile_width:
            self.offset = 0
        
        
class Skyline():

    def __init__(self):
        pass


class Stars():

    def __init__(self, pos=(0, 0), size=10):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(189, 246, 255)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
	    surface.blit(self.surface, self.pos)


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
    car_img = pygame.image.load("flying_car.png")
    scaled_img = pygame.transform.scale(car_img, resolution)
    road = Road(y=resolution[1]-220, tile_width=500, height=220)
    stars = []
    for num in range (100):
        rand_pos = random.randrange(0, (resolution[0]-9)),
        (0, random.randrange(391))
        stars.append(Stars(pos=rand_pos))


    # game logic
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill((0, 0, 35))
        road.draw(screen)
        road.scroll()
        screen.blit(scaled_img, (0, 0))
        for star in stars:
            Stars.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30)
    pygame.quit()


if __name__ == "__main__":
    main()