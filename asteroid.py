import random
import pygame
import circleshape
import constants


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"),
                           self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > constants.ASTEROID_MIN_RADIUS:
            new_angle = random.uniform(20, 50)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

            vel1 = self.velocity.rotate(new_angle)
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = vel1 * 1.2

            vel2 = self.velocity.rotate(-new_angle)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = vel2 * 1.2