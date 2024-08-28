from circleshape import CircleShape
from constants import *
import pygame
class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.math.Vector2(x, y)
