# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        pygame.display.flip()
        delta = timer.tick(60)
        dt = delta/1000


if __name__ == "__main__":
    main()
