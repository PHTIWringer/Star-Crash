import pygame
from PIL import Image
import os
from config import ASSETS_DIR

# viewport
WIDTH = 1200
HEIGHT = 1000

# Background Image
path = os.path.join(ASSETS_DIR, "Background_image.png")
img = Image.open(path).convert("RGB")
fixed_path = os.path.join(ASSETS_DIR, "Background_fixed.png")
img.save(fixed_path, format="PNG")

# load image with pygame
background = pygame.image.load(fixed_path)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
