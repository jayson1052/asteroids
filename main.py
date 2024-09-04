import pygame
# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f'''Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, 'black', rect=None, special_flags=0)
        for drawable_item in drawable:
            drawable_item.draw(screen)
        for data in updatable:
            data.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
