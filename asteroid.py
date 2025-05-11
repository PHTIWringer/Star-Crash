import pygame
    
class Asteroid:
    def __init__(self, x, y, dx, dy, radius, image=None):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.image = image

    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def move(self, screen_width, screen_height):
        self.x += self.dx
        self.y += self.dy

        self.x %= screen_width
        self.y %= screen_height
    
    def draw(self, screen):
        if self.image:
            # print("Drawing ball image")
            screen.blit(self.image, (self.x - self.radius, self.y - self.radius))
        else:
            # print("Drawing fallback circle")
            pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
