import pygame
import math

bullet_color = (255, 0, 0)
class Bullet:
    def __init__(self, x, y, angle, speed=10):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.radius = 6

        rad = math.radians(angle)
        self.dx = -speed * math.sin(rad)
        self.dy = -speed * math.cos(rad)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, (bullet_color), (int(self.x), int(self.y)), self.radius)

    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
