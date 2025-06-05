import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK = (0, 0, 0)
    fps = pygame.time.Clock()

    player1 = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    
    # Pass the asteroids group to AsteroidField
    asteroidfield = AsteroidField(asteroids)  

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player1):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()