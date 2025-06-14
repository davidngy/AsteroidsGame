from circleshape import *
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        #takes surface, color, center, radius as arguments 
        figure = pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
