import random
import pygame
import math


class Circle():
    def __init__(self, radius=20, color=(0, 0, 0), window_width=1288, window_height=720):
        self.radius = radius
        self.color = color
        self.x = 0
        self.y = 0
        self.window_width = window_width
        self.window_height = window_height
        self.clicked = False
        self.spawn()

    def spawn(self):
        self.x = random.randint(self.radius, self.window_width - self.radius)
        self.y = random.randint(self.radius, self.window_height - self.radius)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color,
                           (self.x, self.y), self.radius)

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
