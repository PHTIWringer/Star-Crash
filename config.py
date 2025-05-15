import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

# Levels
levels = {
    "level_one": {
        "count": 2,
        "radius": 100,
        "speed_range": (-1.5, 1.5),
        "acceleration": 0.001,
        "rotation_speed": 0.2,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_two": {
        "count": 3,
        "radius": 80,
        "speed_range": (-2, 2),
        "acceleration": 0.002,
        "rotation_speed": 0.3,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_three": {
        "count": 4,
        "radius": 75,
        "speed_range": (-2.5, 2.5),
        "acceleration": 0.003,
        "rotation_speed": 0.4,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_four": {
        "count": 5,
        "radius": 60,
        "speed_range": (-3, 3),
        "acceleration": 0.004,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_five": {
        "count": 6,
        "radius": 60,
        "speed_range": (-3, 3),
        "acceleration": 0.004,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_six": {
        "count": 7,
        "radius": 60,
        "speed_range": (-3, 3),
        "acceleration": 0.004,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_seven": {
        "count": 8,
        "radius": 60,
        "speed_range": (-3, 3),
        "acceleration": 0.004,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_eight": {
        "count": 9,
        "radius": 60,
        "speed_range": (-3, 3),
        "acceleration": 0.004,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_nine": {
        "count": 10,
        "radius": 60,
        "speed_range": (-3, 3),
        "acceleration": 0.004,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_ten": {
        "count": 3,
        "radius": 100,
        "speed_range": (-5, 5),
        "acceleration": 0.008,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_11": {
        "count": 8,
        "radius": 60,
        "speed_range": (-3, 3),
        "acceleration": 0.004,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_12": {
        "count": 9,
        "radius": 60,
        "speed_range": (-3, 3),
        "acceleration": 0.004,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    },
    "level_13": {
        "count": 15,
        "radius": 60,
        "speed_range": (-3, 3),
        "acceleration": 0.004,
        "rotation_speed": 0.5,
        "image": os.path.join(ASSETS_DIR, "meteor_detailed_NE.png")
    }
}

upgrades = {
    "fire_rate": {
        "price": 100,
        "increment": -25,  # reduce delay by 25 ms
        "min_value": 50
    },
    "max_speed": {
        "price": 150,
        "increment": 10,
        "max_value": 300
    },
    "bullet_speed": {
        "price": 200,
        "increment": 2,
        "max_value": 25
    }
}

player_data = {
    "name": "Ken",
    "score": 0,
    "money": 0,
    "upgrades": {
        "fire_rate": 200,
        "max_speed": 100,
        "bullet_speed": 10
    }
}
