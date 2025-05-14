import random, pygame
from config import levels
from viewport import WIDTH, HEIGHT
from asteroid import Asteroid

current_level = "level_one"
asteroids = []

def load_level(level_name):
    global current_level, asteroids
    level_data = levels[level_name]
    current_level = level_name
    asteroids = []

    count = level_data["count"]
    radius = level_data["radius"]
    speed_range = level_data["speed_range"]
    accel = level_data.get("acceleration", 0)
    rotation = level_data.get("rotation_speed", 0)

    image_path = level_data.get("image")

    if image_path:
        original = pygame.image.load(image_path).convert_alpha()

    for _ in range(count):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        dx = random.uniform(*speed_range)
        dy = random.uniform(*speed_range)

        scaled = pygame.transform.scale(original, (radius * 2, radius * 2))

        asteroids.append(Asteroid(
            x, y, dx, dy, radius,
            image=scaled,
            level=3,
            acceleration=accel,
            rotation_speed=rotation
        ))

def get_asteroids():
    return asteroids

def next_level():
    if current_level == "level_one":
        load_level("level_two")
    else:
        print("No more levels.")
