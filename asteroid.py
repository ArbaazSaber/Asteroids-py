import pygame, random

from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if not self.radius > ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        rand_angle = random.uniform(20, 50)

        first_child_asteroid_velocity = self.velocity.rotate(rand_angle)
        second_child_asteroid_velocity = self.velocity.rotate(-rand_angle)

        child_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        first_child_asteroid = Asteroid(self.position.x, self.position.y, child_asteroid_radius)
        second_child_asteroid = Asteroid(self.position.x, self.position.y, child_asteroid_radius)
        first_child_asteroid.velocity = first_child_asteroid_velocity * 1.2
        second_child_asteroid.velocity = second_child_asteroid_velocity * 1.2