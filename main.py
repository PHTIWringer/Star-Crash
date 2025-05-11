import pygame, sys
from viewport import WIDTH, HEIGHT, background
from spaceship import Spaceship
from game_state import asteroids

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Star Crash')
clock = pygame.time.Clock()

ship = Spaceship(WIDTH // 2, HEIGHT // 2)

def main():
    while True:
        screen.blit(background, (0, 0))

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ship.handle_input(keys)
        ship.update()
        ship.x %= WIDTH
        ship.y %= HEIGHT

        rotated_image, rotated_rect = ship.draw()
        screen.blit(rotated_image, rotated_rect)

        for asteroid in asteroids:
            asteroid.move(WIDTH, HEIGHT)
            asteroid.draw(screen)

        pygame.display.flip()
        clock.tick(60)

main()
