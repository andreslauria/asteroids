# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player1 = Player(constants.SCREEN_WIDTH / 2,constants.SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        for ast in asteroids:
            if ast.collision(player1):
                print("Game Over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        delta = timer.tick(60)
        dt = delta/1000


if __name__ == "__main__":
    main()
