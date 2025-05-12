import pygame, sys
from viewport import WIDTH, HEIGHT, background
from spaceship import Spaceship
from level_manager import get_asteroids, load_level

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Star Crash')
clock = pygame.time.Clock()
FIRE_DELAY = 200  # milliseconds between shots
last_shot_time = 0


ship = Spaceship(WIDTH // 2, HEIGHT // 2)
bullets = []

def main(): 
    global last_shot_time
    load_level("level_one")  # Initialize first level

    while True:
        screen.blit(background, (0, 0))
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if keys[pygame.K_SPACE] and current_time - last_shot_time > FIRE_DELAY:
            bullets.append(ship.fire())
            last_shot_time = current_time

        ship.handle_input(keys)
        ship.update()
        ship.x %= WIDTH
        ship.y %= HEIGHT

        for bullet in bullets:
            bullet.move()
            bullet.draw(screen)
           
        for asteroid in get_asteroids():
            asteroid.move(WIDTH, HEIGHT)
            asteroid.draw(screen)  

        rotated_image, rotated_rect = ship.draw()
        screen.blit(rotated_image, rotated_rect)

        pygame.display.flip()
        clock.tick(60)

main()
