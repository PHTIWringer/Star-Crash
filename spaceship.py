import pygame
import math

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

        self.vx = 0
        self.vy = 0

        self.acceleration = .5
        self.max_speed = 100
        self.drag = 0.985  # slow friction

        self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (255, 255, 255), [(0, 30), (20, 0), (40, 30)])
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
        if keys[pygame.K_UP]:
            rad = math.radians(self.angle)
            self.vx += self.acceleration * math.sin(rad)
            self.vy -= self.acceleration * math.cos(rad)

            # Limit speed
            speed = math.hypot(self.vx, self.vy)
            if speed > self.max_speed:
                scale = self.max_speed / speed
                self.vx *= scale
                self.vy *= scale

    def update(self):
        self.vx *= self.drag
        self.vy *= self.drag

        self.x += self.vx
        self.y += self.vy
        self.rect.center = (self.x, self.y)

    def draw(self):
        rotated = pygame.transform.rotate(self.original_image, self.angle)
        rotated_rect = rotated.get_rect(center=self.rect.center)
        return rotated, rotated_rect