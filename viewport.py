import pygame
from PIL import Image

# viewport
WIDTH = 1200
HEIGHT = 1000

# Background Image
img = Image.open("Background_image.png").convert("RGB")
img.save("Background_fixed.png", format="PNG")
background = pygame.image.load("E:/VSCode Files/Star Crash/Background_image.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
