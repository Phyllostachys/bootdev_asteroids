import pygame
import constants
import player
import asteroid
import asteroidfield
import shot


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

    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (updateable, drawable, asteroids)

    asteroidfield.AsteroidField.containers = (updateable)
    asteroid_field = asteroidfield.AsteroidField()

    shots = pygame.sprite.Group()
    shot.Shot.containers = (updateable, drawable, shots)

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

        for a in asteroids:
            if p.check_collision(a):
                print("Game over!")
                running = False
            
            for s in shots:
                if s.check_collision(a):
                    a.split()
                    s.kill()

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
