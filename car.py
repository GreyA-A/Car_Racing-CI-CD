import pygame
import math

class Car:
    def __init__(self, start_pos):
        self.original_image = pygame.Surface((40, 20), pygame.SRCALPHA)
        self.original_image.fill((255, 0, 0))  # Red car
        self.image = self.original_image
        self.rect = self.image.get_rect(center=start_pos)

        self.pos = pygame.math.Vector2(start_pos)
        self.angle = 0
        self.speed = 0

        self.max_speed = 5
        self.acceleration = 0.2
        self.rotation_speed = 4
    
    def accelerate(self):
        self.speed = min(self.speed + self.acceleration, self.max_speed)

    def brake(self):
        self.speed = max(self.speed - self.acceleration * 2, -self.max_speed / 2)
    
    def apply_friction(self):
        if self.speed > 0:
            self.speed = max(self.speed - self.acceleration / 2, 0)
        elif self.speed < 0:
            self.speed = min(self.speed + self.acceleration / 2, 0)
    
    def turn(self, direction):
        # direction: 1 for left, -1 for right
        if abs(self.speed) > 0.1:
            self.angle += direction * self.rotation_speed