import pygame
import constants
import player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print(pygame.display.Info())

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updateable, drawable)

    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    p = player.Player(x, y)

    running = True
    while running:
        # update input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for item in updateable:
            item.update(dt)

        # render graphics
        screen.fill(pygame.Color("black"))
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # timer for 60 FPS
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
