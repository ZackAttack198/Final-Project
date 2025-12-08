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

        self.chunk_width = 660
        self.offset = 0

        self.building_chunks = [
            (0, y_base - 160, 72, 160),
            (72, y_base - 360, 100, 360),
            (172, y_base - 190, 58, 190),
            (230, y_base - 300, 86, 300),
            (316, y_base - 120, 72, 120),
            (388, y_base - 260, 86, 260),
            (474, y_base - 320, 100, 320),
            (574, y_base - 220, 86, 220)
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
                self.draw_windows(surface, x + chunk_x, y, width, height)

    def draw_windows(self, surface, building_x, building_y, width, height):
        window_color = (0, 170, 255)
        window_width = 8
        window_height = 12
        spacing_x = 6
        spacing_y = 10

        start_x = building_x + 10
        start_y = building_y + 10

        y = start_y
        while y + window_height < building_y + height - 10:
            x = start_x
            while x + window_width < building_x + width - 10:

                    pygame.draw.rect(surface, window_color,
                                    pygame.Rect(x, y, window_width, window_height))
                    
                    x += window_width + spacing_x
            y += window_height + spacing_y

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
        rand_mult = random.uniform(0.1, 0.5)
        self.age += dt
        self.alpha = 255 * (math.sin(math.radians(self.age*rand_mult)) + 1) / 2

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)


class FireworkParticle():

    def __init__(self, pos, velocity, lifetime, color, size, gravity):
        self.pos = pygame.Vector2(pos)
        self.velocity = pygame.Vector2(velocity)
        self.lifetime = lifetime
        self.age = 0
        self.color = color
        self.size = size
        self.gravity = gravity

    def update(self, dt):        
        self.velocity.y += self.gravity * dt
        self.pos += self.velocity * dt
        self.age += dt

    def draw(self, surface):
        time = self.age / self.lifetime
        if time > 1:
            return
        alpha = max(0, int(255 * (1 - time)))
        color = (*self.color, alpha)

        particle = pygame.Rect(
                               int(self.pos.x),
                               int(self.pos.y),
                               self.size,
                               self.size
                               )

        pygame.draw.rect(surface, color, particle)

    def alive(self):
        return self.age < self.lifetime


class Firework():

    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.particles = []
        self._create_burst()

    def _create_burst(self):
        count = random.randint(50, 100)
        base_color = random.choice([
            (255, 0, 0),
            (255, 100, 0),
            (255, 220, 0),
            (0, 255, 0),
            (0, 255, 255),
            (0, 0, 255),
            (150, 0, 255)
        ])

        for num in range(count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(80, 300)
            velocity = pygame.Vector2(math.cos(angle) * speed,
                                      math.sin(angle) * speed)
            lifetime = random.uniform(0.8, 1.8)
            size = random.randint(3, 6)
            self.particles.append(FireworkParticle(self.position, velocity,
                                                   lifetime, base_color,
                                                   size, gravity=100))

    def update(self, dt):
        for p in self.particles:
            p.update(dt)
        self.particles = [p for p in self.particles if p.alive()]

    def draw(self, surf):
        for p in self.particles:
            p.draw(surf)

    def alive(self):
        return any(p.alive() for p in self.particles)


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
    road = Road(y=resolution[1]-220, tile_width=500, height=220, speed=12)
    stars = []
    for num in range (260):
        rand_pos_X = random.randrange(0, (resolution[0]-9))
        rand_pos_y = random.randrange(0, 601)
        rand_pos = (rand_pos_X, rand_pos_y)
        stars.append(Stars(pos=rand_pos))
    skyline = Skyline(y_base=(resolution[1]-219), speed=2, color=(78, 0, 78))
    fireworks = []

    # game logic
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    fireworks.append(Firework(pygame.mouse.get_pos()))
        fireworks = [fw for fw in fireworks if fw.alive]
        for fw in fireworks:
            fw.update(dt)
        screen.fill((0, 0, 35))
        for star in stars:
            star.twinkle(dt * 1000)
            star.draw(screen)
        skyline.draw(screen)
        skyline.scroll()
        road.draw(screen)
        road.scroll()
        screen.blit(scaled_img, (0, -2))
        for fw in fireworks:
            fw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30) / 1000.0
    pygame.quit()


if __name__ == "__main__":
    main()