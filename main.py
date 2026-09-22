import pygame
import sys
from constants     import SCREEN_WIDTH, SCREEN_HEIGHT
from player        import Player
from asteroid      import Asteroid
from asteroidfield import AsteroidField
from logger        import log_state, log_event
from shot          import Shot


def main():
    # --- Info ---
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # --- Initialization ---
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable  = pygame.sprite.Group()
    drawable   = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots      = pygame.sprite.Group()

    # --- Player Initialization ---
    Player.containers = (updatable, drawable)
    x                 = SCREEN_WIDTH / 2
    y                 = SCREEN_HEIGHT / 2
    player            = Player(x, y)

    # --- AsteroidField Initialization ---
    Asteroid.containers      = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield            = AsteroidField()

    # --- Shots Initialization ---
    Shot.containers = (shots, updatable, drawable)

    # --- Game Loop ---
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
