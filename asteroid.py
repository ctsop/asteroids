from circleshape import *
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, WHITE
from main import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, asteroids):
        super().__init__(x, y, radius)

        self.asteroids = asteroids
    

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
    

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(random_angle)
            vector_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, self.asteroids) 
            split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, self.asteroids) 
            split_asteroid_1.velocity = vector_1 * 1.2
            split_asteroid_2.velocity = vector_2 * 1.2
            self.asteroids.add(split_asteroid_1)
            self.asteroids.add(split_asteroid_2)