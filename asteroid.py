
from circleshape import CircleShape
from circleshape import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        #takes surface, color, center, radius as arguments 
        figure = pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
   
    