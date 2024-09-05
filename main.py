import pygame, random, sys 
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
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

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, 'black', rect=None, special_flags=0)
        for drawable_item in drawable:
            drawable_item.draw(screen)
        for data in updatable:
            data.update(dt)
        for asteroid_particle in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid_particle):
                    bullet.kill()
                    asteroid_particle.split()
            if asteroid_particle.collision(player):
                print("Game over!")
                sys.exit("Oops, you crashed into an asteroid! Try again next time!")
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
