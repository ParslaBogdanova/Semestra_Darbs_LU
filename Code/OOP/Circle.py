import random
import pygame
import math


class Circle():
    def __init__(self, radius=100, color=(0, 0, 0), window_width=720, window_height=720):
        self.radius = radius
        self.start_radius = radius
        self.color = color
        self.x = 0
        self.y = 0
        self.window_width = window_width
        self.window_height = window_height

        self.shrink_speed = 10

        self.hit_count = 0
        self.hit_levels_after_clicking = 5

        self.clicked = False
        self.spawn()

    def update(self, dt):
        self.radius -= self.shrink_speed * dt
        if self.radius < 0:
            print("miss")
            self.radius = 0

    def spawn(self):
        self.radius = self.start_radius
        self.x = random.randint(self.radius, self.window_width - self.radius)
        self.y = random.randint(self.radius, self.window_height - self.radius)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color,
                           (self.x, self.y), int(self.radius), width=3)

    def is_clicked(self, mouse_pos):
        dx = mouse_pos[0] - self.x
        dy = mouse_pos[1] - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance <= self.radius:
            self.clicked = True
            self.spawn()
            return True
        else:
            self.clicked = False
            return False

    def level_up(self):
        if self.hit_count % self.hit_levels_after_clicking == 0:
            self.shrink_speed += 5
            print(f"Speed: {self.shrink_speed}")
