from asteroid import *
from player import *
from asteroidfield import *
from shot import *
from player import Player
from constants import *
from turtledemo.penrose import draw
import pygame
import sys
from operator import contains

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    shots = pygame.sprite.Group()
    Shot.containers = (shots ,updateable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2 ,SCREEN_HEIGHT / 2)
    dt = 0  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return            
        
        updateable.update(dt)
        
        for asteroid in asteroids:
            collide = asteroid.collision(player)
            if collide:
                print("Game over!")
                sys.exit()
        
       
        for drawable_element in drawable:
            drawable_element.draw(screen)
            
        pygame.display.flip()
        #drawable.draw(screen)
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
    