import pygame
import glob
import os
from PIL import Image
import math
import random


class Road():

    def __init__(self):
        pass


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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.flip()
        dt = clock.tick(30)
    pygame.quit()


if __name__ == "__main__":
    main()