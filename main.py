# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots_group,updatable,drawable)
    
    player1 = Player(constants.SCREEN_WIDTH / 2,constants.SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0
    
    puntaje = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        shots_group.update(dt)  
        texto_puntos = pygame.font.SysFont('comicsans',30,True)
        for ast in asteroids:
            if ast.collision(player1):
                print("Game Over!")
                sys.exit()
            for shot in shots_group:
                if ast.collision(shot):
                    ast.split()
                    shot.kill()
                    puntaje += 1
        for sprite in drawable:
            sprite.draw(screen)
        for shot in shots_group:
            shot.draw(screen)
        puntos  = texto_puntos.render('Puntaje: ' + str(puntaje),1,"white")
        screen.blit(puntos, (350,10))
        pygame.display.flip()
        delta = timer.tick(60)
        dt = delta/1000


if __name__ == "__main__":
    main()
