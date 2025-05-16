import pygame, sys
from viewport import WIDTH, HEIGHT, background
from spaceship import Spaceship
from level_manager import get_asteroids, load_level
from config import levels as level_data
from config import upgrades as upgrade_data
from projectiles import Bullet
import json, os
from config import player_data

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Star Crash')
clock = pygame.time.Clock()
last_shot_time = 0
INVINCIBILITY_DURATION = 3000
last_respawn_time = 0
lives = 3
game_over = False
level_names = list(level_data.keys())  # ["level_one", "level_two", ...]
current_level_index = 0
level = level_names[current_level_index]
show_level_screen = True
level_intro_time = 0
ready_to_start = False
death_flash = False
death_flash_start = 0
FLASH_DURATION = 1000  # milliseconds
ship = Spaceship(WIDTH // 2, HEIGHT // 2)
bullets = []
score_money = 50 # currency per asteroid broke

SAVE_FILE = os.path.join(os.path.dirname(__file__), "player_save.json")

def reset_ship():
    global last_respawn_time
    ship.x = WIDTH // 2
    ship.y = HEIGHT // 2         
    ship.vx = 0
    ship.vy = 0
    ship.angle = 0
    last_respawn_time = pygame.time.get_ticks()

def draw_level_text(level_name):
    font = pygame.font.SysFont(None, 48)
    text = font.render(f"{level_name.replace('_', ' ').title()}", True, (255, 255, 255))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)

    if level_name == "level_one":
        font_small = pygame.font.SysFont(None, 32)
        text2 = font_small.render("Press SPACE to begin", True, (255, 255, 255))
        rect2 = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        screen.blit(text2, rect2)

def load_player_data():
    global player_data
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            player_data = json.load(f)

load_player_data()

def apply_upgrade(ship, upgrade_name):
    global FIRE_DELAY
    upgrade = upgrade_data[upgrade_name]
    price = upgrade["price"]

    if player_data["money"] < price:
        print("Not enough money")
        return

    if upgrade_name == "fire_rate":
        if player_data["upgrades"]["fire_rate"] + upgrade["increment"] < upgrade["min_value"]:
            print("Fire rate maxed out")
            return
        player_data["money"] -= price
        player_data["upgrades"]["fire_rate"] += upgrade["increment"]

    elif upgrade_name == "max_speed":
        if ship.max_speed + upgrade["increment"] > upgrade["max_value"]:
            print("Speed maxed out")
            return
        player_data["money"] -= price
        ship.max_speed += upgrade["increment"]

    elif upgrade_name == "bullet_speed":
        if player_data["upgrades"]["bullet_speed"] + upgrade["increment"] > upgrade["max_value"]:
            print("Bullet speed maxed out")
            return
        player_data["money"] -= price
        player_data["upgrades"]["bullet_speed"] += upgrade["increment"]

    print(f"{upgrade_name} upgraded!")

def save_player_data():
    with open(SAVE_FILE, "w") as f:
        json.dump(player_data, f, indent=4)

def main():
    global last_shot_time, lives, game_over, level
    global show_level_screen, level_intro_time, ready_to_start
    global current_level_index
    global death_flash, death_flash_start
    global last_respawn_time

    static_keys_released = True

    load_level(level)
    level_intro_time = pygame.time.get_ticks()
    show_level_screen = True
    ready_to_start = False

    while True:
        screen.blit(background, (0, 0))
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Show level text and pause logic
            if show_level_screen:
                if level == "level_one":
                    if not ready_to_start:
                        if any(keys):
                            show_level_screen = False
                            ready_to_start = True
                        else:
                            draw_level_text(level)
                            pygame.display.flip()
                            continue
                else:
                    if current_time - level_intro_time < 1000:
                        draw_level_text(level)
                        pygame.display.flip()
                        continue
                    else:
                        show_level_screen = False

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        apply_upgrade(ship, "fire_rate")
                    elif event.key == pygame.K_2:
                        apply_upgrade(ship, "max_speed")
                    elif event.key == pygame.K_3:
                        apply_upgrade(ship, "bullet_speed")
        
        if show_level_screen:
            draw_level_text(level)
            pygame.display.flip()
            continue

        if keys[pygame.K_SPACE] and current_time - last_shot_time > player_data["upgrades"]["fire_rate"]:
            bullets.append(ship.fire())
            last_shot_time = current_time

        ship.handle_input(keys)
        ship.update()
        ship.x %= WIDTH
        ship.y %= HEIGHT

        ship.thrusting = keys[pygame.K_UP]
        ship.update_particles()
        ship.draw_particles(screen)

        for bullet in bullets:
            bullet.move()
            bullet.draw(screen)

        asteroid_list = get_asteroids()
        for asteroid in asteroid_list:
            if asteroid.homing:
                asteroid.target = (ship.x, ship.y)
            asteroid.move(WIDTH, HEIGHT)
            asteroid.draw(screen)

        asteroid_list = get_asteroids()
        for bullet in bullets[:]:
            bullet_rect = bullet.rect()
            for asteroid in asteroid_list[:]:  # iterate over a copy of same list
                if bullet_rect.colliderect(asteroid.rect()):
                    bullets.remove(bullet)
                    asteroid_list.remove(asteroid)
                    player_data["money"] += score_money
                    new_asteroids = asteroid.split()
                    asteroid_list.extend(new_asteroids)
                    break

                if bullet_rect.colliderect(asteroid.rect()):
                    bullets.remove(bullet)
                    get_asteroids().remove(asteroid)
                    player_data["money"] += score_money
                    new_asteroids = asteroid.split()
                    get_asteroids().extend(new_asteroids)
                    break

        ship_rect = ship.rect
        for asteroid in get_asteroids():
            if current_time - last_respawn_time > INVINCIBILITY_DURATION:
                if ship_rect.colliderect(asteroid.rect()):
                    lives -= 1
                    reset_ship()
                    death_flash = True
                    death_flash_start = pygame.time.get_ticks()
                    if lives <= 0:
                        game_over = True
                    break
 
        if not get_asteroids() and not game_over:
            current_level_index += 1
            if current_level_index < len(level_names):
                level = level_names[current_level_index]
                load_level(level)
                level_intro_time = pygame.time.get_ticks()
                last_respawn_time = level_intro_time 
                show_level_screen = True
            else:
                save_player_data()
                print("YOU WIN")
                pygame.quit()
                sys.exit()

        if game_over:
            save_player_data()
            print("GAME OVER")
            pygame.quit()
            sys.exit()

        rotated_image, rotated_rect = ship.draw()
        screen.blit(rotated_image, rotated_rect)

        if death_flash:
            if pygame.time.get_ticks() - death_flash_start < FLASH_DURATION:
                flash_overlay = pygame.Surface((WIDTH, HEIGHT))
                flash_overlay.fill((255, 0, 0))
                flash_overlay.set_alpha(100)  # semi-transparent
                screen.blit(flash_overlay, (0, 0))
            else:
                death_flash = False

        pygame.display.flip()
        clock.tick(60)

main()
