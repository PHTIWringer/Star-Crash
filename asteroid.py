import pygame, random, math
    
class Asteroid:
    def __init__(self, x, y, dx, dy, radius, image=None, level=3, acceleration=0, rotation_speed=0, homing=False):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.image = image
        self.level = level
        self.acceleration = acceleration
        self.rotation_speed = rotation_speed
        self.angle = 0
        self.homing = homing

    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def move(self, screen_width, screen_height):
        # Apply acceleration
        if self.homing and hasattr(self, "target"):
    # vector toward ship
            tx, ty = self.target
            direction = math.atan2(ty - self.y, tx - self.x)
        else:
            direction = math.atan2(self.dy, self.dx)

        self.dx += self.acceleration * math.cos(direction)
        self.dy += self.acceleration * math.sin(direction)

        self.x += self.dx
        self.y += self.dy

        # Wrap
        self.x %= screen_width
        self.y %= screen_height

        # Rotate
        self.angle = (self.angle + self.rotation_speed) % 360
    
    def draw(self, screen):
        if self.image:
            rotated = pygame.transform.rotate(self.image, self.angle)
            rect = rotated.get_rect(center=(int(self.x), int(self.y)))
            screen.blit(rotated, rect)
        else:
            pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)


    def split(self):
        if self.level > 1:
            new_level = self.level - 1
            new_radius = self.radius // 2
            fragments = []

            #  Resize the current image if it exists
            if self.image:
                scaled_image = pygame.transform.scale(self.image, (new_radius * 2, new_radius * 2))
            else:
                scaled_image = None

            # Generate new smaller asteroids
            for _ in range(2):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(1.5, 3.5)
                dx = speed * math.cos(angle)
                dy = speed * math.sin(angle)
                fragments.append(Asteroid(
                    self.x, self.y,
                    dx, dy,
                    new_radius,
                    image=scaled_image,
                    level=new_level,
                    acceleration=self.acceleration * 1.1,
                    rotation_speed=self.rotation_speed * 1.2
                ))

            return fragments

        return []
