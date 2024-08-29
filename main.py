import pygame
# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
from player import *
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f'''Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, 'black', rect=None, special_flags=0)
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
