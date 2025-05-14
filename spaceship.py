import pygame
import math
from projectiles import Bullet

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

        self.original_image = pygame.image.load("E:/VSCode Files/Star Crash/destroyer.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (60, 60))  # spaceship size
        self.original_image = pygame.transform.rotate(self.original_image, 90)  # rotate left to face upward
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))

        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))

        self.particles = []
        self.thrusting = False

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
        if keys[pygame.K_UP]:
            rad = math.radians(self.angle + 90)
            self.vx += self.acceleration * math.cos(rad)
            self.vy -= self.acceleration * math.sin(rad)

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
    
    def fire(self):
    # Distance from center to nose: use hypotenuse of half-width and half-height
        image_width, image_height = self.image.get_size()
        nose_offset = math.hypot(image_width / 2, image_height / 2)

        rad = math.radians(self.angle)
        nose_offset = 30
        nose_x = self.x - math.sin(rad) * nose_offset
        nose_y = self.y - math.cos(rad) * nose_offset

        return Bullet(nose_x, nose_y, self.angle)
        
        self.particles = []  # in __init__

    def update_particles(self):
        if self.thrusting:
            angle_rad = math.radians(self.angle)
            offset = -30
            px = self.x - math.sin(angle_rad) * offset
            py = self.y - math.cos(angle_rad) * offset
            self.particles.append([px, py, 10])  # [x, y, life]

        # Update particles: shrink life and remove old ones
        self.particles = [[x, y, life - 0.5] for x, y, life in self.particles if life > 0]

    def draw_particles(self, screen):
        for x, y, life in self.particles:
            color = (255, 100, 0)
            pygame.draw.circle(screen, color, (int(x), int(y)), int(life))

