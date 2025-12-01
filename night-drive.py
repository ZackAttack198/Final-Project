import pygame
import math
import random


class Road():

    def __init__(self, y, tile_width=500, height=220, speed=12,
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

    def __init__(self, y_base, speed=2, color=(78, 0, 78)):
        self.y_base = y_base
        self.speed = speed
        self.color = color

        self.chunk_width = 600
        self.offset = 0

        self.building_chunks = [
            (0, y_base - 160, 60, 160),
            (60, y_base - 360, 100, 360),
            (160, y_base - 200, 60, 200),
            (220, y_base - 300, 80, 300),
            (300, y_base - 120, 50, 120),
            (350, y_base - 260, 70, 260),
            (420, y_base - 320, 100, 320),
            (520, y_base - 190, 80, 190)
        ]

    def draw(self, surface):
        screen_width = surface.get_width()

        num_chunks = (screen_width // self.chunk_width) + 2

        for num in range(num_chunks):
            chunk_x = self.offset + num * self.chunk_width

            for x, y, width, height in self.building_chunks:
                pygame.draw.rect(
                    surface,
                    self.color,
                    pygame.Rect(x + chunk_x, y, width, height)
                )

    def scroll(self):
        self.offset -= self.speed
        if self.offset <= -self.chunk_width:
            self.offset = 0
            

class Stars():

    def __init__(self, pos=(0, 0), size=10):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(189, 246, 255)
        self.age = 0
        self.alpha = 255
        self.surface = self.update_surface()

    def twinkle(self, dt):
        rand_multiplier = random.uniform(0.1, 0.5)
        self.age += dt
        self.alpha = 255 * (math.sin(math.radians(self.age*rand_multiplier)) + 1) / 2

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
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

    # class elements
    car_img = pygame.image.load("flying_car.png")
    scaled_img = pygame.transform.scale(car_img, resolution)
    road = Road(y=resolution[1]-220, tile_width=500, height=220)
    skyline = Skyline(y_base=(resolution[1]-219), speed=2, color=(78, 0, 78))
    stars = []
    for num in range (150):
        rand_pos_X = random.randrange(0, (resolution[0]-9))
        rand_pos_y = random.randrange(0, 251)
        rand_pos = (rand_pos_X, rand_pos_y)
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
        skyline.draw(screen)
        skyline.scroll()
        road.draw(screen)
        road.scroll()
        screen.blit(scaled_img, (0, 0))
        for star in stars:
            star.twinkle(dt)
            star.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30)
    pygame.quit()


if __name__ == "__main__":
    main()