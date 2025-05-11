import random, config
from viewport import WIDTH, HEIGHT
from asteroid import Asteroid

total_asteroids = config.levels["level_one"]
asteroids = []

# Push asteroid count to screen (only 1 level for now)
def num_of_asteroids():
    for _ in range(total_asteroids):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        dx = random.uniform(-2, 2)
        dy = random.uniform(-2, 2)
        radius = config.asteroid_radius
        asteroids.append(Asteroid(x, y, dx, dy, radius, image=None))

num_of_asteroids()