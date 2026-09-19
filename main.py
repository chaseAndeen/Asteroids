import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player    import Player
from logger    import log_state


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

    # --- Player Initialization ---
    Player.containers = (updatable, drawable)
    x                 = SCREEN_WIDTH / 2
    y                 = SCREEN_HEIGHT / 2
    player            = Player(x, y)

    # --- Game Loop ---
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
