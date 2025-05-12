import random
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

    for _ in range(count):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        dx = random.uniform(*speed_range)
        dy = random.uniform(*speed_range)
        asteroids.append(Asteroid(x, y, dx, dy, radius, image=None))

def get_asteroids():
    return asteroids

def next_level():
    if current_level == "level_one":
        load_level("level_two")
    else:
        print("No more levels.")
